###############################################################################
##                                      DTT 1.2.1.1  (c)2013 FSL - FreeSoftLand
## Title: Бета версия GridFill Manager 1_3
##
## Date : 26.07.2013
## By   : Cfyzzz
###############################################################################

import bpy, bmesh, copy
from bpy.props import IntProperty, StringProperty

select_verts = []
active_vert = -1


bl_info = {
    "name": "GridFill Manager",                     
    "author": "Alexander Nedovizin",                   
    "version": (0, 1, 3),
    "blender": (2, 6, 8),
    "description": "GridFill Manager",
    "category": "Mesh"
}  


def check_context(obj):
    global select_verts, active_vert
    res = True
    bpy.ops.object.mode_set(mode='OBJECT') 
    bpy.ops.object.mode_set(mode='EDIT') 
    
    sv = find_index_of_selected_vertex(obj)
    for v in sv:
        if not(v in select_verts):
            res = False

    return res


def update_shape(self,context):
    global select_verts, active_vert
    
    ch_c = check_context(context.object)
        
    if not ch_c:
        main(context, context.object.myRad, mode = True)
    else:
      
        selecting_verts(context.object.data,select_verts)
        main(context, context.object.myRad, mode = True)



bpy.types.Object.myRad = IntProperty(
    name="Radius", 
    min = 0,
    default = 1,
    update = update_shape)
    
bpy.types.Object.mnogo_v= IntProperty(
    name="Vertices", 
    default = -1)


def bm_vert_active_get(ob):
    bm = bmesh.from_edit_mesh(ob.data)
    for elem in reversed(bm.select_history):
        if isinstance(elem, bmesh.types.BMVert):
            return elem.index
    return -2
    
    
def find_index_of_selected_vertex(obj):  
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


def get_loop(me, active_v, v_set, not_list=[], step=0):
    vlist = [active_v]
    ln = len(v_set)
    not_list.append(active_v)
    
    step +=1
    list_v_1 = find_connected_verts(me, active_v, not_list)
    
    if step==ln:     
        return vlist 
    
    if len(list_v_1)>0:
        list_v_2 = get_loop(me, list_v_1[0], v_set, not_list, step) 
        vlist += list_v_2
        
    return vlist


def get_opposite(me,vert_index, v_set):
    loop = []
    loop = get_loop(me, vert_index, v_set, [])
    
    ps = len(loop)//2
    ff = loop.index(vert_index)

    if ff>=ps:
        df = ff-ps
    else:
        df = ff+ps

    return loop[df]
    
    
    
def find_all_connected_verts(R, me, active_v, not_list=[], step=0):
    vlist = [active_v]
    not_list.append(active_v)
    step+=1
    list_v_1 = find_connected_verts(me, active_v, not_list)
    
    if step==R+2:     
        return vlist 

    for v in list_v_1:
        list_v_2 = find_all_connected_verts(R, me, v, not_list, step) 
        vlist += list_v_2
        
    return vlist
    

def selecting_verts(me, mas):
    bpy.ops.object.mode_set(mode='OBJECT') 
    
    for idx in mas:
        me.vertices[idx].select = True
    
    bpy.ops.object.mode_set(mode='EDIT') 
    
    
def deselecting_verts(me, mas):
    bpy.ops.object.mode_set(mode='OBJECT') 
    
    for idx in mas:
        me.vertices[idx].select = False
    
    bpy.ops.object.mode_set(mode='EDIT') 



def cls_mnogo(obj):
    obj.mnogo_v = -1
    bpy.ops.ed.undo()
    return
    


def main(context, Rad=1, Dist=0, mode=False):   
    global select_verts, active_vert, mnogo_v

    bpy.ops.object.mode_set(mode='OBJECT') 
    bpy.ops.object.mode_set(mode='EDIT') 

    ob = bpy.context.object
    
    if active_vert >= 0 and ob.mnogo_v>0 and mode:
        cls_mnogo(ob)
   
    ch_c = check_context(ob)

    if mode:
        av = -1
        if ch_c:
            av = active_vert
    else:
        av = bm_vert_active_get(ob)
        if ch_c:
            active_vert = -1

    if (active_vert < 0 or active_vert != av) and not mode:
        active_vert = bm_vert_active_get(ob)
        select_verts=[]
    
    if active_vert==-2 and not mode:
        print_error('Active vert is not define')
        return{'Error: 003'}
    
    if select_verts==[]:
        select_verts = find_index_of_selected_vertex(ob)

        
    sv_len = len(select_verts)

    if sv_len<8: 
        print_error('Error: need for equ or more then 8 verts')
        return{'Error: 001'}
        
    if (sv_len//8)<Rad: 
        Rad = sv_len//8
    
    if (sv_len%2)>0 and not mode:
        print_error('Error: must be an even number of vertices')
        return{'Error: 002'}
    
    mesh = ob.data
    opposit_vert = get_opposite(mesh,active_vert, select_verts)

    nl = [] 
    new_sel_v_1 = find_all_connected_verts(Rad, mesh, active_vert, nl) 
    new_sel_v_2 = find_all_connected_verts(Rad, mesh, opposit_vert, nl)
     
    bpy.ops.mesh.select_all(action='DESELECT')
    bpy.ops.object.mode_set(mode='OBJECT') 
    
    for idx in nl:
        mesh.vertices[idx].select = True
    
    bpy.ops.object.mode_set(mode='EDIT') 
    bpy.ops.mesh.fill_grid() 
    ob.mnogo_v = len(mesh.vertices)

    return {'FINISHED'}


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
        

class GFManagerOperator(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "mesh.gfmanager_operator"
    bl_label = "GridFill Manager Operator"
    bl_options = {'REGISTER', 'UNDO'} 
    rad = bpy.props.IntProperty()

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        main(context, context.object.myRad)
        return {'FINISHED'}




class GFManagerPanel(bpy.types.Panel):
    """Creates a Panel in the Object properties window"""
    bl_label = "Grid Fill Manager"
    bl_idname = "OBJECT_PT_GFManagerPanel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_context = "object"

    def draw(self, context):
        layout = self.layout

        obj = context.object

        row = layout.row()
        row.label(text="Active object is: " + obj.name)
        row = layout.row()
        row.prop(obj, "name")
        layout.prop(obj, 'myRad')

        row = layout.row()
        row.operator("mesh.gfmanager_operator", text='Ok')


def register():
    bpy.utils.register_class(GFManagerPanel)
    bpy.utils.register_class(GFManagerOperator)
    bpy.utils.register_class(MessageOperator)


def unregister():
    bpy.utils.unregister_class(GFManagerPanel)
    bpy.utils.unregister_class(GFManagerOperator)
    bpy.utils.unregister_class(MessageOperator)


if __name__ == "__main__":
    register()

