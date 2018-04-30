bl_info = {
    "name": "Dimensions Plus",
    "author": "Alexander Nedovizi",
    "version": (1, 0),
    "blender": (2, 75, 0),
    "location": "View3D > Toolbar",
    "description": "Proportional dimensions",
    "tracker_url": "https://github.com/Cfyzzz/Scripts/blob/master/DimensionsPlus.py",
    "category": "Object"}   


import bpy
from bpy.props import * 

class ElviraPanel(bpy.types.Panel):
    bl_label = "Dimensions plus"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
                                                  
    @classmethod
    def poll(cls, context):
        return context.active_object is not None and context.active_object.type=='MESH'
    
    
    def draw(self, context):
        lt = context.object.data
        layout = self.layout
        row = layout.row(align=True)
        if (lt.prop_x==-1)or(lt.prop_y==-1)or(lt.prop_z==-1):
            row.operator('elvira.copydims', text = 'Copy')
            check_prop = False
        else:
            row.operator('elvira.pastedims', text = 'Confirm')
            check_prop = True
            
        row = layout.row()
        col = row.column(align=True)
        row.enabled = check_prop
        subrow = col.row(align=True)
        subrow.prop(lt, 'prop_x', text = 'X')
        subrow = col.row(align=True)
        subrow.prop(lt, 'prop_y', text = 'Y')
        subrow = col.row(align=True)
        subrow.prop(lt, 'prop_z', text = 'Z')
        
        col = row.column(align=True)
        row = col.row(align=True)
        row.prop(lt, 'check_x', text = '', icon='LINKED')
        row = col.row(align=True)
        row.prop(lt, 'check_y', text = '', icon='LINKED')
        row = col.row(align=True)
        row.prop(lt, 'check_z', text = '', icon='LINKED')
        
        
class OBJECT_OT_copyclick(bpy.types.Operator):
    bl_idname = "elvira.copydims"
    bl_label = "Copy dimensions" 
    
    def execute(self, context): 
        lt = context.object.data
        lt.prop_x, lt.prop_y, lt.prop_z=context.object.dimensions
        return{'FINISHED'}
    
      
class OBJECT_OT_pasteclick(bpy.types.Operator):
    bl_idname = "elvira.pastedims"
    bl_label = "Paste dimensions" 
    
    def execute(self, context): 
        lt = context.object.data
        l1 = [lt.prop_x, lt.prop_y, lt.prop_z]
        l2=list(context.object.dimensions)
        l3 = [lt.check_x, lt.check_y, lt.check_z]
        
        for idx,l in enumerate(l1):
            if l!=l2[idx]:
                if l3[idx]:
                    k = l/l2[idx]
                else:
                    k = 1
                    
                context.object.dimensions = list(map\
                    (lambda x,y,z:x*k if y==True else z, l2,l3,l1))
                bpy.ops.elvira.copydims()
                break 
            
        return{'FINISHED'}        
             
def initialize():
    bpy.types.Mesh.prop_x = FloatProperty(name="prop_x", default=-1, precision=3)   
    bpy.types.Mesh.prop_y = FloatProperty(name="prop_y", default=-1, precision=3)   
    bpy.types.Mesh.prop_z = FloatProperty(name="prop_z", default=-1, precision=3)   
    bpy.types.Mesh.check_x = BoolProperty(name="check_x", default = True) 
    bpy.types.Mesh.check_y = BoolProperty(name="check_y", default = True) 
    bpy.types.Mesh.check_z = BoolProperty(name="check_z", default = True) 


classes = [ElviraPanel, OBJECT_OT_copyclick, OBJECT_OT_pasteclick]
def register():
    for c in classes:
        bpy.utils.register_class(c)  
    initialize()
    
    
def unregister():    
    del bpy.types.WindowManager.elvira_manager
    for c in reversed(classes):  
        bpy.utils.unregister_class(c)  

if __name__ == "__main__":
    register()  
    
