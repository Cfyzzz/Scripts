# -*- coding: utf-8 -*-

bl_info = {  
 "name": "For export AssettoCorsa",  
 "author": "Nedovizin Alexandr",  
 "version": (1, 1, 2),  
 "blender": (2, 7, 0),  
 "location": "View3D > Tools > For_export_AssettoCorsa",  
 "description": "Помогаем создать файл настроек материалов для AssettoCorsa",  
 "warning": "",  
 "wiki_url": "",  
 "tracker_url": "",                             
 "category": "Object"}   


from bpy_extras.io_utils import ExportHelper  
import json
import bpy
import os

# http://dl.dropboxusercontent.com/u/59609328/blender-rus/for_export_AssettoCorsa.py

def chekdir(filepath):
    if not os.path.exists(filepath):
        symb = os.path.sep
        filepath_ = filepath.rpartition(symb)[0]
        if filepath_=='':
            filepath_ = filepath
        filepath = filepath_
    return filepath


def saveMat2(materials={}, bl_addons_path_=''):
    bl_addons_path=chekdir(bl_addons_path_)
    Mat = {}
    full_line = ''
    if materials=={}:
        mats_names = []
    else:
        mats_names = [m[0] for m in materials.items()]
    
    for matik in bpy.data.materials:
        name = matik.name
        mat_valid = name in mats_names
        
        alphaTested = matik.use_transparency
        sector_texture = False
        if bpy.data.materials[name].texture_slots[0]:
            AsphaltTex = bpy.data.materials[name].texture_slots[0].name
            sector_texture = True
        
        
        if alphaTested:
            boolt = 'true'
        else:
            boolt = 'false'
            
        telo = '{"shaderName" : "ksPerPixel",' \
                +'"alphaBlendmode" : "Opaque",'\
                +'"alphaTested" : '+boolt+',' \
                +'"depthMode" : "DepthNormal",'\
                +'"properties" : {'\
                    +'"ksDiffuse" : {'\
                        +'"valueA": '+str(0.4 if not mat_valid else materials[name]['properties']['ksDiffuse']['valueA']) \
                    +'},'\
                    +'"ksAmbient" : {'\
                        +'"valueA": '+str(0.4 if not mat_valid else materials[name]['properties']['ksAmbient']['valueA']) \
                    +'},'\
                    +'"ksSpecular" : {'\
                        +'"valueA": '+str(0.1 if not mat_valid else materials[name]['properties']['ksSpecular']['valueA']) \
                    +'},'\
                    +'"ksSpecularEXP" : {'\
                        +'"valueA": '+str(10 if not mat_valid else materials[name]['properties']['ksSpecularEXP']['valueA']) \
                    +'},'\
                    +'"ksEmissive" : {'\
                        +'"valueA": '+str(0 if not mat_valid else materials[name]['properties']['ksEmissive']['valueA']) \
                    +'},'\
                    +'"ksAlphaRef" : {'\
                        +'"valueA": '+str(0 if not mat_valid else materials[name]['properties']['ksAlphaRef']['valueA']) \
                        +'}}'
        
        if sector_texture:
            texture = ',"textures" : {"txDiffuse" : {'\
                            +'"slot" : 0,'\
                            +'"textureName" : "'+AsphaltTex+'"}}}'
        else:
            texture = '}'
                        
        full_line = full_line+'"'+name+'":'+telo+texture+','
        
    nodes_full = ''
    for obj in bpy.data.objects:
        objname = 'unusedTemplate'
        if len(obj.name)>5 and obj.name[:5]=='node_':
            objname = obj.name
        nodes_struc = '"'+objname+'":{'\
            +'"lodIn": 0,'\
            +'"lodOut": 1000,'\
            +'"layer":0,'\
            +'"castShadows": true,'\
            +'"isVisible": true,'\
            +'"isTransparent": false,'\
            +'"isRenderable": true}'
        nodes_full = nodes_full + nodes_struc+','
    
    
    res = json.loads('{'+full_line[:-1]+'}')
    Mat['materials']=res
    jnodes = json.loads('{'+nodes_full[:-1]+'}')
    Mat['nodes']=jnodes
    jdata = json.dumps(Mat, sort_keys=True, indent=4)
    svversion = os.path.normpath(os.path.join(bl_addons_path, 'settings.json')) 
    print('\n\n****** for_export_AssettoCorsa.py '+str(bl_info['version'])+' *******')
    print(jdata)
    print(svversion)
    
    file = open(svversion, "w") 
    file.write(jdata)
    file.close()
    return {'FINISHED'}


def loadMat(bl_addons_path_):
    bl_addons_path=chekdir(bl_addons_path_)
    script_paths = os.path.normpath(os.path.dirname(__file__)) 
    svversion = os.path.normpath(os.path.join(bl_addons_path, 'settings.json')) 
    if not os.path.exists(svversion):
        return {}
    
    file = open(svversion, 'r')
    Mats_=file.read()
    file.close()
    
    Mats = json.loads(Mats_)
    materials = Mats['materials']
        
    jdata = json.dumps(Mats, sort_keys=True, indent=4)
    return materials


class Faec_op(bpy.types.Operator):
 
    bl_idname = "object.faec"
    bl_label = "For export AssettoCorsa"
    bl_options = {'REGISTER', 'UNDO', 'PRESET'}  
 
    def execute(self, context):
        bpy.ops.export_test.some_data('INVOKE_DEFAULT')
        return {'FINISHED'}  


class Faec_panel(bpy.types.Panel):
    """Creates a Panel in the Object properties window"""
    bl_label = "For_export_AssettoCorsa"
    bl_idname = "OBJECT_PT_faec"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    bl_options = {'DEFAULT_CLOSED'} 

    def draw(self, context):                    
        layout = self.layout
        col = layout.column(align=True)
        col.operator("object.faec", text = 'Выгрузить настройки!')


class ExportSomeData(bpy.types.Operator, ExportHelper):
    """This appears in the tooltip of the operator and in the generated docs"""
    bl_idname = "export_test.some_data"  # important since its how bpy.ops.import_test.some_data is constructed
    bl_label = "Export Some Data"

    # ExportHelper mixin class uses this
    filename_ext = ""

    def execute(self, context):
        return saveMat2(loadMat(self.filepath), self.filepath)


            

classes = [Faec_op, Faec_panel, ExportSomeData]

# registering and menu integration
def register():
    for c in classes:                              
        bpy.utils.register_class(c)    

# unregistering and removing menus  
def unregister():    
    for c in reversed(classes):  
        bpy.utils.unregister_class(c)
                                        
if __name__ == "__main__":
    register() 

