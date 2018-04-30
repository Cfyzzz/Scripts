import bpy
from bpy_extras.io_utils import ExportHelper
from bpy.props import StringProperty, BoolProperty, EnumProperty
from bpy.types import Operator
from threading import Timer

bl_info = {
    "name": "PolyCams Render",
    "author": "Alexander Nedovizin, Sergey Krumas",
    "version": (0, 1, 1),
    "blender": (2, 6, 7),
    "category": "Render"
}  

file_path = ""   #for correct working

def start_process():
    render_me(file_path)    # do not insert it in the Timer!
    
def set_timer():      
    Timer(3, start_process).start() #waiting for 3 seconds
    for area in bpy.context.screen.areas:
        if area.type == 'VIEW_3D':
            area.type = 'IMAGE_EDITOR'
    print('Start rendering...')            


class ExportSomeData(Operator, ExportHelper):
    """This appears in the tooltip of the operator and in the generated docs""" 
    # important since its how bpy.ops.import_test.some_data is constructed
    bl_idname = "export_test.some_data"  
    bl_label = "Render!"

    # ExportHelper mixin class uses this
    filename_ext = ""
    
    
    def execute(self, context):
        file_path = self.filepath
        set_timer()
        return {'FINISHED'} #close the file selector 
    

def render_me(filepath):
    sceneName = bpy.context.scene.name    

    for cam in bpy.data.objects: 
        if ( cam.type =='CAMERA' and not cam.hide_render): 
            bpy.data.scenes[sceneName].camera = cam 
            bpy.data.scenes[sceneName].render.filepath = filepath+'\\'+cam.name+'\\cadr_' 
            bpy.ops.render.render(animation=True) 
            
    print('Done!') 
    print(bpy.data.scenes[sceneName].render.filepath)
    
                                         
class RenderMe(bpy.types.Operator):
   """Cams render"""
   bl_idname = "scene.render_me"
   bl_label = "Render Me"
   bl_options = {'REGISTER', 'UNDO'}

   def execute(self, context):
        bpy.ops.export_test.some_data('INVOKE_DEFAULT')
        return {'FINISHED'}

       
def menu_func(self, context):
    self.layout.operator(RenderMe.bl_idname)
def menu_func_export(self, context):
    self.layout.operator(ExportSomeData.bl_idname, text="Cams Render!")


addon_keymaps = []                      

def register():
    bpy.utils.register_class(RenderMe)
    bpy.types.VIEW3D_MT_object.append(menu_func)
    
    bpy.utils.register_class(ExportSomeData)
    bpy.types.INFO_MT_file_export.append(menu_func_export)

    # handle the keymap
    wm = bpy.context.window_manager
    km = wm.keyconfigs.addon.keymaps.new(name='Object Mode', space_type='EMPTY')
    kmi = km.keymap_items.new(RenderMe.bl_idname, 'F12', 'PRESS', ctrl=True, shift=False)
    addon_keymaps.append((km, kmi))

def unregister():
    bpy.utils.unregister_class(RenderMe)
    bpy.types.VIEW3D_MT_object.remove(menu_func)
    
    bpy.utils.unregister_class(ExportSomeData)
    bpy.types.INFO_MT_file_export.remove(menu_func_export)

    # handle the keymap
    for km, kmi in addon_keymaps:
        km.keymap_items.remove(kmi)
    addon_keymaps.clear()


if __name__ == "__main__":
    register() 
    