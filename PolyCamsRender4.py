# -*- coding: utf-8 -*-    

import bpy, math
import os
import time     
from bpy_extras.io_utils import ExportHelper
from bpy.props import StringProperty, BoolProperty, EnumProperty
from bpy.types import Operator

bl_info = {
    "name": "PolyCams Render",
    "author": "Alexander Nedovizin",
    "version": (0, 4, 9),
    "blender": (2, 6, 9),
    "category": "Render"
}  

# http://dl.dropboxusercontent.com/u/59609328/Blender-Rus/PolyCamsRender4.py

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
    glob_res = [bpy.context.scene.render.resolution_x, bpy.context.scene.render.resolution_y] 
    
    bpy.data.scenes[sceneName].render.filepath = filepath
    if not os.path.exists(filepath):
        os.mkdir(filepath)
    outputfile_s = os.path.join(filepath, 'stat.txt')
    with open(outputfile_s, 'w') as w_file:
        w_file.write('Batch stats:\n'+'_________________________________\n')
    
    
    camsi = []
    progress = 0
    sline = ''
    backet_x = bpy.context.scene.render.tile_x
    backet_y = bpy.context.scene.render.tile_y
    sq_backet = backet_x*backet_y
    rp = bpy.context.scene.render.resolution_percentage
    for cam in bpy.data.objects: 
        if ( cam.type =='CAMERA' and not cam.hide_render): 
            flag = False
            res = cam.data.name.split('(')
            res_x = glob_res[0]
            res_y = glob_res[1]
            if len(res)==2:
                res = res[1].split(')')
                if len(res)==2:
                    res = res[0].split('+')
                    if len(res)==2:
                        res_x = int(res[0])
                        res_y = int(res[1])
                        flag = True
                        
            camsi.append((res_x,res_y))
            p_tmp = res_x * res_y
            p_tmp_scale = round(p_tmp*rp/100)
            progress += p_tmp
            if flag:
                sline = sline + cam.name +' | '+str(res_x)+'x'+str(res_y)+' | '+ \
                    str(round(res_x*rp/100))+'x'+str(round(res_y*rp/100))+' | '+ \
                    str(round(p_tmp_scale/sq_backet))+'\n'
            else:
                sline = sline + cam.name +' | default | '+ \
                    str(round(res_x*rp/100))+'x'+str(round(res_y*rp/100))+' | '+ \
                    str(round(p_tmp_scale/sq_backet))+'\n'
            
    
    with open(outputfile_s, 'a') as w_file:
        w_file.write('Total resolution = '+str(round(math.sqrt(progress)))+'x'+str(round(math.sqrt(progress)))+ \
            ' ('+str(round(math.sqrt(progress)*rp/100))+'x'+str(round(math.sqrt(progress)*rp/100))+')'+'\n')
        w_file.write('Default Resolution = '+str(glob_res[0])+'x'+str(glob_res[1])+' ('+str(rp)+'%)'+'\n')
        w_file.write('Tiles = '+str(backet_x)+'x'+ str(backet_y)+'\n')
        w_file.write('Total tiles = '+str(round(progress*rp/(sq_backet*100)))+'\n\n')
        w_file.write('Cameras:\n'+'Name | resolution | scaled ('+str(rp)+'%) | tiles\n'+ \
        '________________________________________\n')
        w_file.write(sline)
        
        
    outputfile = os.path.join(filepath, 'log.txt')
    with open(outputfile, 'w') as w_file:
        w_file.write('Cameras:\n'+'Name | resolution | scaled ('+str(rp)+'%) | progress % | remaining time | elapsed time\n'+ \
        '_____________________________________________________________________________\n')
        
    p_tmp = 0
    time_start = time.time()   
    i = 0
    for cam in bpy.data.objects: 
        if ( cam.type =='CAMERA' and not cam.hide_render): 
            bpy.data.scenes[sceneName].camera = cam 
            bpy.context.scene.render.resolution_x = camsi[i][0]
            bpy.context.scene.render.resolution_y = camsi[i][1]
            bpy.data.scenes[sceneName].render.filepath = filepath+'\\'+cam.name
            bpy.ops.render.render(animation=False, write_still = True) 
            p_tmp += camsi[i][0]*camsi[i][1]
            proc = max(round(p_tmp*100/progress),1)
            r_time = time.time() - time_start
            time_tmp = r_time*(100-proc)/proc
            time_tmp = round(time_tmp)
            
            s_rt = time.strftime('%H:%M:%S',time.gmtime(r_time))
            s_lt = time.strftime('%H:%M:%S',time.gmtime(time_tmp))
            with open(outputfile, 'a') as w_file:
                w_file.write(cam.name +' | '+str(camsi[i][0])+'x'+str(camsi[i][1])+' | '+ \
                    str(round(camsi[i][0]*rp/100))+'x'+str(round(camsi[i][1]*rp/100))+' | '+ \
                    str(proc)+' | '+s_lt+' | '+s_rt+'\n')
            i += 1
    
    bpy.context.scene.render.resolution_x = glob_res[0]
    bpy.context.scene.render.resolution_y = glob_res[1]
    #print('Done!') 
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
    kmi = km.keymap_items.new(RenderMe.bl_idname, 'F12', 'PRESS', alt=True, shift=False)
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