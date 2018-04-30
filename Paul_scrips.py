# -*- coding: utf-8 -*-   

bl_info = {
    "name": "Paul scripts",                     
    "author": "Alexander Nedovizin",
    "version": (0, 1, 1),
    "blender": (2, 6, 8),
    "location": "View3D > Toolbar",
    "category": "Mesh"
}  


import bpy



def find_index_of_selected_vertex(mesh):  
    selected_verts = [i.index for i in mesh.vertices if i.select]  
    verts_selected = len(selected_verts)  
    if verts_selected <1:  
        return None                            
    else:  
        return selected_verts  


def find_extreme_select_verts(mesh, verts_idx):
    res_vs = []
    edges = mesh.edges  
 
    for v_idx in verts_idx:
        connecting_edges = [i for i in edges if v_idx in i.vertices[:] and i.select]  
        if len(connecting_edges) == 1: 
            res_vs.append(v_idx)
    return res_vs
    

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


def main_spread(context, mode):
    bpy.ops.object.mode_set(mode='OBJECT') 
    bpy.ops.object.mode_set(mode='EDIT') 
    
    obj = bpy.context.active_object
    me = obj.data

    verts = find_index_of_selected_vertex(me)
    cou_vs = len(verts) - 1
    if verts != None and cou_vs>0:
        extreme_vs = find_extreme_select_verts(me, verts)
        
        if len(extreme_vs) != 2:
            print_error('Надо задавать один луп!')
            print('Error: 01')
            return False
  
        if mode[0]:
            min_v = min([me.vertices[extreme_vs[0]].co.x,extreme_vs[0]], \
                        [me.vertices[extreme_vs[1]].co.x,extreme_vs[1]])
            max_v = max([me.vertices[extreme_vs[0]].co.x,extreme_vs[0]], \
                        [me.vertices[extreme_vs[1]].co.x,extreme_vs[1]])

            if (max_v[0]-min_v[0]) == 0:
                min_v = [me.vertices[extreme_vs[0]].co.x,extreme_vs[0]]
                max_v = [me.vertices[extreme_vs[1]].co.x,extreme_vs[1]]
            
            sort_list = find_all_connected_verts(me,min_v[1],[])
            
            if len(sort_list) != len(verts):
                print_error('Разоравнный луп!')
                print('Error: 020')
                return False
            
            step = []
            if mode[3]:
                list_length = []
                sum_length = 0.0
                x_sum = 0.0
                for sl in range(cou_vs):
                    subb = me.vertices[sort_list[sl+1]].co-me.vertices[sort_list[sl]].co
                    length = subb.length
                    sum_length += length
                    list_length.append(sum_length)
                    x_sum += subb.x
                
                for sl in range(cou_vs):
                    step.append(x_sum * list_length[sl]/sum_length)
            else:
                diap = (max_v[0]-min_v[0])/cou_vs
                for sl in range(cou_vs):
                    step.append((sl+1)*diap)
            
            bpy.ops.object.mode_set(mode='OBJECT') 
            for idx in range(cou_vs):
                me.vertices[sort_list[idx+1]].co.x = me.vertices[sort_list[0]].co.x  + step[idx]

            bpy.ops.object.mode_set(mode='EDIT')  
            
        if mode[1]:
            min_v = min([me.vertices[extreme_vs[0]].co.y,extreme_vs[0]], \
                        [me.vertices[extreme_vs[1]].co.y,extreme_vs[1]])
            max_v = max([me.vertices[extreme_vs[0]].co.y,extreme_vs[0]], \
                        [me.vertices[extreme_vs[1]].co.y,extreme_vs[1]])

            if (max_v[0]-min_v[0]) == 0:
                min_v = [me.vertices[extreme_vs[0]].co.y,extreme_vs[0]]
                max_v = [me.vertices[extreme_vs[1]].co.y,extreme_vs[1]]
            
            sort_list = find_all_connected_verts(me,min_v[1],[])
            if len(sort_list) != len(verts):
                print_error('Разоравнный луп!')
                print('Error: 021')
                return False

            step = []
            if mode[3]:
                list_length = []
                sum_length = 0.0
                y_sum = 0.0
                for sl in range(cou_vs):
                    subb = me.vertices[sort_list[sl+1]].co-me.vertices[sort_list[sl]].co
                    length = subb.length
                    sum_length += length
                    list_length.append(sum_length)
                    y_sum += subb.y
                
                for sl in range(cou_vs):
                    step.append(y_sum * list_length[sl]/sum_length)
            else:
                diap = (max_v[0]-min_v[0])/cou_vs
                for sl in range(cou_vs):
                    step.append((sl+1)*diap)

            bpy.ops.object.mode_set(mode='OBJECT') 
            for idx in range(cou_vs):
                me.vertices[sort_list[idx+1]].co.y = me.vertices[sort_list[0]].co.y  + step[idx]

            bpy.ops.object.mode_set(mode='EDIT')  
            
        if mode[2]:
            min_v = min([me.vertices[extreme_vs[0]].co.z,extreme_vs[0]], \
                        [me.vertices[extreme_vs[1]].co.z,extreme_vs[1]])
            max_v = max([me.vertices[extreme_vs[0]].co.z,extreme_vs[0]], \
                        [me.vertices[extreme_vs[1]].co.z,extreme_vs[1]])

            if (max_v[0]-min_v[0]) == 0:
                min_v = [me.vertices[extreme_vs[0]].co.z,extreme_vs[0]]
                max_v = [me.vertices[extreme_vs[1]].co.z,extreme_vs[1]]
            
            sort_list = find_all_connected_verts(me,min_v[1],[])
            if len(sort_list) != len(verts):
                print_error('Разоравнный луп!')
                print('Error: 022')
                return False
            
            step = []
            if mode[3]:
                list_length = []
                sum_length = 0.0
                z_sum = 0.0
                for sl in range(cou_vs):
                    subb = me.vertices[sort_list[sl+1]].co-me.vertices[sort_list[sl]].co
                    length = subb.length
                    sum_length += length
                    list_length.append(sum_length)
                    z_sum += subb.z
                
                for sl in range(cou_vs):
                    step.append(z_sum * list_length[sl]/sum_length)
            else:
                diap = (max_v[0]-min_v[0])/cou_vs
                for sl in range(cou_vs):
                    step.append((sl+1)*diap)
            
            bpy.ops.object.mode_set(mode='OBJECT') 
            for idx in range(cou_vs):
                me.vertices[sort_list[idx+1]].co.z = me.vertices[sort_list[0]].co.z  + step[idx]

            bpy.ops.object.mode_set(mode='EDIT')  
            
    return True


def main_ss(context):
    obj = bpy.context.active_object
    me = obj.data
    
    bpy.ops.object.mode_set(mode='OBJECT') 
    bpy.ops.object.mode_set(mode='EDIT') 
    
    vs_idx = find_index_of_selected_vertex(me)
    if vs_idx:
        x_coos = [v.co.x for v in me.vertices if v.index in vs_idx]
        y_coos = [v.co.y for v in me.vertices if v.index in vs_idx]
        
        min_x = min(x_coos)
        max_x = max(x_coos)
        
        min_y = min(y_coos)
        max_y = max(y_coos)
        
        len_x = max_x-min_x
        len_y = max_y-min_y
        
        if len_y<len_x:
            bpy.ops.transform.resize(value=(1,0,1), constraint_axis=(False,True,False))
        else:
            bpy.ops.transform.resize(value=(0,1,1), constraint_axis=(True,False,False))


class LayoutSSPanel(bpy.types.Panel):
    bl_label = "Paul scripts"
    bl_idname = "Paul_Operator"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    bl_context = "mesh_edit"
    bl_options = {'DEFAULT_CLOSED'}  
    
    @classmethod
    def poll(cls, context):
        return context.active_object is not None and context.mode == 'EDIT_MESH'

    def draw(self, context):
        lt = bpy.context.window_manager.paul_manager
        
        layout = self.layout
        col = layout.column(align=True)
        col.operator("mesh.simple_scale_operator", text='Схлопнуть')
        
        split = col.split(percentage=0.15)
        if lt.display:
            split.prop(lt, "display", text="", icon='DOWNARROW_HLT')
        else:
            split.prop(lt, "display", text="", icon='RIGHTARROW')

        spread_op = split.operator("mesh.spread_operator", text = 'Распределить')
        spread_op.spread_x = lt.spread_x
        spread_op.spread_y = lt.spread_y
        spread_op.spread_z = lt.spread_z
        spread_op.relation = lt.relation
            
        if lt.display:
            box = col.column(align=True).box().column()
            col_top = box.column(align=True)
            row = col_top.row(align=True)
            row.prop(lt, 'spread_x', text = 'Spread X')
            row = col_top.row(align=True)
            row.prop(lt, 'spread_y', text = 'Spread Y')
            row = col_top.row(align=True)
            row.prop(lt, 'spread_z', text = 'Spread Z')
            row = col_top.row(align=True)
            row = col_top.row(align=True)
            row.prop(lt, 'relation', text = 'Relation')
        
        
 

class SSOperator(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "mesh.simple_scale_operator"
    bl_label = "SScale operator"
    bl_options = {'REGISTER', 'UNDO'} 

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        main_ss(context)
        return {'FINISHED'}


class SpreadOperator(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "mesh.spread_operator"
    bl_label = "Spread operator"
    bl_options = {'REGISTER', 'UNDO'} 
    
    spread_x = bpy.props.BoolProperty(name = 'spread_x', default = False, options = {'HIDDEN'})
    spread_y = bpy.props.BoolProperty(name = 'spread_y', default = False, options = {'HIDDEN'})
    spread_z = bpy.props.BoolProperty(name = 'spread_z', default = True, options = {'HIDDEN'})
    relation = bpy.props.BoolProperty(name = 'relation', default = False)
    
    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        if main_spread(context, (self.spread_x, self.spread_y, self.spread_z, self.relation)):
            print('spread complete')
        return {'FINISHED'}


class paul_managerProps(bpy.types.PropertyGroup):
    """
    Fake module like class
    bpy.context.window_manager.paul_manager
    """
    display = bpy.props.BoolProperty(name = 'display', default = True)
    
    spread_x = bpy.props.BoolProperty(name = 'spread_x', default = False)
    spread_y = bpy.props.BoolProperty(name = 'spread_y', default = False)
    spread_z = bpy.props.BoolProperty(name = 'spread_z', default = True)
    relation = bpy.props.BoolProperty(name = 'relation', default = False)


class MessageOperator(bpy.types.Operator):
    from bpy.props import StringProperty
    
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




classes = [SSOperator, SpreadOperator, LayoutSSPanel, MessageOperator, paul_managerProps]


def register():
    for c in classes:
        bpy.utils.register_class(c)
    bpy.types.WindowManager.paul_manager = \
        bpy.props.PointerProperty(type = paul_managerProps) 
    bpy.context.window_manager.paul_manager.display = False
    bpy.context.window_manager.paul_manager.spread_x = False
    bpy.context.window_manager.paul_manager.spread_y = False
    bpy.context.window_manager.paul_manager.spread_z = True
    bpy.context.window_manager.paul_manager.relation = False
    
def unregister():
    del bpy.types.WindowManager.paul_manager
    for c in reversed(classes):  
        bpy.utils.unregister_class(c)
    

if __name__ == "__main__":
    register()