import bpy
from bpy_extras.io_utils import ExportHelper
from bpy.props import StringProperty, BoolProperty, EnumProperty
from bpy.types import Operator
from copy import copy

bl_info = {
    "name": "PolyCams Render",
    "author": "Alexander Nedovizin",
    "version": (0, 3, 0),
    "blender": (2, 6, 7),
    "category": "Render"
}  


class ExportSomeData(Operator, ExportHelper):
    """This appears in the tooltip of the operator and in the generated docs"""
    bl_idname = "export_test.some_data"  # important since its how bpy.ops.import_test.some_data is constructed
    bl_label = "Export Some Data"

    # ExportHelper mixin class uses this
    filename_ext = ""

    def execute(self, context):
        return render_me(self.filepath)
    

def render_me(filepath):
    sceneName = bpy.context.scene.name     
    scene = bpy.data.scenes[sceneName]
    marks = scene.timeline_markers
    
    lm=[[m.frame, i] for i,m in enumerate(marks)]
    lm.sort()
    diap = []
    print('lm',lm)
    
    for idx, l_mark in enumerate(lm[:-1]):
        mark = marks[l_mark[1]]
        if mark.name == "end":
            continue
        
        start_fr = mark.frame
        if (len(marks)-1)>idx:
            end_fr = marks[lm[idx+1][1]].frame
        else:
            end_fr = copy(scene.frame_end)
        
        name_fr = mark.name    
        diap.append((start_fr, end_fr, name_fr))
        
    if len(diap)==0:
        diap.append((scene.frame_start, scene.frame_end, ''))
    
    for d in diap:
        scene.frame_start = d[0]
        scene.frame_end = d[1]
        for cam in bpy.data.objects: 
            if ( cam.type =='CAMERA' and not cam.hide_render): 
                bpy.data.scenes[sceneName].camera = cam 
                if d[2]!='':
                    bpy.data.scenes[sceneName].render.filepath = filepath+'\\'+d[2]+'\\'+cam.name+'\\'+d[2] 
                else:
                    bpy.data.scenes[sceneName].render.filepath = filepath+'\\'+cam.name+'\\'+cam.name
                bpy.ops.render.render(animation=True) 
            
    print('Done!') 
    #print(bpy.data.scenes[sceneName].render.filepath)
    return {'FINISHED'}
    
                                         
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
    bpy.ops.scene.render_me()