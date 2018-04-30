# -*- coding: utf-8 -*-   

# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####  


bl_info = {
    "name": "Auto Perspective",
    "author": "Alexander Nedovizin",
    "version": (0, 1, 0),
    "blender": (2, 7, 0),
    "location": "View3D > Auto Perspective",
    "category": "3D View"
}   

import bpy



def main(context):
    pass
    return

class ModalTimerOperator(bpy.types.Operator):
    """Operator which runs its self from a timer"""
    bl_idname = "wm.modal_timer_operator"
    bl_label = "Start AutoPersp"

    _timer = None
    frequence = bpy.props.FloatProperty(name="Frequence", default=1.0)
    mode = bpy.props.BoolProperty(name="Mode", default=False)
    
    @classmethod
    def poll(cls, context):
        return (context.area.type == 'VIEW_3D')
    
    def modal(self, context, event):
        config = bpy.context.window_manager.CONFIG_Z
        if event.type == 'ESC' or config.label == 'Start AutoPersp':
            return self.cancel(context)

        if event.type == 'TIMER':
            main(context)
            
        if event.type in ['NUMPAD_1', 'NUMPAD_3', 'NUMPAD_7']:
            view3d = context.space_data.region_3d
            view3d.view_perspective = 'ORTHO'
            view3d.update()
            self.mode = True
            
        if event.type == 'MIDDLEMOUSE':
            view3d = context.space_data.region_3d
            if self.mode:
                view3d.view_perspective = 'PERSP'
                view3d.update()
                self.mode = False

        return {'PASS_THROUGH'}

    def invoke(self, context, event):
        self._timer = context.window_manager.event_timer_add(self.frequence, context.window)
        context.window_manager.modal_handler_add(self)
        config = bpy.context.window_manager.CONFIG_Z
        if config.label == 'Start AutoPersp':
            config.label = 'Stop AutoPersp'
        else:
            config.label = 'Start AutoPersp'
        return {'RUNNING_MODAL'}

    def cancel(self, context):
        context.window_manager.event_timer_remove(self._timer)
        config = bpy.context.window_manager.CONFIG_Z
        config.label = 'Start AutoPersp'
        return {'FINISHED'}


class HelloWorldPanel(bpy.types.Panel):
    """Creates a Panel in the Object properties window"""
    bl_label = "Auto Perspective"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    
    
    def draw(self, context):
        config = bpy.context.window_manager.CONFIG_Z
        
        layout = self.layout
        col = layout.column(align=True)
        
        split = col.split(percentage=0.15)
        if config.display:
            split.prop(config, "display", text="", icon='DOWNARROW_HLT')
        else:
            split.prop(config, "display", text="", icon='RIGHTARROW')
        
        timer_op = split.operator("wm.modal_timer_operator", text = config.label)
        timer_op.frequence = config.frequence
        
        if config.display:
            box = col.column(align=True).box().column()
            col_top = box.column(align=True)
            row = col_top.row(align=True)
            row.prop(config,'frequence')
                
                

class UIElements(bpy.types.PropertyGroup):
    frequence = bpy.props.FloatProperty(name="Frequence")
    label = bpy.props.StringProperty(name="label")
    display = bpy.props.BoolProperty(name="display")


def register():
    bpy.utils.register_class(HelloWorldPanel)
    bpy.utils.register_class(ModalTimerOperator)
    bpy.utils.register_class(UIElements)
    bpy.types.WindowManager.CONFIG_Z = bpy.props.PointerProperty(type = UIElements)
    bpy.context.window_manager.CONFIG_Z.frequence = 1.0
    bpy.context.window_manager.CONFIG_Z.label = 'Start AutoPersp'
    bpy.context.window_manager.CONFIG_Z.display = False



def unregister():
    del bpy.types.WindowManager.CONFIG_Z
    bpy.utils.unregister_class(UIElements)
    bpy.utils.unregister_class(ModalTimerOperator)
    bpy.utils.unregister_class(HelloWorldPanel)


if __name__ == "__main__":
    register()

