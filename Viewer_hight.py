# -*- coding: utf-8 -*-   ﻿

bl_info = {
    "name": "Viewer Hights",
    "author": "Alexander Nedovizin",
    "version": (0, 1, 4),
    "blender": (2, 6, 8),
    "location": "View3D > Viewer Hights",
    "category": "3D View"
}   

import bpy
import random, mathutils
from mathutils import Matrix

def align_matrix(locat):
    context = bpy.context
    loc = Matrix.Translation(locat)
    print('Type',context.space_data.type)

    if (context.space_data.type == 'VIEW_3D'):
        print('align')
        rot = context.space_data.region_3d.view_matrix.to_3x3().inverted().to_4x4()
    else:
        rot = Matrix()
    align_matrix = loc * rot
    return align_matrix



def main(context):
    config = bpy.data.scenes[0].CONFIG_Z
    scene = bpy.context.scene 
    object = bpy.context.object
    mesh = object.data                                  
    texts = []    
    if object.name[:6] == 'Number':
        return
    
    mode_o = object.mode
    bpy.ops.object.mode_set(mode='OBJECT')
    bpy.ops.object.mode_set(mode='EDIT')
    bpy.ops.object.mode_set(mode=mode_o)
    
    for v in mesh.vertices: 
      name_text = 'Number'+str(v.index)
      if not v.select :
        name_text = 'Number'+str(v.index)
        if name_text in bpy.data.objects:
            bpy.data.objects[name_text].hide=True
        continue
            
      if name_text not in bpy.data.objects:
        textData = bpy.data.curves.new('Number','FONT') 
        textData.size = config.size / 100
        name_text = 'Number'+str(v.index)
        textOb = bpy.data.objects.new(name_text, textData) 
        scene.objects.link(textOb) 
        texts.append(textOb) 
      else:
          textOb = bpy.data.objects[name_text]
          textOb.hide=False
      textOb.matrix_world = align_matrix(v.co)
      textOb.data.body = str(round((object.matrix_local*textOb.location).z,3))
      #textOb.location += mathutils.Vector((0.1,0.1,0.1))
      textOb.show_x_ray = config.x_ray
      textOb.matrix_world = object.matrix_local * textOb.matrix_world
      
      mat = config.mat
      if mat in bpy.data.materials:
          if len(textOb.material_slots)>0:
              textOb.material_slots[0].material = bpy.data.materials[mat]
          else:
              textOb.select = True
              tmpObj = scene.objects.active 
              scene.objects.active = textOb
              bpy.ops.object.material_slot_add()
              textOb.material_slots[0].material = bpy.data.materials[mat]
              scene.objects.active = tmpObj
              textOb.select = False
    

class ModalTimerOperator(bpy.types.Operator):
    """Operator which runs its self from a timer"""
    bl_idname = "wm.modal_timer_operator"
    bl_label = "Start View Hight"

    _timer = None
    frequence = bpy.props.FloatProperty(name="Frequence", default=1.0)
    
    def modal(self, context, event):
        if event.type == 'ESC':
            return self.cancel(context)

        if event.type == 'TIMER':
            main(context)

        return {'PASS_THROUGH'}

    def execute(self, context):
        self._timer = context.window_manager.event_timer_add(self.frequence, context.window)
        context.window_manager.modal_handler_add(self)
        return {'RUNNING_MODAL'}

    def cancel(self, context):
        context.window_manager.event_timer_remove(self._timer)
        object = bpy.context.object
        mode_o = object.mode
        bpy.ops.object.mode_set(mode='OBJECT')
        bpy.ops.object.hide_view_clear()
        bpy.ops.object.select_all(action='DESELECT')
        bpy.ops.object.select_pattern(pattern='Number*')
        bpy.ops.object.delete()
        bpy.ops.object.mode_set(mode=mode_o)
        object.select = True
        bpy.context.scene.objects.active = object
        return {'CANCELLED'}





class HelloWorldPanel(bpy.types.Panel):
    """Creates a Panel in the Object properties window"""
    bl_label = "Viewer Hight"
    bl_idname = "OBJECT_PT_hello"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'

    def draw(self, context):
        config = bpy.data.scenes[0].CONFIG_Z
        
        layout = self.layout
        col = layout.column(align=True)
        
        split = col.split(percentage=0.15)
        if config.display:
            split.prop(config, "display", text="", icon='DOWNARROW_HLT')
        else:
            split.prop(config, "display", text="", icon='RIGHTARROW')
        
        timer_op = split.operator("wm.modal_timer_operator")
        timer_op.frequence = config.frequence
        
        if config.display:
            box = col.column(align=True).box().column()
            col_top = box.column(align=True)
            row = col_top.row(align=True)
            row.prop(config,'frequence')
            row = col_top.row(align=True)
            row.prop(config,'x_ray')
            row = col_top.row(align=True)
            row.prop(config,'size')
            row = col_top.row(align=True)
            row.prop(config,'mat')
                
                
        
        


class UIElements(bpy.types.PropertyGroup):
    frequence = bpy.props.FloatProperty(name="Frequence")
    x_ray = bpy.props.BoolProperty(name="X-ray")
    size = bpy.props.IntProperty(name="Size")
    mat = bpy.props.StringProperty(name="Material")
    display = bpy.props.BoolProperty(name="display")


def register():
    bpy.utils.register_class(HelloWorldPanel)
    bpy.utils.register_class(ModalTimerOperator)
    bpy.utils.register_class(UIElements)
    bpy.types.Scene.CONFIG_Z = bpy.props.PointerProperty(type = UIElements)
    bpy.data.scenes[0].CONFIG_Z.frequence = 1.0
    bpy.data.scenes[0].CONFIG_Z.mat = ''
    bpy.data.scenes[0].CONFIG_Z.display = False


def unregister():
    if 'CONFIG_Z' in bpy.data.scenes[0] != None:
        del bpy.data.scenes[0]['CONFIG_Z']
        del bpy.types.Scene.CONFIG_Z
    bpy.utils.unregister_class(UIElements)
    bpy.utils.unregister_class(ModalTimerOperator)
    bpy.utils.unregister_class(HelloWorldPanel)


if __name__ == "__main__":
    register()
    #unregister()
