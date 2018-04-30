# -*- coding: utf-8 -*-

bl_info = {  
 "name": "Doorway",  
 "author": "Nedovizin Alexandr",  
 "version": (1, 3, 4),  
 "blender": (2, 6, 8),  
 "location": "View3D > Tools > Doorway",  
 "description": "Create doorway between the two parallel planes",  
 "warning": "",  
 "wiki_url": "",  
 "tracker_url": "",  
 "category": "Mesh"}  
                         

import bpy, bmesh
from copy import copy
from bpy.props import StringProperty
import mathutils





'''
refs:
http://www.blender.org/documentation/blender_python_api_2_68_release/mathutils.geometry.html
http://www.blender.org/documentation/blender_python_api_2_68_release/bmesh.ops.html#module-bmesh.ops
http://www.mathprofi.ru/uravnenie_pryamoi_na_ploskosti.html
'''


def verts_on_planes(verts, pols):
    '''
    IN - [verts], [polygons]
    OUT - [{polygon index:[verts index]}]
    '''
    
    result = []
    for i,p in enumerate(pols):
        cnt = p.center
        vc = mathutils.Vector((cnt))
        N = pols[i].normal
        vs_idx = []
        
        for j,v in enumerate(verts):
            k = N*(vc-v.co)
            if (abs(k) < 0.01):
                vs_idx.append(j)
        if len(vs_idx)>0:
            result.append({i:vs_idx})
    return result
        
        
def equation_plane(point, normal_dest):
    #получаем коэффициенты уравнения плоскости по точке и нормали
    normal = normal_dest.normalized()
    A = normal.x
    B = normal.y
    C = normal.z
    D = (A*point.x+B*point.y+C*point.z)*-1
    return (A,B,C,D)


def update_lt(self, context):
    if self.drew_it:
        bpy.ops.doorway.doorway()
        bpy.ops.object.mode_set(mode='OBJECT')
    

    
def main_draw(context):
    lt = bpy.context.window_manager.doorway_manager
    #взять нормаль полскости
    ##принадлежит ли точка плоскости
    obj = bpy.context.active_object
    pols = obj.data.polygons
    verts = obj.data.vertices
    
    bpy.ops.object.mode_set(mode='OBJECT')
    
    mods_bool = []
    for mod in obj.modifiers:
        if mod.type == "BOOLEAN":
            mods_bool.append(mod.name)
    len_bm = len(mods_bool)
    
    bpy.ops.object.mode_set(mode='EDIT')
    bpy.ops.mesh.select_mode(type='FACE')
    obj.data.update()

    #**************************
    if len_bm<=lt.mods_bool_count:
        act_face = []
        bm = bmesh.from_edit_mesh(obj.data)
        for elem in bm.select_history:
                if isinstance(elem, bmesh.types.BMFace):
                    act_face.append(pols[elem.index])   
                                          
        R = {}    
        quad = ()
        gp = bpy.context.object.grease_pencil
        for idx, stroke in enumerate(gp.layers.active.active_frame.strokes):
                stroke = gp.layers.active.active_frame.strokes[-1]
                gverts = stroke.points
                R = verts_on_planes(gverts, pols)  
               
                if len(R)==0:
                    #показать предупреждение 
                    print_error('Нет карандаша на активном объекте!')
                    bpy.ops.object.mode_set(mode='OBJECT')
                    #print('Error: 02')
                    return False
                
                #теперь надо получить результирующий вектор
                idx_face_0 = list(R[0].keys())[0]
                if len(R)>0:
                    v1 = R[0][idx_face_0][0] 
                    v2 = R[0][idx_face_0][-1] 
                    
                    vec_diag = gverts[v2].co-gverts[v1].co
                    quad = (gverts[v1].co, gverts[v2].co, pols[idx_face_0].index)
        bm.free     
        
        if len(quad)==0:
            print_error('Нет карандаша на активном объекте!')
            bpy.ops.object.mode_set(mode='OBJECT')
            #print('Error: 03')
            return False
        
        #надо получить противопложную плоскость
        pol = pols[quad[2]]
        pol_normal = copy(pol.normal)
        vec_back = pol_normal * -1
        
        point_mid_1 = (quad[0] + quad[1])/2
        ep = equation_plane(verts[pol.vertices[0]].co, pol_normal)
        
        p_idx = -1
        dist = -1
        
        if pol_normal.length<1e-6:
            doorway_managerProps.mods_bool_count = 100
            print_error('Нарисуйте линию и повторите попытку.')
            print('Error: 01')
            return False
            
        for i,p in enumerate(pols):
            if i == quad[2]: continue
            
            if not lt.check_parallel or (vec_back - p.normal).length<1e-6:
                vs0 = verts[p.vertices[0]].co
                #получаем расстояние между плоскостями
                disttmp = abs(vs0.x*ep[0] + vs0.y*ep[1] + vs0.z*ep[2] + ep[3])/pol_normal.length
                #найти точку пересечения с этой плоскостью
                vec_back.normalize()
                point_mid_2 = point_mid_1 + vec_back*disttmp
                #определяем эта точка находится внутри полигона или нет. 
                cnt2 = mathutils.Vector(p.center)
                sum_cnt2 = 0
                sum_pm2 = 0
                for j,v_idx in enumerate(p.vertices):
                    v1 = verts[v_idx].co
                    l_pm2 = (v1-point_mid_2).length
                    l_cnt2 = (v1 - cnt2).length
                    
                    sum_pm2 += l_pm2
                    sum_cnt2 += l_cnt2
                
                if abs(sum_pm2-sum_cnt2)>2:
                    #вектор НЕ попадает в полигон2
                    continue
                
                if dist>disttmp or dist<0:
                    p_idx = i
                    dist = disttmp

        if p_idx<0: 
            #Сообщить, что искали,но не нашли
            print_error('Нет подходящего противоположного полигона.')
            bpy.ops.object.mode_set(mode='OBJECT')
            print('Error: 04')
            return False

    #плоскость найдена
    #dist - расстояние
    #p_idx - индекс плоскости2
    #ep - уровнение плоскости1
    #vec_diag - вектор-диагональ
    #pol_normal
    
    bpy.ops.object.mode_set(mode='OBJECT')
    
    if len_bm<=lt.mods_bool_count:
        #Первый раз рисуем куб
        bpy.ops.mesh.primitive_cube_add(location=(0.0,0.0,0.0))
        cube = bpy.context.active_object
            
        #удалить грани нормали которых параллельны оси y
        bpy.ops.object.mode_set(mode='EDIT')
        pols_cube = cube.data.polygons
        verts_cube = cube.data.vertices
        napr = mathutils.Vector((0.0,1.0,0.0))
        bpy.ops.mesh.select_all(action='DESELECT')
        bpy.ops.object.mode_set(mode='OBJECT')
    
        for i,p in enumerate(pols_cube):
            nm_p_cube = p.normal
            mul = napr * nm_p_cube
            if mul!=0.0:
                #векторы параллельны, т.к не перпендикулярны (в кубе третьего не дано)
                p.select = True
    
        bpy.ops.object.mode_set(mode='EDIT')
        bpy.ops.mesh.delete(type='FACE')
    
        #отмасштабировать и развернуть
        bpy.ops.mesh.select_all(action='SELECT')
        bpy.ops.object.mode_set(mode='OBJECT')
        
        #получить длину и ширину проёма
        aa = mathutils.Vector((0.0,1.0,0.0)) 
        bb = pol_normal
        vec = aa
        q_rot = vec.rotation_difference(bb).to_matrix().to_4x4()
        vec_scale_cube = vec_diag*q_rot
        vec_scale_cube.y = dist+0.5
        vec_scale_cube.x = abs(vec_scale_cube.x)
        vec_scale_cube.z = abs(vec_scale_cube.z)
    
        bm = bmesh.new()
        bm.from_mesh(cube.data)

        if lt.size_width!=0.0:
            vec_scale_cube.x = abs(lt.size_width)*vec_scale_cube.x /abs(vec_scale_cube.x )
            
        if lt.size_height!=0.0:
            vec_scale_cube.z = abs(lt.size_height)*vec_scale_cube.z/abs(vec_scale_cube.z)    
        
        vec_scale_cube /= 2
        bmesh.ops.scale(bm, vec=vec_scale_cube, verts=bm.verts)
        
        bm.to_mesh(cube.data)
        bm.free
        
        #развернуть куб в плоскость Плоскость1
        aa = mathutils.Vector((0.0,1.0,0.0)) 
        bb = pol_normal
        vec = aa
        q_rot = vec.rotation_difference(bb).to_matrix().to_4x4()
        cube.matrix_local *= q_rot
        
        #выставить в проём
        vec_delta_trans = mathutils.Vector((lt.delta_width, 0, lt.delta_height))
        mat_delta_trans = mathutils.Matrix.Translation(vec_delta_trans)
        
        tmpvec_proem = point_mid_1+vec_back*(dist-0.2)/2
        bpy.ops.transform.translate(value = tmpvec_proem)
        
        list_mat = list(cube.matrix_local)
        list_al_arr = list(map(lambda x:list(x),list_mat))

        mat_value = bpy.context.window_manager.doorway_matrix
        if len(mat_value)==0:
            for i in range(16):
                mat_value = bpy.context.window_manager.doorway_matrix.add()
                mat_value.value = 0.0
            mat_value = bpy.context.window_manager.doorway_matrix
        
        for ii,mv in enumerate(list_al_arr):
            for jj,mv_el in enumerate(mv):
                mat_value[ii*4+jj].value = mv_el
        
        mat_current = copy(cube.matrix_local)
        cube.matrix_local *= mat_delta_trans
        
        lt.matrix_x0 = mat_current[0][3]
        lt.matrix_y0 = mat_current[2][3]
        
        bpy.ops.object.mode_set(mode='EDIT')
        bpy.ops.object.mode_set(mode='OBJECT')
    else:
        #куб уже нарисован
        cube = bpy.context.scene.objects[lt.cube_str_name]
        
        mat_value = bpy.context.window_manager.doorway_matrix
        mat_v = mathutils.Matrix()
        mat_v[0] = mathutils.Vector((mat_value[0].value,mat_value[1].value,mat_value[2].value,mat_value[3].value))
        mat_v[1] = mathutils.Vector((mat_value[4].value,mat_value[5].value,mat_value[6].value,mat_value[7].value))
        mat_v[2] = mathutils.Vector((mat_value[8].value,mat_value[9].value,mat_value[10].value,mat_value[11].value))
        mat_v[3] = mathutils.Vector((mat_value[12].value,mat_value[13].value,mat_value[14].value,mat_value[15].value))
        
        cube.matrix_local = mat_v
        
        vec_delta_trans = mathutils.Vector((lt.delta_width, 0, lt.delta_height))
        mat_delta_trans = mathutils.Matrix.Translation(vec_delta_trans)
        
        mat_current = copy(cube.matrix_local)
        cube.matrix_local *= mat_delta_trans
        
        lt.matrix_x0 = mat_current[0][3]
        lt.matrix_y0 = mat_current[2][3]
        
        bpy.ops.object.mode_set(mode='EDIT')
        bpy.ops.object.mode_set(mode='OBJECT')
        
        
        
    if len_bm<=lt.mods_bool_count:
        doorway_managerProps.mods_bool_count = len_bm
        #вырезаем проем
        bpy.ops.object.select_all(action='DESELECT')
        bpy.context.scene.objects.active = obj
        bpy.ops.object.select_pattern(pattern=obj.name, case_sensitive=False, extend=False)
        bpy.ops.object.modifier_add(type='BOOLEAN')
        for mod in reversed(obj.modifiers):
            if mod.type == "BOOLEAN" and mod.name not in mods_bool:
                bool_name = mod.name
                break
    
        bpy.context.object.modifiers[bool_name].operation = 'DIFFERENCE'
        bpy.context.object.modifiers[bool_name].object = cube
        gp.layers.active.active_frame.strokes.remove(gp.layers.active.active_frame.strokes[-1])

    else:
        mod = obj.modifiers[-1]
        mod.object = cube
        bool_name = mod.name

    bpy.ops.object.select_all(action='DESELECT')           
    bpy.context.scene.objects.active = cube
    bpy.ops.object.select_pattern(pattern=cube.name, case_sensitive=False, extend=False)
    bpy.ops.object.hide_view_set()

    bpy.context.scene.objects.active = obj
    bpy.ops.object.select_pattern(pattern=obj.name, case_sensitive=False, extend=False)
    bpy.ops.object.mode_set(mode='EDIT')
    bpy.ops.mesh.select_all(action='DESELECT')  
    bpy.ops.object.mode_set(mode='OBJECT')

    doorway_managerProps.cube_str_name = cube.name
    doorway_managerProps.obj_str_name = obj.name
    doorway_managerProps.drew_it = True



class CreateDoorway(bpy.types.Operator):
    bl_idname = "doorway.doorway"
    bl_label = "Doorway"
    bl_options = {'UNDO'}  
    
    @classmethod
    def poll(cls, context):
        obj = context.active_object  
        return obj is not None and obj.type == 'MESH'
    
    def execute(self, context):
        main_draw(context)
        return {'FINISHED'} 





class ApplyDoorway(bpy.types.Operator):
    bl_idname = "doorway.apply"
    bl_label = "Doorway apply"
    bl_options = {'UNDO'}  

    def execute(self, context):
        lt = bpy.context.window_manager.doorway_manager
        cube_name = lt.cube_str_name
        if cube_name in bpy.context.scene.objects:
            cube = bpy.context.scene.objects[cube_name]
            obj = bpy.context.scene.objects[lt.obj_str_name]
            
            bpy.ops.object.mode_set(mode='OBJECT')
            bpy.context.scene.objects.active = obj
            bpy.ops.object.select_pattern(pattern=obj.name, case_sensitive=False, extend=False)
            bpy.ops.object.modifier_apply(apply_as="DATA", modifier=obj.modifiers[-1].name)
            
            bpy.ops.object.hide_view_clear()
            bpy.context.scene.objects.active = cube
            bpy.ops.object.select_pattern(pattern=cube.name, case_sensitive=False, extend=False)
            bpy.ops.object.delete()
    
            bpy.context.scene.objects.active = obj
            bpy.ops.object.select_pattern(pattern=obj.name, case_sensitive=False, extend=False)
        
        doorway_managerProps.mods_bool_count = 100
        doorway_managerProps.drew_it = False
        lt.delta_width = 0.0
        lt.delta_height = 0.0
    
        return {'FINISHED'} 






class DoorwayToolPanel(bpy.types.Panel):
    """Creates a Panel in the Object properties window"""
    bl_label = "Doorway"
    bl_idname = "OBJECT_PT_doorway"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    bl_options = {'DEFAULT_CLOSED'} 

    @classmethod
    def poll(cls, context):
        obj = context.active_object  
        return obj is not None and obj.type == 'MESH'

    def draw(self, context):                    
        layout = self.layout
        col = layout.column(align=True)
        lt = bpy.context.window_manager.doorway_manager
        
        split = col.split(percentage=0.15)
        if lt.display_dw:
            split.prop(lt, "display_dw", text="", icon='DOWNARROW_HLT')
        else:
            split.prop(lt, "display_dw", text="", icon='RIGHTARROW')
            
        if lt.mods_bool_count>90:
            split.operator("doorway.doorway", text = 'Create doorway')
            
        if lt.display_dw:
            box = col.column(align=True).box().column()
            col_top = box.column(align=True)
            row = col_top.row(align=True)
            if lt.mods_bool_count>90:
                row.label('Size:', icon = 'FULLSCREEN_ENTER')
                row = col_top.row(align=True)
                row.prop(lt, 'size_width', text = 'Width')
                row = col_top.row(align=True)
                row.prop(lt, 'size_height', text = 'Height')
                row = col_top.row(align=True)
                row.prop(lt, 'check_parallel', text = 'Only parallel planes')
            
            if lt.mods_bool_count<90:
                row.label('Position:', icon = 'MANIPUL')
                row = col_top.row(align=True)
                row.prop(lt, 'delta_width', text = 'Width offset')
                row = col_top.row(align=True)
                row.prop(lt, 'delta_height', text = 'Hieght offset')
                row = col_top.row(align=True)
            
        if lt.mods_bool_count<90:
            split.operator("doorway.apply", text = 'Apply')
        

        
class doorway_managerProps(bpy.types.PropertyGroup):
    """
    Fake module like class
    bpy.context.window_manager.doorway_manager
    """
    size_width = bpy.props.FloatProperty(name = 'size_width')
    size_height = bpy.props.FloatProperty(name = 'size_height')
    delta_width = bpy.props.FloatProperty(name = 'delta_width', update=update_lt)
    delta_height = bpy.props.FloatProperty(name = 'delta_height', update=update_lt)
    
    pol_idx = bpy.props.IntProperty(name = 'pol_idx', default = -1)
    drew_it = bpy.props.BoolProperty(name = 'drew_it', default = False)
    check_parallel = bpy.props.BoolProperty(name = 'check_parallel', default = True)
    
    mods_bool_count = bpy.props.IntProperty(name = 'mods_bool_count', default = 100)
    cube_str_name = bpy.props.StringProperty(name = 'cube_str_name', default = 'Cube')
    obj_str_name = bpy.props.StringProperty(name = 'obj_str_name', default = 'Object')
    matrix_x0 = bpy.props.FloatProperty(name = 'matrix_x0')
    matrix_y0 = bpy.props.FloatProperty(name = 'matrix_y0')
    
    proem_trans = bpy.props.FloatProperty(name = 'proem_trans')
    
    display_dw = bpy.props.BoolProperty(name = "Doorway settings",
        description = "Display settings of the Doorway tool",
        default = False)
        
        
        
        
class MatrixSettingItem(bpy.types.PropertyGroup):
    value = bpy.props.FloatProperty(name="value", default=0.0)
    
    
    



class MessageOperator(bpy.types.Operator):
    bl_idname = "error.message"
    bl_label = "Message"
    type = StringProperty()
    message = StringProperty()
 
    def execute(self, context):
        self.report({'INFO'}, self.message)
        print(self.message)
        return {'FINISHED'}
 
    def invoke(self, context, event):
        wm = context.window_manager
        return wm.invoke_popup(self, width=400, height=200)
 
    def draw(self, context):
        self.layout.label(self.message, icon='BLENDER')


def print_error(message):
    bpy.ops.error.message('INVOKE_DEFAULT', 
        type = "Message",
        message = message)     
        
def register():
    bpy.utils.register_class(MessageOperator)


def unregister():
    bpy.utils.unregister_class(MessageOperator)  

        
                
        

# define classes for registration
classes = [CreateDoorway, DoorwayToolPanel, ApplyDoorway, \
    doorway_managerProps, MatrixSettingItem]


# registering and menu integration
def register():
    for c in classes:
        bpy.utils.register_class(c)    
    bpy.types.WindowManager.doorway_manager = \
        bpy.props.PointerProperty(type = doorway_managerProps)  
    doorway_managerProps.mods_bool_count = 100
    doorway_managerProps.drew_it = False
    doorway_managerProps.pol_idx = -1
    
    bpy.types.WindowManager.doorway_matrix = \
        bpy.props.CollectionProperty(type=MatrixSettingItem)
    
           
# unregistering and removing menus  
def unregister():    
    del bpy.types.WindowManager.doorway_matrix
    del bpy.types.WindowManager.doorway_manager
    for c in reversed(classes):  
        bpy.utils.unregister_class(c)
                                        
if __name__ == "__main__":
    register()