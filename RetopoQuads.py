# -*- coding: utf-8 -*-    

bl_info = {  
 "name": "RetopoQuads",  
 "author": "Nedovizin Alexander",  
 "version": (0, 0, 11),  
 "blender": (2, 6, 9),  
 "location": "Console > QQUAD",  
 "description": "Create quads retopology",  
 "category": "Mesh"}   

import bpy
from mathutils import Vector

# http://dl.dropboxusercontent.com/u/59609328/Blender-Rus/RetopoQuads.py

def find_connected_verts(me, found_index, not_list):  
    edges = me.edges  
    connecting_edges = [i for i in edges if found_index in i.vertices[:] and \
        me.vertices[i.vertices[0]].select and me.vertices[i.vertices[1]].select]  
    if len(connecting_edges) == 0: 
        return []
    else:  
        connected_verts = []  
        for edge in connecting_edges:  
            fe = 0
            cvert = edge.vertices[:]
            for f in me.polygons:
                vf = []
                for v in f.vertices:
                    vf.append(v)
                
                if cvert[0] in vf and cvert[1] in vf: fe += 1
            if fe>1: continue

            cvert = set(cvert)
            cvert.remove(found_index)  
            vert = cvert.pop()
            if not (vert in not_list) and me.vertices[vert].select and \
                True:
                connected_verts.append(vert)  
        
        return connected_verts  
    
    
def find_all_connected_verts(me, active_v, not_list=[]):
    vlist = [active_v]
    not_list.append(active_v)
    list_v_1 = find_connected_verts(me, active_v, not_list)
    
    for v in list_v_1:
        list_v_2 = find_all_connected_verts(me, v, not_list) 
        vlist += list_v_2
        
    return vlist


def getLoops(me, verts):
    vsa = verts.copy()
    result = []
    while len(vsa)>0:
        loop = find_all_connected_verts(me,vsa[0],not_list=[])[:-1]
        for v in loop:
            vsa.remove(v)
        result.append(loop)
    return result


def createMeshFromData(name, origin, verts, faces):
    # Создание меша и объекта
    me = bpy.data.meshes.new(name+'Mesh')
    ob = bpy.data.objects.new(name, me)
    ob.location = origin
    ob.show_name = True
 
    # Привязка объекта к сцене, он становится активным
    scn = bpy.context.scene               
    scn.objects.link(ob)
    scn.objects.active = ob
    ob.select = True
 
    # Создание меша из полученных verts (вершин), faces (граней).
    me.from_pydata(verts, [], faces)
    # Обновление меша с новыми данными
    me.update()    
    return ob     


def vecscorrect(vec, vec0):
            norm = vec.normalized()

            mat_rot_norm = vec0.rotation_difference(norm).to_matrix().to_4x4()
            negative_mat = norm.rotation_difference(vec0).to_matrix().to_4x4()

            return mat_rot_norm, negative_mat


def select_planar(me, indx_face, origins = Vector((0,0,0))):
    bpy.ops.object.mode_set(mode='EDIT')  
    bpy.ops.mesh.select_mode(type='FACE')
    bpy.ops.mesh.select_all(action='DESELECT')
    bpy.ops.object.editmode_toggle()
    me.polygons[indx_face].select = True
    bpy.ops.object.editmode_toggle()
    
    # **********  start select magic  *********
    face = 0
    for i,f in enumerate(me.polygons):
        if f.select: 
            face = i
            break
        
    bpy.ops.mesh.select_all(action='DESELECT')    
    normal = me.polygons[face].normal.copy()
    
    bpy.ops.object.mode_set(mode='OBJECT') 
    vers_s = []
    pols = []
    for i,f in enumerate(me.polygons):
        mul = normal * f.normal
        if abs(mul)>1-1e-6:
            vers_s.extend([v for v in me.polygons[i].vertices])
            pols.append(f)

    flag = True
    faces = [face]
    eds = [v for v in me.polygons[face].edge_keys]
    while flag:
        flag = False
        eds_ = []
        for pp in pols:
            if pp.index in faces: 
                continue
    
            eds_ = [v for v in pp.edge_keys if v in eds or \
                (v[1],v[0]) in eds]
    
            if eds_!=[]: 
                flag = True
                faces.append(pp.index)
                eds.extend([v for v in pp.edge_keys])
        
    for f in faces:
        me.polygons[f].select = True
    # ***************  end select magic  **********
    
    v_dic = {}
    f_list = []
    v_list = []
    v_cou = 0

    bpy.ops.object.mode_set(mode='OBJECT')
    pols = [p for p in me.polygons if p.select]
    for i,f in enumerate(pols):
        v_ = []
        for iv, v in enumerate(f.vertices[:]):
            if v in v_dic:
                v_cou = v_dic[v]
            else:
                v_cou = len(v_list)
                v_dic[v] = v_cou
                v_list.append(me.vertices[v].co)
            v_.append(v_cou)
        
        f_list.append(v_)
    
    bpy.ops.object.mode_set(mode='OBJECT')
    bpy.ops.object.select_all(action='DESELECT')
    obj = createMeshFromData(name='tmp_QQ', origin=origins, verts=v_list, faces=f_list)
    return obj


def rotateZ(me):
    lv = (me.vertices[0].co, 0)
    bv = (me.vertices[0].co, 0)
    tv = (me.vertices[0].co, 0)
    
    for i,v in enumerate(me.vertices[1:]):
        if v.co.x < lv[0].x: lv = (v.co, i)
        if v.co.y > tv[0].y: tv = (v.co, i)
        if v.co.y < bv[0].y: bv = (v.co, i)
        
    medium = (tv[0].y + bv[0].y)/2
    v1 = bv[0]
    v2 = lv[0]
    if lv[0].y>medium:
        v1 = lv[0]
        v2 = tv[0]
    if lv[1]==bv[1]:
        v1 = lv[0]
        v2 = tv[0]
    
    vec_ = v2-v1
    mat, neg_mat = vecscorrect(vec=vec_, vec0 = Vector((0,1,1e-6)))
    return mat, neg_mat
        

def main(context):
    bpy.ops.object.editmode_toggle()
    bpy.ops.object.editmode_toggle()
    bpy.ops.object.mode_set(mode='EDIT')
    bpy.ops.mesh.select_mode(type='FACE')
    
    super_obj = bpy.context.active_object
    super_me = super_obj.data
    fs_super = [p.index for p in super_me.polygons if p.select]
    obs = []
    if fs_super:
        for f_super in fs_super:
            qquads(f_super)
            obs.append(bpy.context.active_object.name)
            bpy.ops.object.select_all(action='DESELECT')
            super_obj.select = True
            bpy.context.scene.objects.active = super_obj
        
        bpy.ops.object.select_all(action='DESELECT')
        for o in obs:
            obj = bpy.data.objects[o]
            obj.select = True
            bpy.context.scene.objects.active = obj
        bpy.ops.object.join()
        bpy.ops.object.mode_set(mode='EDIT')
        bpy.ops.mesh.select_mode(type='FACE')
        bpy.ops.mesh.select_all(action='SELECT')
        bpy.ops.mesh.remove_doubles()
        bpy.ops.mesh.select_all(action='DESELECT')
        

def qquads(f_super):
    maloe = 1e-5
    
    bpy.ops.object.mode_set(mode='EDIT')
    bpy.ops.mesh.select_mode(type='FACE')
    
    #print('\n *********   start    ********')
    
    obj = bpy.context.active_object
    me = obj.data
    
    bpy.ops.object.mode_set(mode='OBJECT')
    
    face = f_super
    ob = select_planar(me, face)
    ob.matrix_world = obj.matrix_world.copy()
    me = ob.data
    
    bpy.ops.object.mode_set(mode='EDIT')  
    bpy.ops.mesh.select_mode(type='VERT')
    bpy.ops.mesh.select_all(action='DESELECT')
    bpy.ops.mesh.select_non_manifold(extend=True)   
    bpy.ops.object.mode_set(mode='OBJECT')
    face = 0
    
    normal = me.polygons[face].normal
    mat, neg_mat = vecscorrect(normal, vec0 = Vector((1e-6,1e-6,1)))
    
    for i,v in enumerate(me.vertices):
        me.vertices[i].co = v.co*mat
    
    matz, neg_matz = rotateZ(me)
    for i,v in enumerate(me.vertices):
        me.vertices[i].co = v.co*matz
    
    bpy.ops.object.mode_set(mode='EDIT')    
    vs_all = [v.index for v in me.vertices if v.select]
    
    loop_all = getLoops(me, vs_all)
    loop_q = []
    loop_sq = []
    lx = []
    ly = []
    
    # оптимизировать прямоугольники
    for i,loop in enumerate(loop_all):
        list_x = []
        list_y = []
        for la in loop:
            list_x.append(me.vertices[la].co.x)
            list_y.append(me.vertices[la].co.y)
            
        list_x = set(list_x)
        list_y = set(list_y)
        
        c_left   = min(list_x)
        c_right  = max(list_x)
        c_top    = max(list_y)
        c_bottom = min(list_y)
        
        vlb = Vector((c_left, c_bottom, 0))
        vlt = Vector((c_left, c_top, 0))
        vrt = Vector((c_right, c_top, 0))
        vrb = Vector((c_right, c_bottom, 0))
        
        sq = vrb - vlb
        lx.extend([c_left, c_right])
        ly.extend([c_top, c_bottom])
        
        loop_sq.append((sq,i))    
        loop_q.append([vlb, vlt, vrt, vrb])
    
    # Получить каркас А
    loop_A = max(loop_sq)[1]
    
    for ix,x in enumerate(lx):
        if x<loop_q[loop_A][0].x: lx[ix]=loop_q[loop_A][0].x
        if x>loop_q[loop_A][3].x: lx[ix]=loop_q[loop_A][3].x
        
    for iy,y in enumerate(ly):
        if y<loop_q[loop_A][0].y: ly[iy]=loop_q[loop_A][0].y
        if y>loop_q[loop_A][2].y: ly[iy]=loop_q[loop_A][2].y
        
    # Разложить сетку
    lx.sort()
    ly.sort()
    
    lx_ = []
    ly_ = []
    for ix,x in enumerate(lx[:-1]):
        if abs(x-lx[ix+1])>maloe: lx_.append(x)
    for iy,y in enumerate(ly[:-1]):
        if abs(y-ly[iy+1])>maloe: ly_.append(y)
    lx_.append(lx[-1])
    ly_.append(ly[-1])
    
    lx = lx_
    ly = ly_
    loop_x = []
    verts = []
    faces = []
    for ix,vx in enumerate(lx[:-1]):
        v = Vector((vx, ly[0], loop_q[loop_A][0].z))
        idx = len(verts)
        verts.append(v)
        loop_x.append(idx)
        
    
    
    extr_rt = len(verts)
    verts.append(Vector((lx[-1], ly[0], loop_q[loop_A][0].z)))
    for y in ly[1:]:
        tmp_x = []
        num_lt = len(verts)
        verts.append(Vector((verts[loop_x[0]].x, y, verts[loop_x[0]].z)))
        
        for ix, line_x in enumerate(loop_x):
            if (verts[line_x].x-lx[ix])>maloe:
                loop_x.insert(ix+1, line_x) 
                continue
            
            xx=(verts[line_x].x+lx[ix+1])/2
            yy=(verts[line_x].y+y)/2
            
            flag = True
            for i,loop in enumerate(loop_q):
                if i==loop_A: continue
                
                if yy>loop[0].y and yy<loop[1].y and \
                   xx>loop[0].x and xx<loop[3].x:
                   flag = False
                   break
        
            if flag: 
                num_lb = line_x
                num_rb = -1
                
                num_rt = len(verts)
                verts.append(Vector((lx[ix+1], y, verts[line_x].z)))
                
                if ix+1<len(loop_x) and ix+2<len(lx):
                    # Это не крайний правый квадрат
                    if abs(verts[loop_x[ix+1]].x - lx[ix+1])<maloe:
                        num_rb = loop_x[ix+1]
                    else:
                        num_rb = len(verts)
                        verts.append(Vector((lx[ix+1], verts[line_x].y, verts[line_x].z)))
                        loop_x.insert(ix+1, num_rb)                    
                else:
                    num_rb = extr_rt
                    extr_rt = num_rt
                
                if num_lt==-1:
                    num_lt = len(verts)
                    verts.append(Vector((lx[ix], y, verts[line_x].z)))
                    
                
                faces.append([num_lb, num_lt, num_rt, num_rb])
                tmp_x.append(num_lt)
                num_lt = num_rt
            else:
                if num_lt>-1:
                    tmp_x.append(num_lt)
                num_lt = -1
            
        loop_x = tmp_x.copy()
    
    bpy.ops.mesh.select_all(action='DESELECT')
    bpy.ops.object.mode_set(mode='OBJECT')
  
    dz_ = me.vertices[0].co.z
    bpy.ops.object.select_all(action='DESELECT')
    
    ob.select = True
    bpy.ops.object.delete()
    
    ob = createMeshFromData(name='retopo object', origin=Vector((0,0,0)), verts=verts, faces=faces)
    ob.matrix_world = obj.matrix_world.copy()
    me = ob.data
    
    dz = dz_ - me.vertices[0].co.z 
    for i,v in enumerate(me.vertices):
        me.vertices[i].co.z = v.co.z+dz
        me.vertices[i].co = v.co*neg_matz*neg_mat
    

class QquadOperator(bpy.types.Operator):
    bl_idname = "mesh.qquad"
    bl_label = "QQUAD"
    bl_options = {'REGISTER', 'UNDO', 'PRESET'}   
    
    @classmethod
    def poll(cls, context):
        return context.active_object is not None
    
    def execute(self, context):
        main(context)
        return {'FINISHED'}   

def register():
    bpy.utils.register_class(QquadOperator)


def unregister():
    bpy.utils.unregister_class(QquadOperator)


if __name__ == "__main__":
    register()