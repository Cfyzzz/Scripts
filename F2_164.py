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

# <pep8 compliant>

bl_info = {
    'name': "F2",
    'author': "Bart Crouch, Alexander Nedovizin",
    'version': (1, 6, 4),
    'blender': (2, 68, 0),
    'location': "Editmode > F",
    'warning': "",
    'description': "Extends the 'Make Edge/Face' functionality",
    'wiki_url': "http://wiki.blender.org/index.php/Extensions:2.6/Py/"\
        "Scripts/Modeling/F2",
    'tracker_url': "http://projects.blender.org/tracker/index.php?"\
        "func=detail&aid=33979",
    'category': 'Mesh'}


import bmesh
import bpy
import itertools
import mathutils
from bpy_extras import view3d_utils
from bpy.props import StringProperty, BoolProperty
from bpy.types import AddonPreferences

class F2AddonPreferences(AddonPreferences):
    bl_idname = __name__

    boolean = BoolProperty(
            name="Auto Grab",
            default=False,
            )

    def draw(self, context):
        layout = self.layout
        layout.label(text="Settings")
        layout.prop(self, "boolean")
        
# create a face from a single selected edge
def quad_from_edge(bm, edge_sel, context, event):
    ob = context.active_object
    region = context.region
    region_3d = context.space_data.region_3d

    # find linked edges that are open (<2 faces connected) and not part of
    # the face the selected edge belongs to
    all_edges = [[edge for edge in edge_sel.verts[i].link_edges if \
        len(edge.link_faces) < 2 and edge != edge_sel and \
        sum([face in edge_sel.link_faces for face in edge.link_faces]) == 0] \
        for i in range(2)]
    if not all_edges[0] or not all_edges[1]:
        return

    # determine which edges to use, based on mouse cursor position
    mouse_pos = mathutils.Vector([event.mouse_region_x, event.mouse_region_y])
    optimal_edges = []
    for edges in all_edges:
        min_dist = False
        for edge in edges:
            vert = [vert for vert in edge.verts if not vert.select][0]
            world_pos = ob.matrix_world * vert.co.copy()
            screen_pos = view3d_utils.location_3d_to_region_2d(region,
                region_3d, world_pos)
            dist = (mouse_pos - screen_pos).length
            if not min_dist or dist < min_dist[0]:
                min_dist = (dist, edge, vert)
        optimal_edges.append(min_dist)

    # determine the vertices, which make up the quad
    v1 = edge_sel.verts[0]
    v2 = edge_sel.verts[1]
    edge_1 = optimal_edges[0][1]
    edge_2 = optimal_edges[1][1]
    v3 = optimal_edges[0][2]
    v4 = optimal_edges[1][2]

    # normal detection
    flip_align = True
    normal_edge = edge_1
    if not normal_edge.link_faces:
        normal_edge = edge_2
        if not normal_edge.link_faces:
            normal_edge = edge_sel
            if not normal_edge.link_faces:
                # no connected faces, so no need to flip the face normal
                flip_align = False
    if flip_align: # there is a face to which the normal can be aligned
        ref_verts = [v for v in normal_edge.link_faces[0].verts]
        if v3 in ref_verts:
            va_1 = v3
            va_2 = v1
        elif normal_edge == edge_sel:
            va_1 = v1
            va_2 = v2
        else:
            va_1 = v2
            va_2 = v4
        if (va_1 == ref_verts[0] and va_2 == ref_verts[-1]) or \
        (va_2 == ref_verts[0] and va_1 == ref_verts[-1]):
            # reference verts are at start and end of the list -> shift list
            ref_verts = ref_verts[1:] + [ref_verts[0]]
        if ref_verts.index(va_1) > ref_verts.index(va_2):
            # connected face has same normal direction, so don't flip
            flip_align = False

    # material index detection
    ref_faces = edge_sel.link_faces
    if not ref_faces:
        ref_faces = edge_sel.verts[0].link_faces
    if not ref_faces:
        ref_faces = edge_sel.verts[1].link_faces
    if not ref_faces:
        mat_index = False
        smooth = False
    else:
        mat_index = ref_faces[0].material_index
        smooth = ref_faces[0].smooth

    # create quad
    try:
        verts = [v3, v1, v2, v4]
        if flip_align:
            verts.reverse()
        face = bm.faces.new(verts)
        if mat_index:
            face.material_index = mat_index
        face.smooth = smooth
    except:
        # face already exists
        return

    # change selection
    edge_sel.select = False
    for vert in edge_sel.verts:
        vert.select = False
    for edge in face.edges:
        if edge.index < 0:
            edge.select = True
    v3.select = True
    v4.select = True

    # toggle mode, to force correct drawing
    bpy.ops.object.mode_set(mode='OBJECT')
    bpy.ops.object.mode_set(mode='EDIT')


def decorator_grab(func):
    #decorate function invoke of class MeshF2
    def bm_vert_active_get(ob):
        bm = bmesh.from_edit_mesh(ob.data)
        for elem in reversed(bm.select_history):
            if isinstance(elem, bmesh.types.BMVert):
                return elem.index  
        return -1
        
    
    def wrapper(self, context, event):
        obj = bpy.context.active_object    
        bm = bmesh.from_edit_mesh(obj.data)
        sel = [v for v in bm.verts if v.select]    
        if len(sel) == 1 and bm_vert_active_get(obj)==-1:        
            return {'CANCELLED'}
        
        
        res = func(self, context, event)
        bpy.ops.object.mode_set(mode='OBJECT')
        bpy.ops.object.mode_set(mode='EDIT')

        user_preferences = context.user_preferences
        addon_prefs = user_preferences.addons[__name__].preferences
        
        obj = bpy.context.active_object        
        selected_verts = [i.index for i in obj.data.vertices if i.select]  
        if len(selected_verts) == 1 and addon_prefs.boolean:
                bpy.ops.transform.translate('INVOKE_DEFAULT')

        return res
    return wrapper

def quad_from_vertex(bm, vert_sel, context, event):
    ob = context.active_object
    region = context.region
    region_3d = context.space_data.region_3d

    # find linked edges that are open (<2 faces connected)
    edges = [edge for edge in vert_sel.link_edges if len(edge.link_faces) < 2]
    if len(edges) < 2:
        return

    # determine which edges to use, based on mouse cursor position
    min_dist = False
    mouse_pos = mathutils.Vector([event.mouse_region_x, event.mouse_region_y])
    for a, b in itertools.combinations(edges, 2):
        other_verts = [vert for edge in [a, b] for vert in edge.verts \
            if not vert.select]
        mid_other = (other_verts[0].co.copy() + other_verts[1].co.copy()) \
            / 2
        new_pos = 2 * (mid_other - vert_sel.co.copy()) + vert_sel.co.copy()
        world_pos = ob.matrix_world * new_pos
        screen_pos = view3d_utils.location_3d_to_region_2d(region, region_3d,
            world_pos)
        dist = (mouse_pos - screen_pos).length
        if not min_dist or dist < min_dist[0]:
            min_dist = (dist, (a, b), other_verts, new_pos)

    # create vertex at location mirrored in the line, connecting the open edges
    edges = min_dist[1]
    other_verts = min_dist[2]
    new_pos = min_dist[3]
    vert_new = bm.verts.new(new_pos)

    # normal detection
    flip_align = True
    normal_edge = edges[0]
    if not normal_edge.link_faces:
        normal_edge = edges[1]
        if not normal_edge.link_faces:
            # no connected faces, so no need to flip the face normal
                flip_align = False
    if flip_align: # there is a face to which the normal can be aligned
        ref_verts = [v for v in normal_edge.link_faces[0].verts]
        if other_verts[0] in ref_verts:
            va_1 = other_verts[0]
            va_2 = vert_sel
        else:
            va_1 = vert_sel
            va_2 = other_verts[1]
        if (va_1 == ref_verts[0] and va_2 == ref_verts[-1]) or \
        (va_2 == ref_verts[0] and va_1 == ref_verts[-1]):
            # reference verts are at start and end of the list -> shift list
            ref_verts = ref_verts[1:] + [ref_verts[0]]
        if ref_verts.index(va_1) > ref_verts.index(va_2):
            # connected face has same normal direction, so don't flip
            flip_align = False

    # material index detection
    ref_faces = vert_sel.link_faces
    if not ref_faces:
        mat_index = False
        smooth = False
    else:
        mat_index = ref_faces[0].material_index
        smooth = ref_faces[0].smooth

    # create face between all 4 vertices involved
    verts = [other_verts[0], vert_sel, other_verts[1], vert_new]
    if flip_align:
        verts.reverse()
    face = bm.faces.new(verts)
    if mat_index:
        face.material_index = mat_index
    face.smooth = smooth

    # change selection
    vert_new.select = True
    vert_sel.select = False

    # toggle mode, to force correct drawing
    bpy.ops.object.mode_set(mode='OBJECT')
    bpy.ops.object.mode_set(mode='EDIT')


class MeshF2(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "mesh.f2"
    bl_label = "Make Edge/Face"
    bl_description = "Extends the 'Make Edge/Face' functionality"
    bl_options = {'REGISTER', 'UNDO'}
    
    

    @classmethod
    def poll(cls, context):
        # check we are in mesh editmode
        ob = context.active_object
        return(ob and ob.type == 'MESH' and context.mode == 'EDIT_MESH')

    @decorator_grab #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    def invoke(self, context, event):
        bm = bmesh.from_edit_mesh(context.active_object.data)
        sel = [v for v in bm.verts if v.select]
        if len(sel) > 2:
            # original 'Make Edge/Face' behaviour
            try:
                bpy.ops.mesh.edge_face_add('INVOKE_DEFAULT')
            except:
                return {'CANCELLED'}
        elif len(sel) == 1:
            # single vertex selected -> mirror vertex and create new face
            quad_from_vertex(bm, sel[0], context, event)
        elif len(sel) == 2:
            edges_sel = [ed for ed in bm.edges if ed.select]
            if len(edges_sel) != 1:
                # 2 vertices selected, but not on the same edge
                bpy.ops.mesh.edge_face_add()
            else:
                # single edge selected -> new face from linked open edges
                quad_from_edge(bm, edges_sel[0], context, event)

        return {'FINISHED'}


# registration
classes = [MeshF2, F2AddonPreferences]
addon_keymaps = []


def register():
    # add operator
    for c in classes:
        bpy.utils.register_class(c)

    # add keymap entry
    km = bpy.context.window_manager.keyconfigs.addon.keymaps.new(\
        name='Mesh', space_type='EMPTY')
    kmi = km.keymap_items.new("mesh.f2", 'F', 'PRESS')
    addon_keymaps.append((km, kmi))


def unregister():
    # remove keymap entry
    for km, kmi in addon_keymaps:
        km.keymap_items.remove(kmi)
        #bpy.context.window_manager.keyconfigs.addon.keymaps.remove(km)
    addon_keymaps.clear()
    
    # remove operator
    for c in reversed(classes):
        bpy.utils.unregister_class(c)

if __name__ == "__main__":
    register()
