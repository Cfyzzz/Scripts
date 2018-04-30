# -*- coding: utf-8 -*- 

bl_info = {
    "name": "Mat_extrude",                     
    "author": "Alexander Nedovizin",
    "version": (0, 0, 8),
    "blender": (2, 6, 9),
    "location": "View3D > Toolbar",
    "description": "Materials extrude",
    "category": "Mesh"
}        

# http://dl.dropboxusercontent.com/u/59609328/Blender-Rus/AutoExtrud.py

import bpy, bmesh
from mathutils import Vector

list_z = []
mats_idx = []
list_f = []
maloe = 1e-5

def getMats(context):
    global list_z, mats_idx, list_f, maloe
    
    obj = bpy.context.active_object
    me = obj.data
    
    bpy.ops.object.mode_set(mode='OBJECT')
    bpy.ops.object.mode_set(mode='EDIT') 
    bpy.ops.mesh.select_mode(type='VERT')
    
    list_z = [v.co.z for v in me.vertices if v.select]
    list_z = list(set(list_z))
    list_z.sort()
    
    bpy.ops.mesh.select_mode(type='FACE')
    list_f = [p.index for p in me.polygons if p.select]
    black_list = []
    mats_idx = []
    for z in list_z:
        for p in list_f:
            if p not in black_list:
                for v in me.polygons[p].vertices:
                    if abs(me.vertices[v].co.z-z)<maloe:
                        mats_idx.append(me.polygons[p].material_index)
                        black_list.append(p)
                        break
    bpy.ops.mesh.select_mode(type='VERT')
    
    


def main(context):
    global list_z, mats_idx, list_f, maloe
    
    obj = bpy.context.active_object
    me = obj.data
    
    bpy.ops.object.mode_set(mode='OBJECT')
    vert = [v.index for v in me.vertices if v.select][0]
    
    
    def find_index_of_selected_vertex(obj):  
        # force 'OBJECT' mode temporarily. [TODO]  
        selected_verts = [i.index for i in obj.data.vertices if i.select]  
        verts_selected = len(selected_verts)  
        if verts_selected <1:                   
            return None  
        else:  
            return selected_verts 
        
        
    def find_connected_verts(me, found_index, not_list):  
        edges = me.edges  
        connecting_edges = [i for i in edges if found_index in i.vertices[:]]  
        if len(connecting_edges) == 0: 
            return []
        else:  
            connected_verts = []  
            for edge in connecting_edges:  
                cvert = set(edge.vertices[:])   
                cvert.remove(found_index)  
                vert = cvert.pop()
                if not (vert in not_list) and me.vertices[vert].select:
                    connected_verts.append(vert)  
            return connected_verts  
        
        
    def find_all_connected_verts(me, active_v, not_list=[], step=0):
        vlist = [active_v]
        not_list.append(active_v)
        step+=1
        list_v_1 = find_connected_verts(me, active_v, not_list)
        
        for v in list_v_1:
            list_v_2 = find_all_connected_verts(me, v, not_list, step) 
            vlist += list_v_2
                     
        return vlist  
        
    
    
    bm = bmesh.new()
    bm.from_mesh(me)
    
    verts = find_all_connected_verts(me,vert)
    vts = [bm.verts[vr] for vr in verts]
    face_build = []
    face_build.extend(verts)
    fl = len(bm.verts)+1
    for zidx,z in enumerate(list_z):
        vts_tmp = []
        for i,vs in enumerate(vts[:-1]):
            vco1 = vs.co
            vco2 = vts[i+1].co
            vco1.z = z
            vco2.z = z
            if i==0:
                v1 = bm.verts.new(vco1)
                face_build.append(len(bm.verts)-1)
            else:
                v1=v2
            v2 = bm.verts.new(vco2)
            face_build.append(len(bm.verts)-1)
            f = bm.faces.new([vs,v1,v2,vts[i+1]])
            f.material_index = mats_idx[min(zidx, len(mats_idx)-1)]
            if i==0:
                vts_tmp.append(v1)
            vts_tmp.append(v2)
        vts = vts_tmp.copy()
        
    bpy.ops.object.mode_set(mode='OBJECT')
    bm.to_mesh(me) 
    bm.free() 
    
    bpy.ops.object.mode_set(mode='EDIT') 
    bpy.ops.mesh.select_mode(type='FACE')
    bpy.ops.mesh.select_all(action = 'DESELECT')
    bpy.ops.object.mode_set(mode='OBJECT')
    for p in face_build:
        me.vertices[p].select = True
    bpy.ops.object.mode_set(mode='EDIT') 
    bpy.ops.mesh.select_mode(type='VERT')
    bpy.ops.mesh.remove_doubles()


class LayoutMatExtPanel(bpy.types.Panel):
    bl_label = "Auto Extrude"
    bl_idname = "MatExtrude_Operator"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    bl_context = "mesh_edit"
    bl_options = {'DEFAULT_CLOSED'}  
    
    @classmethod
    def poll(cls, context):
        return context.active_object is not None and context.mode == 'EDIT_MESH'

    def draw(self, context):
        layout = self.layout
        col = layout.column(align=True)
        row = col.row(align=True) 
        row.operator("mesh.get_mat4extrude", text='Get Mats')
        row = col.row(align=True) 
        row.operator("mesh.mat_extrude", text='Template Extrude')
        



class MatExrudeOperator(bpy.types.Operator):
    """Extude with mats"""
    bl_idname = "mesh.mat_extrude"
    bl_label = "Mat Extrude"
    bl_options = {'REGISTER', 'UNDO'} 

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        main(context)
        return {'FINISHED'}    


class GetMatsOperator(bpy.types.Operator):
    """Get mats"""
    bl_idname = "mesh.get_mat4extrude"
    bl_label = "Get Mats for extrude"
    bl_options = {'REGISTER', 'UNDO'} 

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        getMats(context)
        return {'FINISHED'}    
        

classes = [LayoutMatExtPanel, MatExrudeOperator, GetMatsOperator]


def register():
    for c in classes:
        bpy.utils.register_class(c) 


def unregister():
    for c in reversed(classes):  
        bpy.utils.unregister_class(c) 

if __name__ == "__main__":
    register()       