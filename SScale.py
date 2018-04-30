# -*- coding: utf-8 -*-   

# Author: Nedovizin Alexander, 19.09.2013


bl_info = {
    "name": "SScale",                     
    "author": "Alexander Nedovizin",
    "version": (0, 1, 0),
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


def main(context):
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
    bl_label = "SScale operator"
    bl_idname = "SScale_Operator"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    bl_context = "mesh_edit"
    bl_options = {'DEFAULT_CLOSED'}  
    
    @classmethod
    def poll(cls, context):
        return context.active_object is not None and context.mode == 'EDIT_MESH'

    def draw(self, context):
        layout = self.layout
        layout.operator("mesh.simple_scale_operator", text='Схлопнуть!')
 

class SSOperator(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "mesh.simple_scale_operator"
    bl_label = "SScale operator"
    bl_options = {'REGISTER', 'UNDO'} 

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        main(context)
        return {'FINISHED'}


def register():
    bpy.utils.register_class(SSOperator)
    bpy.utils.register_class(LayoutSSPanel)

def unregister():
    bpy.utils.unregister_class(SSOperator)
    bpy.utils.unregister_class(LayoutSSPanel)
    

if __name__ == "__main__":
    register()
