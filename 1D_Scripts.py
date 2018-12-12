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

# HISTORY
# 0-8-93 (26-10-2017) Changed default option (Sure UV)
# 0-8-94 (27-10-2017) Fixed spread type (Obj distribute by X)
# 0-8-95 (07-11-2017) Added (Loop Resolve) =Blendup cleanup
# 0-8-96 (08-11-2017) Fixed (Loop Resolve) =Blendup cleanup
# 0-8-97 (10-11-2017) New mode: EDGE (Loop Resolve) =Blendup cleanup
# 0-8-98 (20-11-2017) Added (UV/Images -> T-panel -> 1D -> Print loop)
# 0-8-99 (01.12.2017) Fixed (FEDGE, Spread Loop)
# 0-8-100(08.12.2017) Added (Make Border) =Test Zone
# 0-8-101(18.12.2017) Fixed (Mats Unclone - rename if one mat too) =Misc, Added (UV Scaler) =Test Zone
# 0-8-102(15.01.2018) Fixed (Loop Resolve, Select Chunks = vertices mode)
# 0-8-103(22.01.2018) Added (Fedge) nonquads
# 0-8-104(29.01.2018) Changed option (make border) =size +-100
# 0-8-105(31.01.2018) Added (RCS Read Camera Setup)
# 0-8-106(31.01.2018) UI (RCS Read Camera Setup)
# 0-8-107(10.02.2018) Misc (Obj switch on) - Add button OFF and modify logic
# 0-8-108(16.02.2018) Change settings default (Spread Loop => Uniform=False)
# 0-8-109(16.02.2018) Fix (Loop Resolve = relation by Dist)
# 0-8-110(16.02.2018) Fix (RCS) obj.name replace to cam.data.name
# 0-8-111(15.03.2018) Added (Naming/Instances -> Guess Active Instanes) = option Filter_mats
# 0-8-112(15.03.2018) Change settings default (Blendup cleanup) Obj verts report = 30
# 0-8-113(23.03.2018) Fix (Loop Resolve = relation by Dist) and Change settings default loopresolve_relative = True
# 0-9-0(31.03.2018) Add new Catgory: Render = [Render Nikits's Akimov], [Batch Render]
# 0-9-1(03.04.2018) Added (Render) Prew & Next camera's [Nikitron script]
# 0-9-2(06.04.2018) Change (Render = Prev/Next) - select and set active current cam
# 0-9-3(09.04.2018) Change (Naming/Instances = Select iinstances) add separate by type object: MESH, CURVE
# 0-9-4(13.04.2018) Change (Naming/Instances = Select iinstances) add message format: selected, inst, unique
# 0-9-5(15.04.2018) Change (Search instances 1 and 2) unified search logic
# 0-9-6(15.04.2018) Added (TestZone: Instance Resizer)
# 0-9-7(21.04.2018) Fix(Naming/Instances = Guess Active Instancess) select find objects
# 0-9-8(23.04.2018) Fix(Naming/Instances = Guess Chain Instancess) select find objects
# 0-9-9(28.04.2018) Change (Naming/Instances = Propagate Obname) array processing
# 0-9-10(30.04.2018) Fix (Naming/Instances = Propagate Obname) array processing
# 0-9-11(02.05.2018) Change (FEDGE) = fast check edges
# 0-9-12(09.05.2018) Added (TestZone: NJoin)
# 0-9-13(15.05.2018) Fix (TestZone: NJoin) active negative
# 0-9-14(17.05.2018) Move Panels: LoopResolve and LoopReduce, Remove button AutoUpdate, New format Name Panel with version
# 0-9-15(17.05.2018) Fix (TestZone: Instance Resizer) removed the reaction to a negative scale
# 0-9-16(19.05.2018) Fix (TestZone: Instance Resizer) correct scaling of instances
# 0-9-17(22.05.2018) Change (Multiple obj import) new func [By layers]: Import sorted by name objects to layers
# 0-9-18(23.05.2018) Change (Multiple obj import) new func [By layers]: Import into layers from the first selected
# 0-9-19(07.06.2018) Change (Naming/Instances = Propagate Obname) base objname > meshname >> all instances objname
# 0-9-20(08.06.2018) Added (Corner Edges) new CornerCross and ExtendCross
# 0-9-21(08.06.2018) Change (Blendup Cleanup = Verts project) save face after split
# 0-9-22(10.06.2018) Change (TestZone: Instance Resizer) scale apply to independent objects
# 0-9-23(14.06.2018) Fix (Blendup Cleanup = Verts project) Blender crashed after it and use f2
# 0-9-24(15.06.2018) Added (TestZone = Volume Select)
# 0-9-25(15.06.2018) Fix (TestZone = Volume Select)
# 0-9-26(15.06.2018) Fix (TestZone = Volume Select) add icon for modes
# 0-9-27(23.07.2018) Added (TestZone) Batch Remover
# 0-9-28(23.07.2018) Move Panel: Batch Remover
# 0-9-29(03.09.2018) Render(UI): Add Shortcut
# 0-9-30(08.09.2018) Change (Instances ++ replace) add: Use translation
# 0-9-31(09.09.2018) Change (Instances ++ replace) add: Selected only
# 0-9-32(11.09.2018) Change (Instances ++ replace) inactivate Selected only
# 0-9-33(02.10.2018) Change (Render) add: OpenGL Render
# 0-10-00(11.10.2018) Reformat Panel Edges/loops
# 0-10-01(19.10.2018) Upp version
# 0-10-02(19.10.2018) Bugfix
# 0-10-03(19.10.2018) Bugfix
# 0-10-04(23.10.2018) Set the panels in order
# 0-10-05(23.10.2018) Changed the order of the tools
# 0-10-06(27.10.2018) Filter on the Mesh of the functions guess_active_instance, chain_instance, obname_to_meshname, meshname_to_obname
# 0-10-07(06.11.2018) Changed (Mats sort) show in seacher
# 0-10-09(16.11.2018) Fixed panel Batch render
# 0-10-10(16.11.2018) Fixed UV Scaler
# 0-10-12(18.11.2018) Fixed (Test Zone) Polyedge select
# 0-10-13(21.11.2018) Added (Test Zone) Ssmooth
# 0-10-14(23.11.2018) Fixed (Test Zone) Ssmooth - add Shortcut
# 0-10-15(12.12.2018) Changed (Corner Edges): enable To Active edge
# 0-10-16(12.12.2018) Changed (Stairs maker): go to source object after execution

bl_info = {
    "name": "1D_Scripts",
    "author": "Alexander Nedovizin, Paul Kotelevets aka 1D_Inc (concept design), Nikitron",
    "version": (0, 10, 16),
    "blender": (2, 7, 9),
    "location": "View3D > Toolbar",
    "category": "Mesh"
}

# https://github.com/Cfyzzz/Scripts/blob/master/1D_Scripts.py

import bpy, bmesh, mathutils, math
from mathutils import Vector, Matrix
from mathutils.geometry import intersect_line_plane, intersect_point_line, intersect_line_line
from math import sin, cos, pi, sqrt, degrees, tan, radians
import os, urllib
from bpy.props import (BoolProperty,
                       FloatProperty,
                       StringProperty,
                       EnumProperty,
                       IntProperty,
                       CollectionProperty,
                       FloatVectorProperty
                       )
from bpy_extras.io_utils import ExportHelper, ImportHelper
from bpy.types import Operator
import time
from collections import namedtuple
from operator import mul, itemgetter, add, attrgetter
from functools import reduce
from abc import abstractmethod, ABCMeta
from addon_utils import check

list_z = []
mats_idx = []
list_f = []
maloe = 1e-5
steps_smoose = 0
omsureuv_all_scale_def_glob = 1.0


def check_lukap(bm):
    if hasattr(bm.verts, "ensure_lookup_table"):
        bm.verts.ensure_lookup_table()
        bm.edges.ensure_lookup_table()
        bm.faces.ensure_lookup_table()


# ----- Module: edge fillet-------
# author this module: Zmj100
# version 0.3.0
# ref:
def a_rot(ang, rp, axis, q):
    mtrx = Matrix.Rotation(ang, 3, axis)
    tmp = q - rp
    tmp1 = mtrx * tmp
    tmp2 = tmp1 + rp
    return tmp2


# ------ ------
class f_buf():
    an = 0


# ------ ------
def f_edgefillet(bme, list_0, adj, n, radius, out, flip):
    check_lukap(bme)

    dict_0 = get_adj_v_(list_0)
    list_1 = [[dict_0[i][0], i, dict_0[i][1]] for i in dict_0 if (len(dict_0[i]) == 2)][0]

    list_del = [bme.verts[list_1[1]]]
    list_2 = []

    p = (bme.verts[list_1[1]].co).copy()
    p1 = (bme.verts[list_1[0]].co).copy()
    p2 = (bme.verts[list_1[2]].co).copy()

    vec1 = p - p1
    vec2 = p - p2

    ang = vec1.angle(vec2, any)
    f_buf.an = round(degrees(ang))

    if f_buf.an == 180 or f_buf.an == 0.0:
        pass
    else:
        opp = adj
        if radius == False:
            h = adj * (1 / cos(ang * 0.5))
            d = adj
        elif radius == True:
            h = opp / sin(ang * 0.5)
            d = opp / tan(ang * 0.5)

        p3 = p - (vec1.normalized() * d)
        p4 = p - (vec2.normalized() * d)

        no = (vec1.cross(vec2)).normalized()
        rp = a_rot(radians(90), p, (p3 - p4), (p - (no * h)))

        vec3 = rp - p3
        vec4 = rp - p4

        axis = vec1.cross(vec2)

        if out == False:
            if flip == False:
                rot_ang = vec3.angle(vec4)
            elif flip == True:
                rot_ang = vec1.angle(vec2)
        elif out == True:
            rot_ang = (2 * pi) - vec1.angle(vec2)

        for j in range(n + 1):
            if out == False:
                if flip == False:
                    tmp2 = a_rot(rot_ang * j / n, rp, axis, p4)
                elif flip == True:
                    tmp2 = a_rot(rot_ang * j / n, p, axis, p - (vec1.normalized() * opp))
            elif out == True:
                tmp2 = a_rot(rot_ang * j / n, p, axis, p - (vec2.normalized() * opp))

            bme.verts.new(tmp2)
            bme.verts.index_update()
            check_lukap(bme)
            list_2.append(bme.verts[-1].index)

        check_lukap(bme)
        if flip == True:
            list_1[1:2] = list_2
        else:
            list_2.reverse()
            list_1[1:2] = list_2
        list_2[:] = []

        n1 = len(list_1)
        for t in range(n1 - 1):
            bme.edges.new([bme.verts[list_1[t]], bme.verts[list_1[(t + 1) % n1]]])
            bme.edges.index_update()

        check_lukap(bme)

    bme.verts.remove(list_del[0])
    bme.verts.index_update()
    check_lukap(bme)


class f_op0(bpy.types.Operator):
    bl_idname = 'f.op0_id'
    bl_label = 'Edge Fillet'
    bl_options = {'REGISTER', 'UNDO'}

    adj = FloatProperty(name='', default=0.1, min=0.00001, max=100.0, step=1, precision=3)
    n = IntProperty(name='', default=3, min=1, max=100, step=1)
    out = BoolProperty(name='Outside', default=False)
    flip = BoolProperty(name='Flip', default=False)
    radius = BoolProperty(name='Radius', default=False)

    def draw(self, context):
        layout = self.layout
        if f_buf.an == 180 or f_buf.an == 0.0:
            box = layout.box()
            box.label('Info:')
            box.label('Angle equal to 0 or 180,')
            box.label('unable to fillet.')
        else:
            box = layout.box()
            box.prop(self, 'radius')
            row = box.split(0.35, align=True)

            if self.radius == True:
                row.label('Radius:')
            elif self.radius == False:
                row.label('Distance:')
            row.prop(self, 'adj')
            row1 = box.split(0.55, align=True)
            row1.label('Number of sides:')
            row1.prop(self, 'n', slider=True)

            if self.n > 1:
                row2 = box.split(0.50, align=True)
                row2.prop(self, 'out')
                if self.out == False:
                    row2.prop(self, 'flip')

    def execute(self, context):
        adj = self.adj
        n = self.n
        out = self.out
        flip = self.flip
        radius = self.radius

        edit_mode_out()
        ob_act = context.active_object
        bme = bmesh.new()
        bme.from_mesh(ob_act.data)
        check_lukap(bme)

        list_0 = [[v.index for v in e.verts] for e in bme.edges if e.select and e.is_valid]
        if not list_0:
            list_v = [v.index for v in bme.verts if v.select and v.is_valid]

        if not list_0 and len(list_v) == 1:
            connected_edges = bme.verts[list_v[0]].link_edges
            list_1 = [[v.index for v in e.verts] for e in connected_edges if e.is_valid]
            if len(list_1) != 2:
                self.report({'INFO'}, 'Two adjacent edges or single vert must be selected.')
                edit_mode_in()
                return {'CANCELLED'}

            if out == True:
                flip = False
            f_edgefillet(bme, list_1, adj, n, radius, out, flip)

        elif len(list_0) != 2:
            self.report({'INFO'}, 'Two adjacent edges or single vert must be selected.')
            edit_mode_in()
            return {'CANCELLED'}
        else:
            if out == True:
                flip = False
            f_edgefillet(bme, list_0, adj, n, radius, out, flip)

        bme.to_mesh(ob_act.data)
        edit_mode_in()
        bpy.ops.mesh.select_all(action='DESELECT')
        return {'FINISHED'}


# ----- Module: extrude along path -------
# author this module: Zmj100
# version 0.5.0.9
# ref: http://blenderartists.org/forum/showthread.php?179375-Addon-Edge-fillet-and-other-bmesh-tools-Update-Jan-11

def edit_mode_out():
    bpy.ops.object.mode_set(mode='OBJECT')


def edit_mode_in():
    bpy.ops.object.mode_set(mode='EDIT')


def get_adj_v_(list_):
    tmp = {}
    for i in list_:
        try:
            tmp[i[0]].append(i[1])
        except KeyError:
            tmp[i[0]] = [i[1]]
        try:
            tmp[i[1]].append(i[0])
        except KeyError:
            tmp[i[1]] = [i[0]]
    return tmp


def f_1(frst, list_, last):  # edge chain
    fi = frst
    tmp = [frst]
    while list_ != []:
        for i in list_:
            if i[0] == fi:
                tmp.append(i[1])
                fi = i[1]
                list_.remove(i)
            elif i[1] == fi:
                tmp.append(i[0])
                fi = i[0]
                list_.remove(i)
        if tmp[-1] == last:
            break
    return tmp


def f_2(frst, list_):  # edge loop
    fi = frst
    tmp = [frst]
    while list_ != []:
        for i in list_:
            if i[0] == fi:
                tmp.append(i[1])
                fi = i[1]
                list_.remove(i)
            elif i[1] == fi:
                tmp.append(i[0])
                fi = i[0]
                list_.remove(i)
        if tmp[-1] == frst:
            break
    return tmp


def is_loop_(list_fl):
    return True if len(list_fl) == 0 else False


def e_no_(bme, indx, p, p1):
    if hasattr(bme.verts, "ensure_lookup_table"):
        bme.verts.ensure_lookup_table()
    tmp1 = (bme.verts[indx].co).copy()
    tmp1[0] += 0.1
    tmp1[1] += 0.1
    tmp1[2] += 0.1
    ip1 = intersect_point_line(tmp1, p, p1)[0]
    return tmp1 - ip1


# ------ ------
def f_(bme, dict_0, list_fl, loop):
    check_lukap(bme)
    if loop:
        list_1 = f_2(eap_buf.list_sp[0], eap_buf.list_ek)
        del list_1[-1]
    else:
        list_1 = f_1(eap_buf.list_sp[0], eap_buf.list_ek,
                     list_fl[1] if eap_buf.list_sp[0] == list_fl[0] else list_fl[0])

    list_2 = [v.index for v in bme.verts if v.select and v.is_valid]
    n1 = len(list_2)

    list_3 = list_2[:]

    dict_1 = {}
    for k in list_2:
        dict_1[k] = [k]

    n = len(list_1)
    for i in range(n):
        p = (bme.verts[list_1[i]].co).copy()
        p1 = (bme.verts[list_1[(i - 1) % n]].co).copy()
        p2 = (bme.verts[list_1[(i + 1) % n]].co).copy()
        vec1 = p - p1
        vec2 = p - p2
        ang = vec1.angle(vec2, any)

        if round(degrees(ang)) == 180.0 or round(degrees(ang)) == 0.0:
            pp = p - ((e_no_(bme, list_1[i], p, p1)).normalized() * 0.1)
            pn = vec1.normalized()
        else:
            pp = ((p - (vec1.normalized() * 0.1)) + (p - (vec2.normalized() * 0.1))) * 0.5
            pn = ((vec1.cross(vec2)).cross(p - pp)).normalized()

        if loop:  # loop
            if i == 0:
                pass
            else:
                for j in range(n1):
                    v = (bme.verts[list_3[j]].co).copy()
                    bme.verts.new(intersect_line_plane(v, v + (vec1.normalized() * 0.1), pp, pn))
                    bme.verts.index_update()
                    if hasattr(bme.verts, "ensure_lookup_table"):
                        bme.verts.ensure_lookup_table()
                    list_3[j] = bme.verts[-1].index
                    dict_1[list_2[j]].append(bme.verts[-1].index)

        else:  # path
            if i == 0:
                pass
            elif i == (n - 1):
                pp_ = p - ((e_no_(bme, list_fl[1] if eap_buf.list_sp[0] == list_fl[0] else list_fl[0], p,
                                  p1)).normalized() * 0.1)
                pn_ = vec1.normalized()
                for j in range(n1):
                    v = (bme.verts[list_3[j]].co).copy()
                    bme.verts.new(intersect_line_plane(v, v + (vec1.normalized() * 0.1), pp_, pn_))
                    bme.verts.index_update()
                    if hasattr(bme.verts, "ensure_lookup_table"):
                        bme.verts.ensure_lookup_table()
                    dict_1[list_2[j]].append(bme.verts[-1].index)
            else:
                for j in range(n1):
                    v = (bme.verts[list_3[j]].co).copy()
                    bme.verts.new(intersect_line_plane(v, v + (vec1.normalized() * 0.1), pp, pn))
                    bme.verts.index_update()
                    if hasattr(bme.verts, "ensure_lookup_table"):
                        bme.verts.ensure_lookup_table()
                    list_3[j] = bme.verts[-1].index
                    dict_1[list_2[j]].append(bme.verts[-1].index)

    # -- -- -- --
    list_4 = [[v.index for v in e.verts] for e in bme.edges if e.select and e.is_valid]
    n2 = len(list_4)

    for t in range(n2):
        for o in range(n if loop else (n - 1)):
            bme.faces.new([bme.verts[dict_1[list_4[t][0]][o]], bme.verts[dict_1[list_4[t][1]][o]],
                           bme.verts[dict_1[list_4[t][1]][(o + 1) % n]], bme.verts[dict_1[list_4[t][0]][(o + 1) % n]]])
            bme.faces.index_update()
            if hasattr(bme.faces, "ensure_lookup_table"):
                bme.faces.ensure_lookup_table()


# ------ ------
class eap_buf():
    list_ek = []  # path
    list_sp = []  # start point


# ------ operator 0 ------
class eap_op0(bpy.types.Operator):
    bl_idname = 'eap.op0_id'
    bl_label = '....'

    def execute(self, context):
        edit_mode_out()
        ob_act = context.active_object
        bme = bmesh.new()
        bme.from_mesh(ob_act.data)
        check_lukap(bme)
        eap_buf.list_ek[:] = []
        for e in bme.edges:
            if e.select and e.is_valid:
                eap_buf.list_ek.append([v.index for v in e.verts])
                e.select_set(0)
        bme.to_mesh(ob_act.data)
        edit_mode_in()
        bme.free()
        return {'FINISHED'}


# ------ operator 1 ------
class eap_op1(bpy.types.Operator):
    bl_idname = 'eap.op1_id'
    bl_label = '....'

    def execute(self, context):
        edit_mode_out()
        ob_act = context.active_object
        bme = bmesh.new()
        bme.from_mesh(ob_act.data)
        check_lukap(bme)
        eap_buf.list_sp[:] = []
        for v in bme.verts:
            if v.select and v.is_valid:
                eap_buf.list_sp.append(v.index)
                v.select_set(0)
        bme.to_mesh(ob_act.data)
        edit_mode_in()
        bme.free()
        return {'FINISHED'}


# ------ operator 2 ------
class eap_op2(bpy.types.Operator):
    bl_idname = 'eap.op2_id'
    bl_label = 'Extrude Along Path'
    bl_options = {'REGISTER', 'UNDO'}

    def draw(self, context):
        layout = self.layout

    def execute(self, context):
        edit_mode_out()
        ob_act = context.active_object
        bme = bmesh.new()
        bme.from_mesh(ob_act.data)
        check_lukap(bme)

        dict_0 = get_adj_v_(eap_buf.list_ek)
        list_fl = [i for i in dict_0 if (len(dict_0[i]) == 1)]
        loop = is_loop_(list_fl)
        f_(bme, dict_0, list_fl, loop)

        bme.to_mesh(ob_act.data)
        edit_mode_in()
        bme.free()
        return {'FINISHED'}


# ------ operator 3 ------
class eap_op3(bpy.types.Operator):
    bl_idname = 'eap.op3_id'
    bl_label = '.......'

    def execute(self, context):
        edit_mode_out()
        ob_act = context.active_object
        bme = bmesh.new()
        bme.from_mesh(ob_act.data)
        check_lukap(bme)
        av = bm_vert_active_get(bme)
        if av[1] == 'V':
            eap_buf.list_sp[:] = []
            v = bme.verts[av[0]]
            if v.select and v.is_valid:
                eap_buf.list_sp.append(v.index)
                v.select_set(0)
                bpy.ops.eap.op0_id()
        edit_mode_in()
        bme.free()
        return {'FINISHED'}


# -------------- END --- extrude along path ---------

# ----- Module: Sure UVW Map v.0.5.1 -------
# author this module: Alexander Milovsky (www.milovsky.ru)
# version 0.5.1
# ref: http://blenderartists.org/forum/showthread.php?236631-Addon-Simple-Box-UVW-Map-Modifier

# globals for Box Mapping
all_scale_def = 1
tex_aspect = 1.0
x_offset_def = 0
y_offset_def = 0
z_offset_def = 0
x_rot_def = 0
y_rot_def = 0
z_rot_def = 0

# globals for Best Planar Mapping
xoffset_def = 0
yoffset_def = 0
zrot_def = 0

# Preview flag
preview_flag = True


def show_texture():
    obj = bpy.context.active_object
    mesh = obj.data
    is_editmode = (obj.mode == 'EDIT')
    # if in EDIT Mode switch to OBJECT
    if is_editmode:
        bpy.ops.object.mode_set(mode='OBJECT', toggle=False)

    # if no UVtex - create it
    if not mesh.uv_textures:
        uvtex = bpy.ops.mesh.uv_texture_add()
    uvtex = mesh.uv_textures.active
    uvtex.active_render = True

    img = None
    aspect = 1.0
    mat = obj.active_material

    try:
        if mat:
            img = mat.active_texture
            for f in mesh.polygons:
                if not is_editmode or f.select:
                    uvtex.data[f.index].image = img.image
        else:
            img = None
    except:
        pass

    # Back to EDIT Mode
    if is_editmode:
        bpy.ops.object.mode_set(mode='EDIT', toggle=False)


def box_map():
    # print('** Boxmap **')
    global all_scale_def, x_offset_def, y_offset_def, z_offset_def, x_rot_def, y_rot_def, z_rot_def, tex_aspect
    obj = bpy.context.active_object
    mesh = obj.data

    is_editmode = (obj.mode == 'EDIT')

    # if in EDIT Mode switch to OBJECT
    if is_editmode:
        bpy.ops.object.mode_set(mode='OBJECT', toggle=False)

    # if no UVtex - create it
    if not mesh.uv_textures:
        uvtex = bpy.ops.mesh.uv_texture_add()
    uvtex = mesh.uv_textures.active
    # uvtex.active_render = True

    img = None
    aspect = 1.0
    mat = obj.active_material
    try:
        if mat:
            img = mat.active_texture
            aspect = img.image.size[0] / img.image.size[1]
    except:
        pass
    aspect = aspect * tex_aspect

    #
    # Main action
    #
    if all_scale_def:
        sc = 1.0 / all_scale_def
    else:
        sc = 1.0

    sx = 1 * sc
    sy = 1 * sc
    sz = 1 * sc
    ofx = x_offset_def
    ofy = y_offset_def
    ofz = z_offset_def
    rx = x_rot_def / 180 * pi
    ry = y_rot_def / 180 * pi
    rz = z_rot_def / 180 * pi

    crx = cos(rx)
    srx = sin(rx)
    cry = cos(ry)
    sry = sin(ry)
    crz = cos(rz)
    srz = sin(rz)
    ofycrx = ofy * crx
    ofzsrx = ofz * srx

    ofysrx = ofy * srx
    ofzcrx = ofz * crx

    ofxcry = ofx * cry
    ofzsry = ofz * sry

    ofxsry = ofx * sry
    ofzcry = ofz * cry

    ofxcrz = ofx * crz
    ofysrz = ofy * srz

    ofxsrz = ofx * srz
    ofycrz = ofy * crz

    # uvs = mesh.uv_loop_layers[mesh.uv_loop_layers.active_index].data
    uvs = mesh.uv_layers.active.data
    for i, pol in enumerate(mesh.polygons):
        if not is_editmode or mesh.polygons[i].select:
            for j, loop in enumerate(mesh.polygons[i].loop_indices):
                v_idx = mesh.loops[loop].vertex_index
                # print('before[%s]:' % v_idx)
                # print(uvs[loop].uv)
                n = mesh.polygons[i].normal
                co = mesh.vertices[v_idx].co
                x = co.x * sx
                y = co.y * sy
                z = co.z * sz
                if abs(n[0]) > abs(n[1]) and abs(n[0]) > abs(n[2]):
                    # X
                    if n[0] >= 0:
                        uvs[loop].uv[0] = y * crx + z * srx - ofycrx - ofzsrx
                        uvs[loop].uv[1] = -y * aspect * srx + z * aspect * crx + ofysrx - ofzcrx
                    else:
                        uvs[loop].uv[0] = -y * crx + z * srx + ofycrx - ofzsrx
                        uvs[loop].uv[1] = y * aspect * srx + z * aspect * crx - ofysrx - ofzcrx
                elif abs(n[1]) > abs(n[0]) and abs(n[1]) > abs(n[2]):
                    # Y
                    if n[1] >= 0:
                        uvs[loop].uv[0] = -x * cry + z * sry + ofxcry - ofzsry
                        uvs[loop].uv[1] = x * aspect * sry + z * aspect * cry - ofxsry - ofzcry
                    else:
                        uvs[loop].uv[0] = x * cry + z * sry - ofxcry - ofzsry
                        uvs[loop].uv[1] = -x * aspect * sry + z * aspect * cry + ofxsry - ofzcry
                else:
                    # Z
                    if n[2] >= 0:
                        uvs[loop].uv[0] = x * crz + y * srz + - ofxcrz - ofysrz
                        uvs[loop].uv[1] = -x * aspect * srz + y * aspect * crz + ofxsrz - ofycrz
                    else:
                        uvs[loop].uv[0] = -y * srz - x * crz + ofxcrz - ofysrz
                        uvs[loop].uv[1] = y * aspect * crz - x * aspect * srz - ofxsrz - ofycrz

    # Back to EDIT Mode
    if is_editmode:
        bpy.ops.object.mode_set(mode='EDIT', toggle=False)


# Best Planar Mapping
def best_planar_map():
    global all_scale_def, xoffset_def, yoffset_def, zrot_def, tex_aspect

    obj = bpy.context.active_object
    mesh = obj.data

    is_editmode = (obj.mode == 'EDIT')

    # if in EDIT Mode switch to OBJECT
    if is_editmode:
        bpy.ops.object.mode_set(mode='OBJECT', toggle=False)

    # if no UVtex - create it
    if not mesh.uv_textures:
        uvtex = bpy.ops.mesh.uv_texture_add()
    uvtex = mesh.uv_textures.active
    # uvtex.active_render = True

    img = None
    aspect = 1.0
    mat = obj.active_material
    try:
        if mat:
            img = mat.active_texture
            aspect = img.image.size[0] / img.image.size[1]
    except:
        pass
    aspect = aspect * tex_aspect

    #
    # Main action
    #
    if all_scale_def:
        sc = 1.0 / all_scale_def
    else:
        sc = 1.0

        # Calculate Average Normal
    v = Vector((0, 0, 0))
    cnt = 0
    for f in mesh.polygons:
        if f.select:
            cnt += 1
            v = v + f.normal

    zv = Vector((0, 0, 1))
    q = v.rotation_difference(zv)

    sx = 1 * sc
    sy = 1 * sc
    sz = 1 * sc
    ofx = xoffset_def
    ofy = yoffset_def
    rz = zrot_def / 180 * pi

    cosrz = cos(rz)
    sinrz = sin(rz)

    # uvs = mesh.uv_loop_layers[mesh.uv_loop_layers.active_index].data
    uvs = mesh.uv_layers.active.data
    for i, pol in enumerate(mesh.polygons):
        if not is_editmode or mesh.polygons[i].select:
            for j, loop in enumerate(mesh.polygons[i].loop_indices):
                v_idx = mesh.loops[loop].vertex_index

                n = pol.normal
                co = q * mesh.vertices[v_idx].co
                x = co.x * sx
                y = co.y * sy
                z = co.z * sz
                uvs[loop].uv[0] = x * cosrz - y * sinrz + xoffset_def
                uvs[loop].uv[1] = aspect * (- x * sinrz - y * cosrz) + yoffset_def

    # Back to EDIT Mode
    if is_editmode:
        bpy.ops.object.mode_set(mode='EDIT', toggle=False)


class SureUVWOperator(bpy.types.Operator):
    bl_idname = "object.sureuvw_operator"
    bl_label = "Sure UVW Map"
    bl_space_type = "PROPERTIES"
    bl_region_type = "WINDOW"
    bl_context = "data"

    bl_options = {'REGISTER', 'UNDO'}

    action = StringProperty()

    size = FloatProperty(name="Size", default=1.0, precision=4)
    rot = FloatVectorProperty(name="XYZ Rotation")
    offset = FloatVectorProperty(name="XYZ offset", precision=4)

    zrot = FloatProperty(name="Z rotation", default=0.0)
    xoffset = FloatProperty(name="X offset", default=0.0, precision=4)
    yoffset = FloatProperty(name="Y offset", default=0.0, precision=4)
    texaspect = FloatProperty(name="Texture aspect", default=1.0, precision=4)

    flag90 = BoolProperty()
    flag90ccw = BoolProperty()

    @classmethod
    def poll(cls, context):
        obj = context.active_object
        return (obj and obj.type == 'MESH')

    def execute(self, context):
        # print('** execute **')
        # print(self.action)
        global all_scale_def, x_offset_def, y_offset_def, z_offset_def, x_rot_def, y_rot_def, z_rot_def, xoffset_def, yoffset_def, zrot_def, tex_aspect

        all_scale_def = self.size
        tex_aspect = self.texaspect

        x_offset_def = self.offset[0]
        y_offset_def = self.offset[1]
        z_offset_def = self.offset[2]
        x_rot_def = self.rot[0]
        y_rot_def = self.rot[1]
        z_rot_def = self.rot[2]

        xoffset_def = self.xoffset
        yoffset_def = self.yoffset
        zrot_def = self.zrot

        if self.flag90:
            self.zrot += 90
            zrot_def += 90
            self.flag90 = False

        if self.flag90ccw:
            self.zrot += -90
            zrot_def += -90
            self.flag90ccw = False

        if self.action == 'bestplanar':
            best_planar_map()
        elif self.action == 'box':
            box_map()
        elif self.action == 'showtex':
            show_texture()
        elif self.action == 'doneplanar':
            best_planar_map()
        elif self.action == 'donebox':
            box_map()

        # print('finish execute')
        return {'FINISHED'}

    def invoke(self, context, event):
        # print('** invoke **')
        # print(self.action)
        global all_scale_def, x_offset_def, y_offset_def, z_offset_def, x_rot_def, y_rot_def, z_rot_def, xoffset_def, yoffset_def, zrot_def, tex_aspect

        self.size = all_scale_def
        self.texaspect = tex_aspect
        self.offset[0] = x_offset_def
        self.offset[1] = y_offset_def
        self.offset[2] = z_offset_def
        self.rot[0] = x_rot_def
        self.rot[1] = y_rot_def
        self.rot[2] = z_rot_def

        self.xoffset = xoffset_def
        self.yoffset = yoffset_def
        self.zrot = zrot_def

        if self.action == 'bestplanar':
            best_planar_map()
        elif self.action == 'box':
            box_map()
        elif self.action == 'showtex':
            show_texture()
        elif self.action == 'doneplanar':
            best_planar_map()
        elif self.action == 'donebox':
            box_map()

        # print('finish invoke')
        return {'FINISHED'}

    def draw(self, context):
        if self.action == 'bestplanar' or self.action == 'rotatecw' or self.action == 'rotateccw':
            self.action = 'bestplanar'
            layout = self.layout
            layout.label("Size - " + self.action)
            layout.prop(self, 'size', text="")
            layout.label("Z rotation")
            col = layout.column()
            col.prop(self, 'zrot', text="")
            row = layout.row()
            row.prop(self, 'flag90ccw', text="-90 (CCW)")
            row.prop(self, 'flag90', text="+90 (CW)")
            layout.label("XY offset")
            col = layout.column()
            col.prop(self, 'xoffset', text="")
            col.prop(self, 'yoffset', text="")

            layout.label("Texture aspect")
            layout.prop(self, 'texaspect', text="")

            # layout.prop(self,'preview_flag', text="Interactive Preview")
            # layout.operator("object.sureuvw_operator",text="Done").action='doneplanar'

        elif self.action == 'box':
            layout = self.layout
            layout.label("Size")
            layout.prop(self, 'size', text="")
            layout.label("XYZ rotation")
            col = layout.column()
            col.prop(self, 'rot', text="")
            layout.label("XYZ offset")
            col = layout.column()
            col.prop(self, 'offset', text="")
            layout.label("Texture squash (optional)")
            layout.label("Always must be 1.0 !!!")
            layout.prop(self, 'texaspect', text="")

            # layout.prop(self,'preview_flag', text="Interactive Preview")
            # layout.operator("object.sureuvw_operator",text="Done").action='donebox'


# -------------- END --- Sure UVW Map v.0.5.1 ---------
# -----------

# ------------------ Bargool_1D_tools

def is_multiuser(obj):
    """ Test for instances """
    return hasattr(obj.data, 'users') and obj.data.users > 1


def filter_named_data(items):
    return [o for o in items if hasattr(o.data, 'name')]


def drop_selection(scene):
    for o in scene.objects:
        o.select = False


def find_instances(obj, context):
    """ Finds instances of object obj """
    if not hasattr(obj.data, 'name'):
        return
    mesh_name = obj.data.name
    for o in filter_named_data(context.scene.objects):
        if o.data.name == mesh_name:
            yield o


def create_instance(obj, scene):
    """ Creates instance of obj """
    duplicated = obj.copy()
    scene.objects.link(duplicated)
    return duplicated


def compare_notstrict_list_order(list_1, list_2):
    count = 0
    _list_1 = set(list_1)
    for element in _list_1:
        count += list_2.count(element)
    return len(list_1) == count == len(list_2)


class BTBatchOperatorMixin(object):
    """
    Abstract base class for batch processing objects
    Inheritors must define:
        filter_object method to define what objects to process
        process_object method to define what to do with each object
    This mixin is for use in batch_operator_factory, because most of operators
    just filter some objects and make simple things with them
    """
    __metaclass__ = ABCMeta

    bl_options = {'REGISTER', 'UNDO'}

    use_only_selected_objects = True
    context = None

    def get_use_selected_objects(self):
        return self.use_only_selected_objects

    def execute(self, context):
        """
        Template method pattern
        Must override filter_object, process_object and pre_process_objects
        """
        self.context = context
        # Select and filter objects
        self.selected_objects = context.selected_objects[:]
        self.active_object = context.active_object
        if self.get_use_selected_objects():
            self.objects = context.selected_objects
        else:
            drop_selection(context.scene)
            self.objects = context.scene.objects
        self.pre_filter_objects()
        self.work_objects = [obj for obj in self.objects if self.filter_object(obj)]
        # Cache old active object. At the end we will return activeness
        old_active = bpy.context.scene.objects.active
        for obj in self.work_objects:
            # As I understood, objects for bpy.ops operators must be
            # active in most cases
            bpy.context.scene.objects.active = obj
            # Fight!
            self.process_object(obj)
        bpy.context.scene.objects.active = old_active
        self.post_process_objects()
        return {'FINISHED'}

    def filter_object(self, obj):
        return True

    @abstractmethod
    def process_object(self, obj):
        raise NotImplementedError

    def pre_filter_objects(self):
        pass

    def post_process_objects(self):
        pass


class BTSelectInstancesOperator(bpy.types.Operator):
    bl_idname = 'paul.select_instances'
    # Double "II" just for quick "space" start of operator (space -> "ii", an there is operator)
    bl_label = 'Select IInstances 1D_Scripts'
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return len(context.selected_objects) > 0

    def execute(self, context):
        scene = context.scene
        possible_types = ['MESH', 'CURVE']
        native_selected_objects = filter_named_data(context.selected_objects)
        total_selected_objects = 0
        total_instances = 0
        total_unique = 0
        for _type in possible_types:
            selected_objects = native_selected_objects.copy()
            mesh_names = set([o.data.name for o in selected_objects if o.type == _type])
            objects_to_select = [obj for obj in filter_named_data(scene.objects) if obj.data.name in mesh_names and \
                                 obj.type == _type]

            total_selected_objects += len(objects_to_select)
            total_instances += len(mesh_names)
            mesh_names_to_select = [o.data.name for o in objects_to_select]
            total_unique += len([name for name in mesh_names if mesh_names_to_select.count(name) == 1])
            for obj in objects_to_select:
                obj.select = True

        message = "{} selected, {} inst, {} unique".format(total_selected_objects, total_instances, total_unique)
        self.report({'INFO'}, message)
        scene['report'] = message
        return {'FINISHED'}


class BTFilterInstancesOperator(BTBatchOperatorMixin, bpy.types.Operator):
    bl_idname = 'paul.filter_instances'
    # Double "III" just for quick "space" start of operator (space -> "iii", an there is operator)
    bl_label = 'Filter IIInstances 1D_Scripts'
    bl_options = {'REGISTER', 'UNDO'}

    use_only_selected_objects = False
    mesh_names = {}

    def pre_filter_objects(self):
        self.objects = filter_named_data(self.objects)
        self.mesh_names = set([o.data.name for o in filter_named_data(self.selected_objects)])

    def filter_object(self, obj):
        return obj.data.name in self.mesh_names and is_multiuser(obj)

    def process_object(self, obj):
        obj.select = True


class BTObjDistributeByXOperator(bpy.types.Operator):
    bl_idname = 'paul.obj_distribute_by_x'
    bl_label = 'Obj Distribute by X 1D_Scripts'
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return True if context.selected_objects else False

    def execute(self, context):
        # x = context.active_object.location[0]
        objs = sorted(context.selected_objects,
                      key=lambda o: sum(o.dimensions) / 3)
        x = objs[0].location[0]
        for obj in objs:
            obj.location[0] = x
            x += obj.dimensions[0] * 1.3
        return {'FINISHED'}


class BTObnameToMeshnameOperator(BTBatchOperatorMixin, bpy.types.Operator):
    bl_idname = 'paul.obname_to_meshname'
    bl_label = 'Obname to Meshname 1D_Scripts >'
    bl_description = 'Assigns object name to its meshname. Works with all selected objects'

    def process_object(self, obj):
        if obj.type != "EMPTY":
            obj.data.name = obj.name


class BTMeshnameToObnameOperator(BTBatchOperatorMixin, bpy.types.Operator):
    bl_idname = 'paul.meshname_to_obname'
    bl_label = 'Meshname to Obname 1D_Scripts <'
    bl_description = 'Assigns meshname to object name. Works with all selected objects'

    def process_object(self, obj):
        if obj.type != "EMPTY":
            obj.name = obj.data.name


class BTIsolateLayersOperator(bpy.types.Operator):
    bl_idname = 'paul.isolate_layers'
    bl_label = 'Isolate Layers 1D_Scripts'
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        selected_layers = [list(o.layers) for o in context.selected_objects]
        layers = map(lambda *x: any(x), *selected_layers)
        scene = context.scene
        scene.layers = list(layers)
        return {'FINISHED'}


class BTDropInstancesOperator(bpy.types.Operator):
    bl_idname = 'paul.drop_instances'
    bl_label = 'Drop Instances 1D_Scripts'
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        scene = context.scene
        acitive_object = context.active_object
        # object_layers = list(acitive_object.layers)
        matrices = [o.matrix_local for o in find_instances(acitive_object, context) if o.name != acitive_object.name]
        bpy.ops.mesh.separate()
        separated_object = scene.objects[0]
        # separated_object.layers = object_layers
        for m in matrices:
            duplicated = create_instance(separated_object, scene)
            duplicated.matrix_local = m

        return {'FINISHED'}


# __author__ = 'Aleksey Nakoryakov'


class BTBatchRemoverMixin(BTBatchOperatorMixin):
    """
    Base mixin for batch processing objects
    Inheritors must override:
        filter_object method to define what objects to process
        process_object method to define what to do with each object
    """

    class OPERATOR_TYPE_ENUM:
        do_select = 'DO_SELECT'
        do_remove = 'DO_REMOVE'

    operator_type = bpy.props.EnumProperty(items=((OPERATOR_TYPE_ENUM.do_remove,) * 3,
                                                  (OPERATOR_TYPE_ENUM.do_select,) * 3),
                                           options={'HIDDEN'})

    @classmethod
    def poll(cls, context):
        return (context.selected_objects or
                context.scene.batch_operator_settings.work_without_selection)

    def get_use_selected_objects(self):
        return not self.context.scene.batch_operator_settings.work_without_selection

    def pre_filter_objects(self):
        self.count = 0
        if self.get_use_selected_objects():
            drop_selection(self.context.scene)

    def process_object(self, obj):
        self.count += 1
        if self.operator_type == self.OPERATOR_TYPE_ENUM.do_remove:
            self.do_remove(obj)
        obj.select = True  # All you need is love!

    def post_process_objects(self):
        message = '{} {} properties'.format(
            'Removed' if self.operator_type == self.OPERATOR_TYPE_ENUM.do_remove else 'Selected',
            self.count
        )
        self.report({'INFO'}, message)

    def do_remove(self, obj):
        raise NotImplementedError


class BTBatchUVMapsEraserOperator(BTBatchRemoverMixin, bpy.types.Operator):
    bl_idname = 'object.uvmaps_eraser'
    bl_label = 'UV Maps Batch Remove'
    bl_description = 'Removes UV Maps from selected or all objects in scene'
    dropdown_name = 'UV Maps'

    def filter_object(self, obj):
        """ We need to remove uv_textures. So we need objects with them """
        # I didn't see blender yet, so I don't know what objects have textures
        # so just find them
        return hasattr(obj.data, 'uv_textures') and obj.data.uv_textures

    def do_remove(self, obj):
        count = 0
        while obj.data.uv_textures:
            bpy.ops.mesh.uv_texture_remove()
            count += 1
        return count


class BTBatchVertexGroupEraserOperator(BTBatchRemoverMixin, bpy.types.Operator):
    bl_idname = 'object.vertex_groups_eraser'
    bl_label = 'Vertex Groups Batch Remove'
    bl_description = 'Removes Vertex Groups from ' \
                     'selected or all objects in scene'
    dropdown_name = 'Vertex Groups'

    def filter_object(self, obj):
        has_groups = (hasattr(obj, 'vertex_groups') and
                      obj.vertex_groups)
        return has_groups

    def do_remove(self, obj):
        bpy.ops.object.vertex_group_remove(all=True)
        # We try to count removed items, so return something
        return 1


class BTBatchShapeKeysEraserOperator(BTBatchRemoverMixin, bpy.types.Operator):
    bl_idname = 'object.shape_keys_eraser'
    bl_label = 'Shape Keys Batch Remove'
    bl_description = 'Removes Shape Keys from selected or all objects in scene'
    dropdown_name = 'Shape Keys'

    def filter_object(self, obj):
        has_keys = hasattr(obj.data, 'shape_keys') and obj.data.shape_keys
        return True if has_keys else False

    def do_remove(self, obj):
        bpy.ops.object.shape_key_remove(all=True)
        # We try to count removed items, so return something
        return 1


class BTBatchVertexColorsEraserOperator(BTBatchRemoverMixin, bpy.types.Operator):
    bl_idname = 'object.vertex_colors_eraser'
    bl_label = 'Vertex Colors Batch Remove'
    bl_description = 'Removes VCols from selected or all objects in scene'
    dropdown_name = 'Vertex Colors'

    def filter_object(self, obj):
        has_colors = (hasattr(obj.data, 'vertex_colors') and
                      obj.data.vertex_colors)
        return True if has_colors else False

    def do_remove(self, obj):
        count = 0
        while obj.data.vertex_colors:
            for color in obj.data.vertex_colors:
                # Have to make vcolor active to remove it
                color.active = True
                bpy.ops.mesh.vertex_color_remove()
                # count is wrong because there is no guarantee that
                # vertex_color_remove tries to our active color
                count += 1
        return count


class BTBatchMaterialEraserOperator(BTBatchRemoverMixin, bpy.types.Operator):
    bl_idname = 'object.materials_eraser'
    bl_label = 'Materials Batch Remove'
    bl_description = 'Removes Materials from selected or all objects in scene'
    dropdown_name = 'Materials'

    def filter_object(self, obj):
        has_materials = hasattr(obj.data, 'materials') and obj.data.materials
        return True if has_materials else False

    def do_remove(self, obj):
        count = 0
        while obj.data.materials:
            bpy.ops.object.material_slot_remove()
            count += 1
        return count


class BTBatchGPencilEraserOperator(BTBatchRemoverMixin, bpy.types.Operator):
    bl_idname = 'object.gpencil_eraser'
    bl_label = 'GPencil Batch Remove'
    bl_description = 'Removes GPencils from selected or all objects in scene'
    dropdown_name = 'Grease Pencil'

    def filter_object(self, obj):
        has_materials = hasattr(obj, 'grease_pencil') and obj.grease_pencil
        return True if has_materials else False

    def do_remove(self, obj):
        count = 0
        while obj.grease_pencil:
            bpy.ops.gpencil.data_unlink()
            count += 1
        return count


class BTAllModifiersEraserOperator(BTBatchRemoverMixin, bpy.types.Operator):
    bl_idname = 'object.all_modifiers_eraser'
    bl_label = 'All Modifiers Batch Remove'
    bl_description = 'Removes All Modifiers from ' \
                     'selected or all objects in scene'
    dropdown_name = 'All Modifiers'

    def filter_object(self, obj):
        has_modifiers = hasattr(obj, 'modifiers') and obj.modifiers
        return True if has_modifiers else False

    def do_remove(self, obj):
        count = 0
        for modifier in obj.modifiers:
            bpy.ops.object.modifier_remove(modifier=modifier.name)
            count += 1
        return count


class BTAllSubsurfsEraserOperator(BTBatchRemoverMixin, bpy.types.Operator):
    bl_idname = 'object.all_subsurfs_eraser'
    bl_label = 'All Subsurfs Batch Remove'
    bl_description = 'Removes All Subsurfs from selected ' \
                     'or all objects in scene'
    dropdown_name = 'All Subsurfs'

    def filter_object(self, obj):
        has_modifiers = hasattr(obj, 'modifiers')
        if has_modifiers:
            has_subsurfs = len([m for m in obj.modifiers if m.type == 'SUBSURF']) > 0
            has_modifiers = has_modifiers and has_subsurfs
        return True if has_modifiers else False

    def do_remove(self, obj):
        count = 0
        subsurfs = [m for m in obj.modifiers if m.type == 'SUBSURF']
        for modifier in subsurfs:
            bpy.ops.object.modifier_remove(modifier=modifier.name)
            count += 1
        return count


class BTZeroSubsurfsEraserOperator(BTBatchRemoverMixin, bpy.types.Operator):
    bl_idname = 'object.zero_subsurfs_eraser'
    bl_label = 'Zero Subsurfs Batch Remove'
    bl_description = 'Removes Subsurfs with view 0 from ' \
                     'selected or all objects in scene'
    dropdown_name = 'Zero Subsurfs'

    def filter_object(self, obj):
        has_modifiers = hasattr(obj, 'modifiers')
        if has_modifiers:
            has_subsurfs = len([m for m in obj.modifiers
                                if m.type == 'SUBSURF' and m.levels == 0]) > 0
            has_modifiers = has_modifiers and has_subsurfs
        return True if has_modifiers else False

    def do_remove(self, obj):
        count = 0
        subsurfs = [m for m in obj.modifiers
                    if m.type == 'SUBSURF' and m.levels == 0]
        for modifier in subsurfs:
            bpy.ops.object.modifier_remove(modifier=modifier.name)
            count += 1
        return count


class BTEdgeSplitRemoverOperator(BTBatchRemoverMixin, bpy.types.Operator):
    bl_idname = 'object.edge_split_remover'
    bl_label = 'Edge Split Batch Remove/Select'
    bl_description = 'Removes/selects Edge Splits from selected or all objects in scene'
    dropdown_name = 'Edge Split'

    def filter_object(self, obj):
        has_modifiers = hasattr(obj, 'modifiers')
        return has_modifiers and any([m for m in obj.modifiers if m.type == 'EDGE_SPLIT'])

    def do_remove(self, obj):
        count = 0
        edge_splits = [m for m in obj.modifiers if m.type == 'EDGE_SPLIT']
        for modifier in edge_splits:
            bpy.ops.object.modifier_remove(modifier=modifier.name)
            count += 1
        return count


class BTMirrorMDFRemoverOperator(BTBatchRemoverMixin, bpy.types.Operator):
    bl_idname = 'object.mirror_mdf_remover'
    bl_label = 'Mirror modifier Batch Remove/Select'
    bl_description = 'Removes/selects Mirror modifier from selected or all objects in scene'
    dropdown_name = 'Mirror'

    def filter_object(self, obj):
        has_modifiers = hasattr(obj, 'modifiers')
        return has_modifiers and any([m for m in obj.modifiers if m.type == "MIRROR"])

    def do_remove(self, obj):
        count = 0
        mirrors = [m for m in obj.modifiers if m.type == 'MIRROR']
        for modifier in mirrors:
            bpy.ops.object.modifier_remove(modifier=modifier.name)
            count += 1


class BTMultipleUVMapsRemoverOperator(BTBatchRemoverMixin, bpy.types.Operator):
    bl_idname = 'object.multiple_uvmaps_remover'
    bl_label = 'Multiple UV Maps Batch Remove'
    bl_description = ('Removes all except active UV Maps from selected '
                      'or all objects in scene')
    dropdown_name = 'Multiple UV Maps'

    def filter_object(self, obj):
        return hasattr(obj.data, 'uv_textures') and len(obj.data.uv_textures) > 1

    def do_remove(self, obj):
        count = 0
        textures = obj.data.uv_textures
        textures.active_index = 0
        for _ in range(len(textures) - 1):
            if textures[textures.active_index].active_render:
                textures.active_index += 1
            bpy.ops.mesh.uv_texture_remove()
            count += 1
        return count


class BTBevelModifierRemoverOperator(BTBatchRemoverMixin, bpy.types.Operator):
    bl_idname = 'object.bevel_modifier_remover'
    bl_label = 'Bevel modifier Batch Remove'
    bl_description = ('Removes or selects Bevel modifiers from selected '
                      'or all objects in scene')
    dropdown_name = 'Bevel'

    modifier_type = 'BEVEL'

    def filter_object(self, obj):
        has_modifiers = hasattr(obj, 'modifiers')
        return has_modifiers and any([m for m in obj.modifiers if m.type == self.modifier_type])

    def do_remove(self, obj):
        count = 0
        bevels = [m for m in obj.modifiers if m.type == self.modifier_type]
        for modifier in bevels:
            bpy.ops.object.modifier_remove(modifier=modifier.name)
            count += 1


class BTEmptySlotsRemoverOperator(BTBatchRemoverMixin, bpy.types.Operator):
    bl_idname = 'object.empty_slots_remover'
    bl_label = 'Empty slots Batch Remove'
    bl_description = ('Removes empty slots or selects objects with empty slots '
                      'from selected or all objects in scene')
    dropdown_name = 'Empty material slots'

    def filter_object(self, obj):
        slots = getattr(obj, 'material_slots')
        return slots and any(s for s in slots if not s.material)

    def do_remove(self, obj):
        count = 0
        for idx in self._get_empty_index(obj):
            obj.active_material_index = idx
            bpy.ops.object.material_slot_select()
            bpy.ops.object.material_slot_remove()
        return count

    def _get_empty_index(self, obj):
        yield next(idx for idx, slot in enumerate(obj.material_slots) if not slot.material)


def create_panel_batch_remover(col, scene):
    col.operator(scene.batch_operator_settings.removers_dropdown,
                 text='Remove').operator_type = BTBatchRemoverMixin.OPERATOR_TYPE_ENUM.do_remove
    col.operator(scene.batch_operator_settings.removers_dropdown,
                 text='Select').operator_type = BTBatchRemoverMixin.OPERATOR_TYPE_ENUM.do_select
    col.prop(scene.batch_operator_settings, 'removers_dropdown',
             text='Action')
    col.prop(scene.batch_operator_settings, 'work_without_selection')


def get_description(operator):
    """ Gets description from operator, if exists """
    return hasattr(operator, 'bl_description') and operator.bl_description


class BatchOperatorSettings(bpy.types.PropertyGroup):
    work_without_selection = bpy.props.BoolProperty(
        name='Whole scene',
        default=False,
        description='If set, batch erasers will '
                    'work with all objects without selection')

    # We need all subclasses of BatchRemoverMixin in one dropdown
    operators = [
        (op.bl_idname, op.dropdown_name, get_description(op))
        for op in sorted(BTBatchRemoverMixin.__subclasses__(), key=attrgetter('dropdown_name'))]

    removers_dropdown = bpy.props.EnumProperty(
        items=operators,
        name='Removers')

    # TODO: Extract this and next to another class. Just for verticals
    verticals_select_behaviour = bpy.props.EnumProperty(
        items=[
            ('Z All', 'All', 'Z All'),
            ('Z Up', 'Up', 'Z Up'),
            ('Z Down', 'Down', 'Z Down'),
            ('Z Between', 'Between', 'Z Between'),
            ('Z Level', 'Z Level', 'Z Level'),
        ],
        name='Options')

    select_global_limit = bpy.props.BoolProperty(name='Global limit',
                                                 default=True)

    import_cleanup_recalculate_normals = bpy.props.BoolProperty(
        name='Recalculate Normals', default=False)
    import_cleanup_apply_rotations = bpy.props.BoolProperty(
        name='Apply rotation', default=True)
    import_cleanup_remove_doubles = bpy.props.BoolProperty(
        name='Remove doubles', default=True)
    import_cleanup_remove_doubles_threshold = bpy.props.FloatProperty(
        name='threshold', default=0.001, precision=4,
        min=0.0001, max=10
    )
    import_cleanup_tris_to_quads = bpy.props.BoolProperty(
        name='Tris to quads', default=True)
    import_cleanup_tris_to_quads_limit = bpy.props.IntProperty(
        name='limit', default=60, min=0, max=360
    )
    import_cleanup_clear_custom_normals = bpy.props.BoolProperty(
        name='Clear custom normals',
        default=True,
    )
    import_cleanup_reveal_hidden = bpy.props.BoolProperty(
        name='Reveal hidden',
        default=True,
    )
    import_cleanup_fix_double_faces = bpy.props.BoolProperty(
        name='Fix Double Faces',
        default=False,
    )
    import_cleanup_triangulate = bpy.props.BoolProperty(
        name='Triangulate',
        default=False,
    )
    geometry_inbound_only = bpy.props.BoolProperty(
        name='Inbound Only', default=True)

    do_triangulate_while_union = bpy.props.BoolProperty(name='Do triangulate',
                                                        default=True)


class TestSettings:
    text = None
    slope_plane = None


class BatchPanelSettings(bpy.types.PropertyGroup):
    do_show_select_vertices = bpy.props.BoolProperty(default=False)
    do_show_remover = bpy.props.BoolProperty(default=False)
    do_show_cleanup = bpy.props.BoolProperty(default=False)
    do_show_misc = bpy.props.BoolProperty(default=False)
    do_show_instances_placement = bpy.props.BoolProperty(default=False)
    do_show_naming_tools = bpy.props.BoolProperty(default=False)
    do_show_slope_align = bpy.props.BoolProperty(default=False)


# ----------- END --- Bargool_1D_tools

# ----------- BEGIN --- Smart UV
def compare_loops(luv1, luv2):
    return luv1 == luv2 or abs(luv1.uv[0] - luv2.uv[0]) < 0.001 and \
           abs(luv1.uv[1] - luv2.uv[1]) < 0.001


def init_bm():
    bm = bmesh.from_edit_mesh(bpy.context.edit_object.data)
    bm.verts.ensure_lookup_table()
    bm.edges.ensure_lookup_table()
    bm.edges.index_update()
    bm.verts.index_update()

    return bm


def get_selected_loops(bm, uvl):
    ret = []
    for f in bm.faces:
        if f.hide:
            continue
        for l in f.loops:
            if l[uvl].select:
                ret.add(l.index)
    return ret


class UVLoop:
    uvl = None

    def __init__(self, loop):
        loop.tag = True
        self.loops = [loop]
        self.prev = None
        self.next = None
        for l in loop.vert.link_loops:
            if not l.tag and l[self.uvl].select and \
                    compare_loops(loop[self.uvl], l[self.uvl]):
                self.loops.append(l)
                l.tag = True

    @property
    def first(self):
        ret = self
        while ret.prev:
            ret = ret.prev

        return ret

    @property
    def vert(self):
        return self.loops[0].vert

    def co(self, uvl):
        return self.loops[0][self.uvl].uv

    def find_loop(self):
        uvl = self.uvl
        us = []
        for l in self.loops:
            ll = l.link_loop_next
            if not ll.tag and ll[uvl].select:
                us.append(UVLoop(ll))
            ll = l.link_loop_prev
            if not ll.tag and ll[uvl].select:
                us.append(UVLoop(ll))

        maxu = 1 if self.prev or self.next else 2
        if len(us) > maxu:
            return None

        if us:
            for u in us:
                if not self.prev:
                    self.prev = u
                    u.next = self
                elif not self.next:
                    self.next = u
                    u.prev = self
                else:
                    return False
                loop = u.find_loop()
                if not loop:
                    return False
            return True
        else:
            if self.prev or self.next:
                return True

        us.clear()
        return False


def get_uv_edge_loops(bm, uvl):
    ret = []
    us = []
    UVLoop.uvl = uvl

    for v in bm.verts:
        for l in v.link_loops:
            l.tag = False

    for v in bm.verts:
        if v.hide or not v.select:
            continue

        us.clear()
        for l in v.link_loops:
            if not l.tag and l[uvl].select:
                us.append(UVLoop(l))

        for u in us:
            loop = u.find_loop()
            if loop:
                ret.append(u)

    return ret


def is_linked(l1s, l2):
    for l1 in l1s:
        if l1.link_loop_next == l2 or l1.link_loop_prev == l2:
            return True
    return False


def get_uv_loops(bm, uvl, loop):
    ret = []
    for i, l in enumerate(bm.verts[loop[0]].link_loops):
        if i == 0:
            ret.append([[l]])
            continue

        added = False
        for uv_loop in ret:
            if compare_loops(uv_loop[0][0][uvl], l[uvl]):
                uv_loop[0].append(l)
                added = True

        if not added:
            ret.append([[l]])

    for i, vi in enumerate(loop):
        if i == 0:
            continue

        v = bm.verts[vi]
        for l in v.link_loops:
            l.tag = False
        for uv_loop in ret:
            added = False
            for l in v.link_loops:
                if l.tag:
                    continue
                if is_linked(uv_loop[i - 1], l):
                    uv_loop.append([l])
                    added = True
                    l.tag = True
                    break

            if not added:
                return None

        for l in v.link_loops:
            added = False
            for uv_loop in ret:
                uv_loop[i]
                if uv_loop[i][0] == l:
                    added = True
                    continue
                if compare_loops(uv_loop[i][0][uvl], l[uvl]):
                    uv_loop[i].append(l)
                    added = True
                    break

            if not added:
                return None

    return ret


class SUV_OT_spreads(bpy.types.Operator):
    bl_idname = "suv.spreads"
    bl_label = "Spread Loop"

    @classmethod
    def poll(self, context):
        ao = context.active_object
        return ao and ao.type == 'MESH'

    def execute(self, context):
        bm = init_bm()
        uvl = bm.loops.layers.uv.verify()

        us = get_uv_edge_loops(bm, uvl)

        for u in us:
            edge_lengths = []
            edge_loop_length = 0
            prev_v = None

            count = 0
            u = u.first
            while True:
                count += 1
                if not u.next:
                    break
                u = u.next

            ul = u
            uf = u = u.first
            u = u.next
            for i in range(count):
                v1uv = u.loops[0][uvl].uv
                v2uv = uf.loops[0][uvl].uv
                u0 = v1uv[0]
                v0 = v1uv[1]
                du = v2uv[0] - v1uv[0]
                dv = v2uv[1] - v1uv[1]
                edge_length = sqrt(du ** 2 + dv ** 2)
                edge_lengths.append(edge_length)
                edge_loop_length += edge_length
                uf = u

                if not u.next:
                    break
                u = u.next

            ul = u
            uf = u = u.first
            v1uv = u.loops[0][uvl].uv
            v2uv = ul.loops[0][uvl].uv
            u0 = v1uv[0]
            v0 = v1uv[1]
            du = v2uv[0] - v1uv[0]
            dv = v2uv[1] - v1uv[1]

            for l in u.loops:
                l = l[uvl]
                l.uv[0] = u0
                l.uv[1] = v0

            u0 = l.uv[0]
            v0 = l.uv[1]
            u = u.next

            for i in range(count):
                if u == ul: i = len(edge_lengths) - 1
                v = u.vert
                for l in u.loops:
                    l = l[uvl]
                    l.uv[0] = u0 - edge_lengths[i]
                    l.uv[1] = v0
                u0 = l.uv[0]
                v0 = l.uv[1]

                if not u.next:
                    break
                u = u.next

        bmesh.update_edit_mesh(context.object.data, False, False)
        return {'FINISHED'}


# ----------- END --- Smart UV


# -----------------

# ----------- Nikita Akimov: 1d_timeline_render ------
# ----------- BEGIN -------------------

class NATimeLineRender:
    frames = []
    currentframe = None

    @staticmethod
    def startrender(context):
        print('-- TimeLineRender: STARTED --')
        __class__.clear()
        __class__.getframestorender()
        if __class__.frames:
            __class__.rendernextframe(context)
        else:
            __class__.clear()
            print('-- TimeLineRender: NO FRAMES TO RENDER --')

    @staticmethod
    def rendernextframe(context):
        if __class__.frames:
            __class__.currentframe = __class__.frames.pop()
            __class__.setframetorender(context, __class__.currentframe)
            if __class__.onrenderfinished not in bpy.app.handlers.render_complete:
                bpy.app.handlers.render_complete.append(__class__.onrenderfinished)
            if __class__.onrendercancel not in bpy.app.handlers.render_cancel:
                bpy.app.handlers.render_cancel.append(__class__.onrendercancel)
            if __class__.onsceneupdate_startrender not in bpy.app.handlers.scene_update_post:
                bpy.app.handlers.scene_update_post.append(__class__.onsceneupdate_startrender)
        else:
            __class__.clear()
            print('-- TimeLineRender: FINISHED --')

    @staticmethod
    def setframetorender(context, frame):
        context.screen.scene.frame_current = frame

    @staticmethod
    def getframestorender():
        if NATimeLineRenderOptions.textblockname in bpy.data.texts:
            line = bpy.data.texts[NATimeLineRenderOptions.textblockname].lines[0].body
            if line:
                linearr = line.split(NATimeLineRenderOptions.framesdelimiter)
                linearrframes = [int(i) for i in linearr if NATimeLineRenderOptions.diapasonedelimiter not in i]
                linearrdiapasones = sum([list(range(int(i.split('-')[0]), int(i.split('-')[1]) + 1)) for i in linearr if
                                         NATimeLineRenderOptions.diapasonedelimiter in i], [])
                linearrframes.extend(linearrdiapasones)
                __class__.frames = list(set(linearrframes))

    @staticmethod
    def checktextblock(context):
        textblock = None
        textblockmode = None
        if NATimeLineRenderOptions.textblockname in bpy.data.texts:
            textblock = bpy.data.texts[NATimeLineRenderOptions.textblockname]
            textblockmode = 'OK'
        else:
            textblock = bpy.data.texts.new(name=NATimeLineRenderOptions.textblockname)
            textblock.from_string(NATimeLineRenderOptions.emptyshablon)
            textblock.name = NATimeLineRenderOptions.textblockname
            textblockmode = 'SAMPLE'
        if textblock:
            areatoshow = None
            for area in context.screen.areas:
                if area.type == 'TEXT_EDITOR':
                    areatoshow = area
            if not areatoshow:
                for area in context.screen.areas:
                    if area.type not in ['PROPERTIES', 'INFO', 'OUTLINER']:
                        areatoshow = area
                        break
            if areatoshow:
                areatoshow.type = 'TEXT_EDITOR'
                areatoshow.spaces.active.text = textblock
                textblock.current_line_index = 0
        return textblockmode

    @staticmethod
    def saverenderrezult():
        destdir = __class__.destdir()
        if destdir:
            filename = NATimeLineRenderOptions.fileprefix + '{:04}'.format(
                __class__.currentframe) + '.' + __class__.extension(bpy.context)
            filepath = os.path.join(destdir, filename)
            for currentarea in bpy.context.window_manager.windows[0].screen.areas:
                if currentarea.type == 'IMAGE_EDITOR':
                    overridearea = bpy.context.copy()
                    overridearea['area'] = currentarea
                    bpy.ops.image.save_as(overridearea, copy=True, filepath=filepath)
                    print('-- TimeLineRender: FINISHED RENDER FRAME ', __class__.currentframe, ' --')
                    break
        else:
            print('TimeLineRender: Error - no destination directory')

    @staticmethod
    def destdir():
        dir = None
        if bpy.data.filepath:
            dir = os.path.join(os.path.dirname(bpy.data.filepath),
                               os.path.splitext(os.path.basename(bpy.data.filepath))[0])
        else:
            dir = os.path.join(os.path.dirname(bpy.context.user_preferences.filepaths.temporary_directory),
                               'TimeLineRender')
        return dir

    @staticmethod
    def extension(context):
        extensions = {'JPEG': 'jpg', 'PNG': 'png'}
        return extensions[context.scene.render.image_settings.file_format]

    @staticmethod
    def clear():
        __class__.frames = []
        __class__.currentframe = None
        if __class__.onrenderfinished in bpy.app.handlers.render_complete:
            bpy.app.handlers.render_complete.remove(__class__.onrenderfinished)
        if __class__.onrendercancel in bpy.app.handlers.render_cancel:
            bpy.app.handlers.render_cancel.remove(__class__.onrendercancel)
        if __class__.onsceneupdate_startrender in bpy.app.handlers.scene_update_post:
            bpy.app.handlers.scene_update_post.remove(__class__.onsceneupdate_startrender)
        if __class__.onsceneupdate_saverender in bpy.app.handlers.scene_update_post:
            bpy.app.handlers.scene_update_post.remove(__class__.onsceneupdate_saverender)

    @staticmethod
    def onsceneupdate_startrender(scene):
        # start render on scene update
        if __class__.onsceneupdate_startrender in bpy.app.handlers.scene_update_post:
            bpy.app.handlers.scene_update_post.remove(__class__.onsceneupdate_startrender)
        status = bpy.ops.render.render('INVOKE_DEFAULT')
        if status == {'CANCELLED'}:
            if __class__.onsceneupdate_startrender not in bpy.app.handlers.scene_update_post:
                bpy.app.handlers.scene_update_post.append(__class__.onsceneupdate_startrender)

    @staticmethod
    def onsceneupdate_saverender(scene):
        # save render rezult on scene update
        if __class__.onsceneupdate_saverender in bpy.app.handlers.scene_update_post:
            bpy.app.handlers.scene_update_post.remove(__class__.onsceneupdate_saverender)
        __class__.saverenderrezult()
        # and start next render
        __class__.rendernextframe(bpy.context)

    @staticmethod
    def onrenderfinished(scene):
        # render finished - save render result on next scene update
        if __class__.onsceneupdate_saverender not in bpy.app.handlers.scene_update_post:
            bpy.app.handlers.scene_update_post.append(__class__.onsceneupdate_saverender)

    @staticmethod
    def onrendercancel(scene):
        # render aborted
        __class__.clear()
        print('-- TimeLineRender: ABORTED BY USER --')


class NATimeLineRenderOptions:
    textblockname = 'TimeLineRender.txt'
    emptyshablon = '1,2,7-9,4\n# В первой строке указываются номера и диапазоны кадров для рендера'
    framesdelimiter = ','
    diapasonedelimiter = '-'
    fileprefix = 'TR_'


class NATimeLineRenderStart(bpy.types.Operator):
    bl_idname = 'timelinerender.start'
    bl_label = 'Start TimeLineRender'
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        render = NATimeLineRender.checktextblock(context)
        if render == 'OK':
            NATimeLineRender.startrender(context)
        return {'FINISHED'}


# ------------- END -- Nikita Akimov: 1d_timeline_render

# ------------- START ----- nikitron.cc.ua: Camswitch

class NGD1_camswitch(bpy.types.Operator):
    """
    Следующая и предыдущая камера в сцене.
    next & previous camera in ther scene.
    """
    bl_idname = "scene.camswitch"
    bl_label = "Camswitch D1"
    bl_options = {'REGISTER', 'UNDO'}

    next = bpy.props.BoolProperty(name='next', default=True)

    def execute(self, context):
        cams = [k for k in bpy.data.objects if k.type == 'CAMERA']
        print(cams)
        active = bpy.data.scenes[bpy.context.scene.name].camera
        for i, k in enumerate(cams):
            if self.next:
                if k == active and i < (len(cams) - 1):
                    bpy.data.scenes[bpy.context.scene.name].camera = bpy.data.objects[cams[i + 1].name]
                    bpy.context.scene.objects.active = bpy.data.objects[cams[i + 1].name]
                    bpy.data.objects[cams[i + 1].name].select = True
                    break
                elif k == active:
                    bpy.data.scenes[bpy.context.scene.name].camera = bpy.data.objects[cams[0].name]
                    bpy.context.scene.objects.active = bpy.data.objects[cams[0].name]
                    bpy.data.objects[cams[0].name].select = True
                    break
            else:
                if k == active and i > 0:
                    bpy.data.scenes[bpy.context.scene.name].camera = bpy.data.objects[cams[i - 1].name]
                    bpy.context.scene.objects.active = bpy.data.objects[cams[i - 1].name]
                    bpy.data.objects[cams[i - 1].name].select = True
                    break
                elif k == active:
                    bpy.data.scenes[bpy.context.scene.name].camera = bpy.data.objects[cams[-1].name]
                    bpy.context.scene.objects.active = bpy.data.objects[cams[-1].name]
                    bpy.data.objects[cams[-1].name].select = True
                    break
        return {'FINISHED'}


# ------------- END --------- nikitron.cc.ua: Camswitch

# ----------- BEGIN ------- Andrey Menshikov, from AM_1D_Scripts
def crossSplit(func):
    """decorator for splitting edges in 2D/3D"""

    def run(self, context):

        obj = bpy.context.object
        me = obj.data
        bm = bmesh.from_edit_mesh(me)

        b_edges = tuple(bm.edges)
        edges = [b_edges[e.index] for e in bm.edges if e.select]
        if len(b_edges) < 2:
            bpy.context.tool_settings.mesh_select_mode = True, True, True
            return {"FINISHED"}

        edges_split = [[] for e in edges]

        # intersect all edges
        for i, edge_1 in enumerate(edges):
            for j, edge_2 in enumerate(edges[i + 1:], start=i + 1):

                point = func(self, edge_1.verts[0].co, edge_1.verts[1].co, edge_2.verts[0].co, edge_2.verts[1].co,
                             context)

                if point:
                    for position, point_data in zip((i, j), point):
                        if 0 < point_data < 1:
                            edges_split[position].append(point_data)

        # set points
        for edge, percents in zip(edges, edges_split):

            vector = edge.verts[1].co - edge.verts[0].co
            point = edge.verts[0].co

            geom_split = bmesh.ops.bisect_edges(bm, edges=[edge], cuts=len(percents))["geom_split"]
            vertices = [v for v in geom_split if isinstance(v, bmesh.types.BMVert)]
            vertices.sort(key=lambda v: (point - v.co).length)
            percents.sort()
            for vertex, percent in zip(vertices, percents):
                vertex.co = point + vector * percent

        bmesh.update_edit_mesh(me)
        bpy.context.tool_settings.mesh_select_mode = True, True, True
        return {"FINISHED"}

    return run


class AMCornerCross(bpy.types.Operator):
    """split edges in 2D projection on Z"""

    bl_idname = "paul.corner_cross"
    bl_label = "Corner Cross"
    bl_options = {'REGISTER', 'UNDO'}

    @crossSplit
    def execute(self, v1, v2, v3, v4, context):
        """find projection in 2D space"""

        config = bpy.context.window_manager.paul_manager

        v1 = mathutils.Vector((v1.x, v1.y))
        v2 = mathutils.Vector((v2.x, v2.y))
        v3 = mathutils.Vector((v3.x, v3.y))
        v4 = mathutils.Vector((v4.x, v4.y))

        point = mathutils.geometry.intersect_line_line_2d(v1, v2, v3, v4)
        if point is None:
            if config.corner_overlap:
                return None
            else:
                return self.findNonOverlap((v1, v2), (v3, v4))

        try:
            percent_1 = (point - v1).length / (v2 - v1).length
        except ZeroDivisionError:
            percent_1 = 0

        try:
            percent_2 = (point - v3).length / (v4 - v3).length
        except ZeroDivisionError:
            percent_2 = 0

        return percent_1, percent_2

    @staticmethod
    def findNonOverlap(line1, line2):
        """find projection without overlap"""

        xdiff = (line1[0].x - line1[1].x, line2[0].x - line2[1].x)
        ydiff = (line1[0].y - line1[1].y, line2[0].y - line2[1].y)

        def det(a, b):
            return a[0] * b[1] - a[1] * b[0]

        div = det(xdiff, ydiff)
        if div == 0:
            return None

        d = det(*line1), det(*line2)
        x = det(d, xdiff) / div
        y = det(d, ydiff) / div

        point = mathutils.Vector((x, y))
        v1 = line1[1] - line1[0]

        try:
            param_1 = (point - line1[0]) * v1 / v1.length / v1.length
        except ZeroDivisionError:
            param_1 = 0

        v2 = line2[1] - line2[0]
        try:
            param_2 = (point - line2[0]) * v2 / v2.length / v2.length
        except ZeroDivisionError:
            param_2 = 0

        return param_1, param_2


class AMExtendCross(bpy.types.Operator):
    """split edges in 3D"""

    bl_idname = "paul.extend_cross"
    bl_label = "Extend Cross"
    bl_options = {'REGISTER', 'UNDO'}

    @crossSplit
    def execute(self, v1, v2, v3, v4, context):
        """find intersection in 3D"""

        config = bpy.context.window_manager.paul_manager

        try:
            p1, p2 = mathutils.geometry.intersect_line_line(v1, v2, v3, v4)
        except TypeError:
            return None

        vector_1 = v2 - v1
        try:
            percent_1 = (p1 - v1) * vector_1 / vector_1.length / vector_1.length
        except ZeroDivisionError:
            percent_1 = 0

        vector_2 = v4 - v3
        try:
            percent_2 = (p2 - v3) * vector_2 / vector_2.length / vector_2.length
        except ZeroDivisionError:
            percent_2 = 0

        if config.corner_overlap and not (0 < percent_1 < 1 and 0 < percent_2 < 1):
            return None
        return percent_1, percent_2


# ----------- END ------- Andrey Menshikov, from AM_1D_Scripts


def find_index_of_selected_vertex(mesh):
    selected_verts = [i.index for i in mesh.vertices if i.select]
    verts_selected = len(selected_verts)
    if verts_selected < 1:
        return None
    else:
        return selected_verts


def find_extreme_select_verts(mesh, verts_idx):
    res_vs = []
    edges = mesh.edges

    for v_idx in verts_idx:
        connecting_edges = [i for i in edges if v_idx in i.vertices[:] and i.select \
                            and i.vertices[0] in verts_idx and i.vertices[1] in verts_idx]
        if len(connecting_edges) == 1:
            res_vs.append(v_idx)
    return res_vs


def find_connected_verts_simple(me, found_index):
    edges = me.edges
    connecting_edges = [i for i in edges if found_index in i.vertices[:] and \
                        me.vertices[i.vertices[0]].select and me.vertices[i.vertices[1]].select]
    if len(connecting_edges) == 0:
        return []
    else:
        connected_verts = []
        for edge in connecting_edges:
            cvert = set(edge.vertices[:])
            cvert.remove(found_index)
            vert = cvert.pop()
            connected_verts.append(vert)
        return connected_verts


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


def find_all_connected_verts(me, active_v, not_list=[], step=0):
    vlist = [active_v]
    not_list.append(active_v)
    step += 1
    list_v_1 = find_connected_verts(me, active_v, not_list)

    for v in list_v_1:
        list_v_2 = find_all_connected_verts(me, v, not_list, step)
        vlist += list_v_2
    return vlist


def find_connected_verts_bm(bm, found_index, not_list):
    connecting_edges = bm.verts[found_index].link_edges

    if len(connecting_edges) == 0:
        return []
    else:
        connected_verts = []
        for edge in connecting_edges:
            cvert = set((edge.verts[0].index, edge.verts[1].index))
            cvert.remove(found_index)
            vert = cvert.pop()
            if not (vert in not_list) and bm.verts[vert].select:
                connected_verts.append(vert)
                not_list.append(vert)
        return connected_verts


def find_all_connected_verts_bm(bm, active_v, not_list=[]):
    result = [active_v]
    vlist = [active_v]
    if active_v not in not_list:
        not_list.append(active_v)

    list_v_1 = find_connected_verts_bm(bm, active_v, not_list)
    list_v_3 = []
    for list_v in list_v_1:
        list_v_2 = find_all_connected_verts_bm(bm, list_v, not_list)
        list_v_3.append(list_v_2)

    if list_v_3:
        result = list_v_3[0] + vlist
        if len(list_v_3) > 1:
            result = result + list(reversed(list_v_3[1]))

    return result


def find_dupes_verts(context, radius):
    bpy.ops.object.editmode_toggle()
    bpy.ops.object.editmode_toggle()

    ob = context.active_object
    mesh = ob.data

    bpy.ops.mesh.select_all(action='DESELECT')

    bm = bmesh.new()
    bm.from_mesh(mesh)

    doubs = bmesh.ops.find_doubles(bm, verts=bm.verts, dist=radius)

    bpy.ops.object.mode_set(mode='OBJECT')
    double_verts = doubs['targetmap']
    if len(double_verts.keys()) > 1:
        for k, v in double_verts.items():
            mesh.vertices[v.index].select = True

    mesh.update()
    bm.free()

    bpy.ops.object.mode_set(mode='EDIT')
    bpy.ops.mesh.select_mode(use_expand=True, type='VERT')
    context.tool_settings.mesh_select_mode = (True, False, False)
    return len(double_verts)


def find_all_segments(me, min_vts=3):
    # out: [[segment1], [segment2], ...]
    # editmode: VERTS
    edit_mode_vert = bpy.context.tool_settings.mesh_select_mode[0]
    edit_mode_edge = bpy.context.tool_settings.mesh_select_mode[1]
    if edit_mode_vert:
        # vertices = me.vertices
        l_sel_vi = find_index_of_selected_vertex(me)
        if not l_sel_vi: return False
        # avi = l_sel_vi[0]
        tmp_idx_vts = l_sel_vi.copy()
        segments = []
        upp = 100  # ограничение количества сегментов
        bl = []
        set_sel_vi = set(l_sel_vi)
        while tmp_idx_vts and upp > 0:
            upp -= 1
            act_vi = tmp_idx_vts[0]
            segment = find_all_connected_verts(me, act_vi, bl, 0)
            if len(segment) >= min_vts: segments.append(segment)
            tmp_idx_vts = list(set_sel_vi ^ set(bl))

        if upp < 1: return False

    elif edit_mode_edge:
        l_sel_edgs = [e for e in me.edges if e.select]
        if not l_sel_edgs: return False
        segments = []
        for e in l_sel_edgs:
            segment = [e.vertices[0], e.vertices[1]]
            segments.append(segment)

    else:
        return False

    return segments


def bm_vert_active_get(bm):
    for elem in reversed(bm.select_history):
        if isinstance(elem, (bmesh.types.BMVert, bmesh.types.BMEdge, bmesh.types.BMFace)):
            return elem.index, str(elem)[3:4]
    return None, None


def bm_edge_active_get(bm):
    for elem in reversed(bm.select_history):
        if isinstance(elem, bmesh.types.BMEdge):
            return elem.index
    return None


def to_store_coner(obj_name, bm, mode):
    config = bpy.context.window_manager.paul_manager
    active_edge, el = bm_vert_active_get(bm)
    old_name_c = config.object_name_store_c
    old_coner1 = config.coner_edge1_store
    old_coner2 = config.coner_edge2_store

    def check():
        if mode == 'EDIT_MESH' and \
                (old_name_c != config.object_name_store_c or \
                 old_coner1 != config.coner_edge1_store or \
                 old_coner2 != config.coner_edge2_store):
            config.flip_match = False

    if active_edge != None and el == 'E':
        mesh = bpy.data.objects[obj_name].data
        config.object_name_store_c = obj_name
        config.coner_edge1_store = active_edge
        verts = bm.edges[active_edge].verts
        v0 = verts[0].index
        v1 = verts[1].index
        edges_idx = [i.index for i in mesh.edges \
                     if (v1 in i.vertices[:] or v0 in i.vertices[:]) and i.select \
                     and i.index != active_edge]
        if edges_idx:
            config.coner_edge2_store = edges_idx[0]
            check()
            return True

    if active_edge != None and el == 'V':
        mesh = bpy.data.objects[obj_name].data
        config.object_name_store_c = obj_name

        v2_l = find_all_connected_verts(mesh, active_edge, [], 0)
        control_vs = find_connected_verts_simple(mesh, active_edge)
        if len(v2_l) > 2 and len(control_vs) == 1:
            v1 = v2_l.pop(1)
            edges_idx = []
            for v2 in v2_l[:2]:
                edges_idx.extend([i.index for i in mesh.edges \
                                  if v1 in i.vertices[:] and v2 in i.vertices[:]])

            if len(edges_idx) > 1:
                config.coner_edge1_store = edges_idx[0]
                config.coner_edge2_store = edges_idx[1]
                check()
                return True

    check()
    config.object_name_store_c = ''
    config.coner_edge1_store = -1
    config.coner_edge2_store = -1
    if mode == 'EDIT_MESH':
        config.flip_match = False
        print_error('Two edges is not detected')
        print('Error: align 05')
    return False


def to_store_vert(obj_name, bm):
    config = bpy.context.window_manager.paul_manager
    active_edge, el = bm_vert_active_get(bm)
    old_edge1 = config.active_edge1_store
    old_edge2 = config.active_edge2_store
    old_name_v = config.object_name_store_v

    def check():
        if old_name_v != config.object_name_store_v or \
                old_edge1 != config.active_edge1_store or \
                old_edge2 != config.active_edge2_store:
            config.flip_match = False

    if active_edge != None and el == 'E':
        mesh = bpy.data.objects[obj_name].data
        config.object_name_store_v = obj_name
        config.active_edge1_store = active_edge
        verts = bm.edges[active_edge].verts
        v0 = verts[0].index
        v1 = verts[1].index
        edges_idx = [i.index for i in mesh.edges \
                     if (v1 in i.vertices[:] or v0 in i.vertices[:]) and i.select \
                     and i.index != active_edge]
        if edges_idx:
            config.active_edge2_store = edges_idx[0]
            check()
            return True

    if active_edge != None and el == 'V':
        mesh = bpy.data.objects[obj_name].data
        config.object_name_store_v = obj_name

        v2_l = find_all_connected_verts(mesh, active_edge, [], 0)
        control_vs = find_connected_verts_simple(mesh, active_edge)
        if len(v2_l) > 2 and len(control_vs) == 1:
            v1 = v2_l.pop(1)
            edges_idx = []
            for v2 in v2_l[:2]:
                edges_idx.extend([i.index for i in mesh.edges \
                                  if v1 in i.vertices[:] and v2 in i.vertices[:]])

            if len(edges_idx) > 1:
                config.active_edge1_store = edges_idx[0]
                config.active_edge2_store = edges_idx[1]
                check()
                return True

    check()
    config.object_name_store_v = ''
    config.active_edge1_store = -1
    config.active_edge2_store = -1
    config.flip_match = False
    print_error('Side is undefined')
    print('Error: 3dmatch 10')
    return False


def to_store(obj_name, bm):
    config = bpy.context.window_manager.paul_manager
    active_edge, el = bm_vert_active_get(bm)
    if active_edge != None and el == 'E':
        config.object_name_store = obj_name
        config.edge_idx_store = active_edge
        verts = bm.edges[active_edge].verts
        config.vec_store = (verts[1].co - verts[0].co) * \
                           bpy.data.objects[obj_name].matrix_world.to_3x3().transposed()
        return True

    if active_edge != None and el == 'V':
        obj_act = bpy.context.active_object
        mesh = obj_act.data
        v2_l = find_index_of_selected_vertex(mesh)
        if len(v2_l) == 2:
            v1 = active_edge
            v2_l.pop(v2_l.index(v1))
            v2 = v2_l[0]
            edges_idx = [i.index for i in mesh.edges \
                         if v1 in i.vertices[:] and v2 in i.vertices[:]]

            if edges_idx:
                config.edge_idx_store = edges_idx[0]

            config.object_name_store = obj_name
            config.vec_store = (mesh.vertices[v1].co - mesh.vertices[v2].co) * \
                               bpy.data.objects[obj_name].matrix_world.to_3x3().transposed()
            return True

    config.object_name_store = ''
    config.edge_idx_store = -1
    config.vec_store = mathutils.Vector((0, 0, 0))
    print_error('Active edge is not detected')
    print('Error: align 02')
    return False


def sel_radius_verts(context, radius):
    bpy.ops.object.editmode_toggle()
    bpy.ops.object.editmode_toggle()

    ob = context.active_object
    mesh = ob.data

    points = [v.co for v in mesh.vertices if v.select]
    if not points:
        print_error2('No selected vertices', 'sel_radius_verts 01')
        return 0

    size = len(mesh.vertices)
    kd = mathutils.kdtree.KDTree(size)
    for i, p in enumerate(mesh.vertices):
        kd.insert(p.co, i)

    kd.balance()

    arr_idx = []
    for point in points:
        for (co, index, dist) in kd.find_range(point, radius):
            arr_idx.append(index)

    bpy.ops.object.mode_set(mode='OBJECT')
    for vi in arr_idx:
        mesh.vertices[vi].select = True

    bpy.ops.object.mode_set(mode='EDIT')
    arr_idx = set(arr_idx)
    return len(arr_idx) - len(points)


def select_mesh_rot(me, matrix):
    verts = [v for v in me.verts if v.select == True]
    for v in verts:
        v.co = v.co * matrix


def store_align(vts='edge', mode='EDIT_MESH'):
    bpy.ops.object.editmode_toggle()
    bpy.ops.object.editmode_toggle()

    obj = bpy.context.active_object
    mesh = obj.data
    bm = bmesh.new()
    bm.from_mesh(mesh)
    result = True
    check_lukap(bm)

    if vts == 'vert':
        result = to_store_vert(obj.name, bm)
    elif vts == 'edge':
        result = to_store(obj.name, bm)
    else:
        # vts=='coner':
        result = to_store_coner(obj.name, bm, mode)

    bm.free()
    return result


def StairsMaker(self=None):
    bpy.ops.object.mode_set(mode='OBJECT')
    bpy.ops.object.mode_set(mode='EDIT')

    obj = bpy.context.active_object
    mesh = obj.data

    # Найти верхнюю и нижнюю Z-координаты и вычислить dZ
    vcoz = [v.co.z for v in mesh.vertices if v.select]
    z_max = max(vcoz)
    z_min = min(vcoz)
    dZ = z_max - z_min

    # Определить количество лесенок (фейсов) Pc
    faces_selected = [f for f in mesh.polygons if f.select]
    Pc = len(faces_selected)

    # Вычисить высоту лесенок dZ/(Pc+1)=h0
    h0 = dZ / (Pc + 1)

    print_info("H/S = %.4f / %d = %.4f" % (dZ, Pc + 1, h0), self)

    # Построить лесенку
    bm = bmesh.new()
    bm.from_mesh(mesh)
    check_lukap(bm)

    lEdges_select_idx = [e.index for e in mesh.edges if e.select]
    lFaces_select = [p for p in mesh.polygons if p.select]
    lEdges_select = [mesh.edges[i] for i in lEdges_select_idx]

    def findNearestPols(pol, sel_pols):
        lEdges_ = [e for e in pol.edge_keys]
        lEdges = list(add(*zip(*lEdges_)))

        lEdges_pols = [p.edge_keys for p in sel_pols if p != pol]
        lEdges_sel_ = [e for e in lEdges_pols]
        tmp = list(*zip(*zip(lEdges_sel_)))
        tmp_ = []
        for line in tmp:
            tmp_.extend(line)

        lEdges_sel = list(add(*zip(*tmp_)))
        lNearest_pols = set(lEdges) & set(lEdges_sel)
        count = len(lNearest_pols)
        return count, list(lNearest_pols)

    def findNearestEdges(sel_pols, sel_edges):
        lEdges_sel_ = [p.edge_keys for p in sel_pols]
        lEdges_sel = []
        lEdges_for_sel = []
        sel_edges_ = [(e.vertices[0], e.vertices[1]) for e in sel_edges]
        sel_edges_.extend([(e.vertices[1], e.vertices[0]) for e in sel_edges])
        for te in lEdges_sel_:
            for e in te:
                if e in lEdges_sel and e in sel_edges_:
                    lEdges_for_sel.append(e)

            lEdges_sel.extend(te)

        lEdges_ = list(set(lEdges_for_sel))
        lEdges = [e.index for e in sel_edges if (e.vertices[0], e.vertices[1]) in lEdges_ or \
                  (e.vertices[1], e.vertices[0]) in lEdges_]
        return lEdges

    def memory_new_edge(v0, v1, lverts, ledges, base_vi):
        lverts.extend([v0, v1])
        ledges.append((base_vi, base_vi + 1))
        # base_vi += 2

    def memory_new_face(lverts, lfaces, base_vi):
        v0, v1, v2, v3 = base_vi - 2, base_vi - 1, base_vi + 1, base_vi
        dv01 = lverts[v0] - lverts[v1]
        dv32 = lverts[v3] - lverts[v2]
        if dv01 * dv32 < 0:
            v2, v3 = base_vi, base_vi + 1

        lfaces.append((v0, v1, v2, v3))

    def createMeshFromData(name, origin, verts, faces):
        # Создание меша и объекта
        bpy.ops.object.mode_set(mode='OBJECT')
        me = bpy.data.meshes.new(name + 'Mesh')
        ob = bpy.data.objects.new(name, me)
        ob.location = origin
        ob.show_name = True

        # Привязка объекта к сцене, он становится активным
        scn = bpy.context.scene
        scn.objects.link(ob)
        scn.objects.active = ob
        ob.select = True

        # Создание меша из полученных verts (вершин), faces (граней).
        me.from_pydata(verts, [], faces)
        # Обновление меша с новыми данными
        me.update()
        bpy.ops.object.mode_set(mode='EDIT')
        bpy.ops.mesh.normals_make_consistent(inside=False)
        return ob

    lEdgesAll = findNearestEdges(lFaces_select, lEdges_select)
    extr_pols = []
    for pol in lFaces_select:
        test, npls = findNearestPols(pol, lFaces_select)
        if test == 2:
            extr_pols.append(pol.index)
            continue

    if len(extr_pols) == 2:
        c0 = abs(mesh.polygons[extr_pols[0]].center.z - z_max)
        c1 = abs(mesh.polygons[extr_pols[1]].center.z - z_max)
        if c1 < c0: extr_pols.reverse()

        start_face = extr_pols[0]
        end_face = extr_pols[1]

        cener0 = abs((sum([v.co.z for v in bm.edges[lEdgesAll[0]].verts]) / 2) - z_max)
        cener1 = abs((sum([v.co.z for v in bm.edges[lEdgesAll[-1]].verts]) / 2) - z_max)
        if cener1 < cener0: lEdgesAll.reverse()

        verts_unpack_faces_ = [(e.verts[0], e.verts[1]) for e in bm.faces[start_face].edges]
        verts_unpack_faces = list(add(*zip(*verts_unpack_faces_)))  # [(,),(,)] -> [,,,]
        all_verts_ = [(e.verts[0], e.verts[1]) for e in [bm.edges[ei] for ei in lEdgesAll]]
        all_verts = list(add(*zip(*all_verts_)))  # [(,),(,)] -> [,,,]
        verts_start_edge = list(set(verts_unpack_faces) ^ set(all_verts))

        verts_end_edge = [v for v in bm.edges[lEdgesAll[-1]].verts]
        start_edge = [e for e in bm.faces[start_face].edges \
                      if e.verts[0] in verts_start_edge \
                      and e.verts[1] in verts_start_edge][0]

        end_edge = [e for e in bm.faces[end_face].edges \
                    if e.verts[0] not in verts_start_edge \
                    and e.verts[1] not in verts_start_edge][0]

        ## Сортируем список
        centre_edges = [(bm.edges[ei].verts[0].co + bm.edges[ei].verts[1].co) / 2 for ei in lEdgesAll]
        size = len(centre_edges)
        kd = mathutils.kdtree.KDTree(size)
        for i, p in enumerate(centre_edges):
            kd.insert(p, i)
        kd.balance()
        point = (start_edge.verts[0].co + start_edge.verts[1].co) / 2
        lEdgesAll_ = []
        for (co, index, dist) in kd.find_n(point, size):
            lEdgesAll_.append(lEdgesAll[index])
            edge_ = bm.edges[lEdgesAll[index]]

        lEdgesAll = lEdgesAll_

        ## lEdgesAll - упорядоченный список ребер сверху вниз
        top = z_max
        # base_vi = len(bm.verts)
        base_vi = 2
        ex_lEdgesAll = lEdgesAll + [end_edge.index]
        prev_edge = start_edge
        v2_prev = prev_edge.verts[0].co.copy()
        v3_prev = prev_edge.verts[1].co.copy()
        new_verts_co = [v2_prev, v3_prev]
        new_edges = [(0, 1)]
        new_faces = []

        for i, ei in enumerate([start_edge.index] + lEdgesAll):
            top -= h0
            edge_ = bm.edges[ei]
            v0_ = edge_.verts[0].co.copy()
            v1_ = edge_.verts[1].co.copy()
            v0_.z = v1_.z = top
            memory_new_edge(v0_, v1_, new_verts_co, new_edges, base_vi)
            memory_new_face(new_verts_co, new_faces, base_vi)
            base_vi += 2

            next_edge_ = bm.edges[ex_lEdgesAll[i]]
            v2_ = next_edge_.verts[0].co.copy()
            v3_ = next_edge_.verts[1].co.copy()
            v2_.z = v3_.z = top
            memory_new_edge(v2_, v3_, new_verts_co, new_edges, base_vi)
            memory_new_face(new_verts_co, new_faces, base_vi)
            base_vi += 2

            v2_prev, v3_prev = v2_, v3_

        top -= h0
        v0_ = v3_prev.copy()
        v1_ = v2_prev.copy()
        v0_.z = v1_.z = top
        memory_new_edge(v0_, v1_, new_verts_co, new_edges, base_vi)
        memory_new_face(new_verts_co, new_faces, base_vi)
        base_vi += 2

        obj_lift = createMeshFromData("new_lift", obj.location, new_verts_co, new_faces)
        edit_mode_out()
        bpy.context.scene.objects.active = obj
        obj.select = True
        obj_lift.select = False
        edit_mode_in()

    bm.free()


def getNormalPlane(vecs, mat):
    if len(vecs) < 3:
        return None

    out_ = []
    vec_c = mathutils.Vector((0, 0, 0))
    for v in vecs:
        vec = v * mat
        out_.append(vec)
        vec_c += vec

    vec_c = vec_c / len(vecs)

    v = out_[1] - out_[0]
    w = out_[2] - out_[0]
    A = v.y * w.z - v.z * w.y
    B = -v.x * w.z + v.z * w.x
    C = v.x * w.y - v.y * w.x
    D = -out_[0].x * A - out_[0].y * B - out_[0].z * C

    norm = mathutils.Vector((A, B, C)).normalized()
    return norm


def getNormalPlane2(vecs, mat):
    if len(vecs) < 3:
        return None

    out_ = []
    vec_c = mathutils.Vector((0, 0, 0))
    for v in vecs:
        vec = mat * v
        out_.append(vec)
        vec_c += vec

    vec_c = vec_c / len(vecs)

    v = out_[1] - out_[0]
    w = out_[2] - out_[0]
    A = v.y * w.z - v.z * w.y
    B = -v.x * w.z + v.z * w.x
    C = v.x * w.y - v.y * w.x
    D = -out_[0].x * A - out_[0].y * B - out_[0].z * C

    norm = mathutils.Vector((A, B, C)).normalized()
    return norm


def mk_ob(mesh, name, loc):
    ob = bpy.data.objects.new(name, mesh)
    ob.location = loc
    bpy.context.scene.objects.link(ob)
    return ob


def sign(x):
    if x < 0:
        return -1
    else:
        return 1


def match3D(flip=False):
    mode_ = bpy.context.mode
    store_align('coner', mode_)
    config = bpy.context.window_manager.paul_manager
    if config.object_name_store_v == '' or \
            config.object_name_store_v not in bpy.context.scene.objects or \
            config.active_edge1_store < 0 or config.active_edge2_store < 0:
        print_error('Stored Vertex is required')
        print('Error: 3dmatch 01')
        return False

    if config.object_name_store_c == '':
        if mode_ == 'EDIT_MESH':
            print_error('Not specified object')
            print('Error: 3dmatch 02')
            return False
        else:
            config.object_name_store_c = bpy.context.active_object.name

    if config.coner_edge1_store == -1 or \
            config.coner_edge2_store == -1:
        if mode_ == 'EDIT_MESH':
            # print_error('Not specified object')
            print_error('Stored edges is required')
            print('Error: 3dmatch 03')
            return False

    obj_A = bpy.data.objects[config.object_name_store_v]
    obj_B = bpy.data.objects[config.object_name_store_c]
    ve1 = obj_A.data.edges[config.active_edge1_store]
    ve2 = obj_A.data.edges[config.active_edge2_store]
    e1 = obj_B.data.edges[config.coner_edge1_store]
    e2 = obj_B.data.edges[config.coner_edge2_store]

    # получаем ещё две вершины. Иначе - реджект
    connect_vs = []
    connect_vs.extend(ve1.vertices[:])
    connect_vs.extend(ve2.vertices[:])
    v1 = -1
    for v in connect_vs:
        if connect_vs.count(v) > 1:
            v1 = obj_A.data.vertices[v]
            connect_vs.pop(connect_vs.index(v))
            connect_vs.pop(connect_vs.index(v))
            break

    if v1 == -1:
        print_error('Active vertex of object_A must have two edges')
        print('Error: 3dmatch 04')
        return False

    v2 = obj_A.data.vertices[connect_vs[0]]
    v3 = obj_A.data.vertices[connect_vs[1]]

    # вычислить нормаль объекта Б
    # if mode_ =='EDIT_MESH':
    if config.coner_edge1_store != -1:
        lws = list(e1.vertices[:] + e2.vertices[:])
        for l in lws:
            if lws.count(l) > 1:
                lws.pop(lws.index(l))
                w1 = obj_B.data.vertices[lws.pop(lws.index(l))]

        w3 = obj_B.data.vertices[lws.pop()]
        w2 = obj_B.data.vertices[lws.pop()]
    else:
        w1, w2, w3 = 0, 0, 0

    mat_w = obj_B.matrix_world.copy()
    k_x = 1
    if mode_ != 'EDIT_MESH':
        if config.flip_match:
            k_x = -1
        else:
            k_x = 1

    if flip != config.flip_match:
        config.flip_match = flip
        if mode_ == 'EDIT_MESH':
            bpy.ops.object.mode_set(mode='EDIT')
            normal_B = getNormalPlane([w1.co, w2.co, w3.co], mathutils.Matrix())
            normal_z = mathutils.Vector((0, 0, 1))
            mat_rot_norm = normal_B.rotation_difference(normal_z).to_matrix().to_4x4()

            verts = [v for v in obj_B.data.vertices if v.select == True]
            for v in verts:
                v.co = mat_rot_norm * v.co

            bpy.ops.transform.resize(value=(1, 1, -1), constraint_axis=(False, False, True))
        else:
            k_x *= -1

    normal_x = mathutils.Vector((1, 0, 0)) * k_x

    bpy.ops.object.mode_set(mode='EDIT')
    bpy.ops.object.mode_set(mode='OBJECT')
    edge_idx = [i.index for i in obj_A.data.edges \
                if v1 in i.vertices[:] and v2 in i.vertices[:]]

    vecA = (v2.co - v1.co) * obj_A.matrix_world.to_3x3().transposed()

    if mode_ == 'EDIT_MESH':
        v1A = obj_A.matrix_world * v1.co
        w1B = obj_B.matrix_world * w1.co

        vecB = (w2.co - w1.co)
        mat_rot = vecB.rotation_difference(vecA).to_matrix().to_4x4()

        # rotation1
        bpy.ops.object.mode_set(mode='EDIT')
        bpy.ops.object.mode_set(mode='OBJECT')

        normal_A = getNormalPlane([v1.co, v2.co, v3.co], mathutils.Matrix())
        normal_A = normal_A * obj_A.matrix_world.to_3x3().transposed()
        normal_B = getNormalPlane([w1.co, w2.co, w3.co], mathutils.Matrix())
        mat_rot2 = normal_B.rotation_difference(normal_A).to_matrix().to_4x4()

        verts = [v for v in obj_B.data.vertices if v.select == True]
        for v in verts:
            v.co = mat_rot2 * v.co

        bpy.ops.object.mode_set(mode='EDIT')
        bpy.ops.object.mode_set(mode='OBJECT')

        vecA = (v2.co - v1.co) * obj_A.matrix_world.to_3x3().transposed()
        vecB = (w2.co - w1.co)
        mat_rot = vecB.rotation_difference(vecA).to_matrix().to_4x4()
        verts = [v for v in obj_B.data.vertices if v.select == True]
        for v in verts:
            v.co = mat_rot * v.co

        # invert rotation
        bpy.ops.object.mode_set(mode='EDIT')
        bpy.ops.object.mode_set(mode='OBJECT')

        vec1 = mathutils.Vector((0, 0, 1))
        vec2 = obj_B.matrix_world * vec1
        mat_rot2 = vec1.rotation_difference(vec2).to_matrix().to_4x4()
        mat_tmp = obj_B.matrix_world.copy()

        mat_tmp[0][3] = 0
        mat_tmp[1][3] = 0
        mat_tmp[2][3] = 0
        mat_inv = mat_tmp.inverted()

        verts = [v for v in obj_B.data.vertices if v.select == True]
        for v in verts:
            v.co = mat_inv * v.co

        # location
        bpy.ops.object.mode_set(mode='EDIT')
        bpy.ops.object.mode_set(mode='OBJECT')

        w1B = obj_B.matrix_world * w1.co
        mat_loc = mathutils.Matrix.Translation(v1A - w1B)
        vec_l = mat_inv * (v1A - w1B)

        mat_tp = obj_B.matrix_world
        vec_loc = mathutils.Vector((mat_tp[0][3], mat_tp[1][3], mat_tp[2][3]))

        verts = [v for v in obj_B.data.vertices if v.select == True]
        for v in verts:
            v.co = v.co + vec_l

        bpy.ops.object.mode_set(mode='EDIT')

    else:
        if config.coner_edge1_store == -1:
            v1A = obj_A.matrix_world * v1.co
            normal_A = getNormalPlane([v1.co, v2.co, v3.co], mathutils.Matrix())
            normal_A = normal_A * obj_A.matrix_world.to_3x3().transposed()
            normal_z = mathutils.Vector((0, 0, 1))
            mat_rot1 = normal_z.rotation_difference(normal_A).to_matrix().to_4x4()

            vecA = (v2.co - v1.co) * obj_A.matrix_world.to_3x3().transposed()
            vecB = mat_rot1 * normal_x
            mat_rot = vecB.rotation_difference(vecA).to_matrix().to_4x4()

            obj_B.matrix_world = mat_rot * mat_rot1
            vec_l = v1A - obj_B.location
            obj_B.location = obj_B.location + vec_l

        else:
            v1A = obj_A.matrix_world * v1.co
            w1B = obj_B.matrix_world * w1.co
            vecB = (w2.co - w1.co) * obj_B.matrix_world.to_3x3().transposed()

            normal_A = getNormalPlane([v1.co, v2.co, v3.co], mathutils.Matrix())
            normal_A = normal_A * obj_A.matrix_world.to_3x3().transposed()
            normal_B = getNormalPlane([w1.co, w2.co, w3.co], mathutils.Matrix())
            normal_B = normal_B * obj_B.matrix_world.to_3x3().transposed()
            mat_rot1 = normal_B.rotation_difference(normal_A).to_matrix().to_4x4()

            vecA = (v2.co - v1.co) * obj_A.matrix_world.to_3x3().transposed()
            vecB = mat_rot1 * vecB
            mat_rot = vecB.rotation_difference(vecA).to_matrix().to_4x4()

            obj_B.matrix_world = mat_rot * mat_rot1
            w1B = obj_B.matrix_world * w1.co
            vec_l = v1A - w1B
            obj_B.location = obj_B.location + vec_l
    return True


def mirrorside():
    mode_ = bpy.context.mode
    bpy.ops.object.mode_set(mode='OBJECT')
    bpy.ops.object.mode_set(mode='EDIT')
    config = bpy.context.window_manager.paul_manager
    if config.object_name_store_v == '' or \
            config.active_edge1_store < 0 or config.active_edge2_store < 0:
        print_error2('Stored Vertex is required', 'mirrorside 01')
        return False

    obj_A = bpy.data.objects[config.object_name_store_v]
    ve1 = obj_A.data.edges[config.active_edge1_store]
    ve2 = obj_A.data.edges[config.active_edge2_store]

    # получаем ещё две вершины. Иначе - реджект
    connect_vs = []
    connect_vs.extend(ve1.vertices[:])
    connect_vs.extend(ve2.vertices[:])
    v1 = -1
    for v in connect_vs:
        if connect_vs.count(v) > 1:
            v1 = obj_A.matrix_world * obj_A.data.vertices[v].co
            connect_vs.pop(connect_vs.index(v))
            connect_vs.pop(connect_vs.index(v))
            break

    if v1 == -1:
        print_error2('Active vertex of object_A must have two edges', 'mirrorside 04')
        return False

    v2 = obj_A.matrix_world * obj_A.data.vertices[connect_vs[0]].co
    v3 = obj_A.matrix_world * obj_A.data.vertices[connect_vs[1]].co

    obj_B = bpy.context.scene.objects.active
    normal_B = getNormalPlane([v1, v2, v3], mathutils.Matrix())
    if mode_ == 'EDIT_MESH':
        bpy.ops.object.mode_set(mode='EDIT')
        ref_vts = [v for v in obj_B.data.vertices if v.select == True]
        verts = []
        v_idx_B = []
        for v in ref_vts:
            verts.append(v.co)
            v_idx_B.append(v.index)

        bpy.ops.object.mode_set(mode='OBJECT')
        bm = bmesh.new()
        bm.from_mesh(obj_B.data)
        check_lukap(bm)

        vts = []
        mat_inv = obj_B.matrix_world.inverted()
        for pt_a_ in verts:
            pt_a = obj_B.matrix_world * pt_a_
            pt_b = normal_B + pt_a
            cross_pt = mathutils.geometry.intersect_line_plane(pt_a, pt_b, v1, normal_B)

            d_vec = cross_pt - pt_a
            pt_c = cross_pt + d_vec
            v_new = bm.verts.new(mat_inv * pt_c)
            vts.append(v_new)

        bm.verts.index_update()
        check_lukap(bm)
        vts_ = [v.index for v in vts]
        ref_edges = [(e.vertices[0], e.vertices[1]) for e in obj_B.data.edges if e.select == True]
        for e in ref_edges:
            ev0 = v_idx_B.index(e[0])
            ev1 = v_idx_B.index(e[1])
            e = (bm.verts[vts_[ev0]], bm.verts[vts_[ev1]])
            bm.edges.new(e)
        check_lukap(bm)

        ref_faces = [(v for v in f.vertices) for f in obj_B.data.polygons if f.select == True]
        for f in ref_faces:
            f_B = []
            for v in f:
                fv = v_idx_B.index(v)
                f_B.append(bm.verts[vts_[fv]])

            bm.faces.new(tuple(f_B))

        bm.to_mesh(obj_B.data)
        bm.free()
        bpy.ops.object.mode_set(mode='EDIT')

    elif mode_ == 'OBJECT':
        bpy.ops.object.mode_set(mode='OBJECT')
        bm = bmesh.new()
        bm.from_mesh(obj_B.data)
        check_lukap(bm)

        ref_vtert = bm.verts
        mat_inv = obj_B.matrix_world.inverted()
        for pt_a_ in ref_vtert:
            pt_a = obj_B.matrix_world * pt_a_.co
            pt_b = normal_B + pt_a
            cross_pt = mathutils.geometry.intersect_line_plane(pt_a, pt_b, v1, normal_B)

            d_vec = cross_pt - pt_a
            pt_c = cross_pt + d_vec
            ref_vtert[pt_a_.index].co = mat_inv * pt_c

        name = obj_B.name + 'copy'
        me = bpy.data.meshes.new(name + '_Mesh')
        obj_C = bpy.data.objects.new(name, me)
        # Привязка объекта к сцене
        bpy.context.scene.objects.link(obj_C)

        bm.to_mesh(me)
        me.update()
        bm.free()
    return True


def getorient():
    obj = bpy.context.active_object
    if obj.type != 'MESH':
        return False

    space_data = bpy.context.space_data
    trans_ori = 'GLOBAL'
    if hasattr(space_data, 'transform_orientation'):
        trans_ori = space_data.transform_orientation

    bpy.ops.transform.create_orientation(name='1DTEMP', use=True, overwrite=True)
    if trans_ori == '1DTEMP':
        bpy.context.space_data.show_manipulator = not bpy.context.space_data.show_manipulator
    else:
        bpy.context.space_data.show_manipulator = True
    return True


def main_align_object(axe='X', project='XY'):
    obj_res = bpy.context.active_object
    if obj_res.type == 'MESH':
        bpy.ops.object.mode_set(mode='EDIT')
        bpy.ops.object.mode_set(mode='OBJECT')

    config = bpy.context.window_manager.paul_manager
    if config.object_name_store == '':
        print_error('Stored Edge is required')
        print('Error: align_object 01')
        return False

    obj = bpy.data.objects[config.object_name_store]
    mesh = obj.data
    bm = bmesh.new()
    bm.from_mesh(mesh)
    check_lukap(bm)

    # Найдём диагональ Store
    edge_idx = config.edge_idx_store
    verts_edge_store = bm.edges[edge_idx].verts
    vec_diag_store = verts_edge_store[1].co - verts_edge_store[0].co

    # Развернем объект
    dict_axe = {'X': (1.0, 0.0, 0.0), 'Y': (0.0, 1.0, 0.0), 'Z': (0.0, 0.0, 1.0)}
    aa_vec = dict_axe[axe]

    aa = mathutils.Vector(aa_vec)
    bb = vec_diag_store.normalized()

    planes = set(project)
    if 'X' not in planes:
        aa.x = 0
        bb.x = 0
    if 'Y' not in planes:
        aa.y = 0
        bb.y = 0
    if 'Z' not in planes:
        aa.z = 0
        bb.z = 0

    vec = aa
    q_rot = vec.rotation_difference(bb).to_matrix().to_4x4()
    obj_res.matrix_world *= q_rot
    for obj in bpy.context.scene.objects:
        if obj.select:
            if obj.name != obj_res.name:
                orig_tmp = obj_res.location - obj.location
                mat_loc = mathutils.Matrix.Translation(orig_tmp)
                mat_loc2 = mathutils.Matrix.Translation(-orig_tmp)

                obj.matrix_world *= mat_loc * q_rot * mat_loc2
    return True


def main_align():
    bpy.ops.object.mode_set(mode='OBJECT')
    bpy.ops.object.mode_set(mode='EDIT')

    config = bpy.context.window_manager.paul_manager
    if config.object_name_store == '':
        print_error('Stored Edge is required')
        print('Error: align 01')
        return False

    obj = bpy.data.objects[config.object_name_store]
    mesh = obj.data
    bm = bmesh.new()
    bm.from_mesh(mesh)
    check_lukap(bm)

    # Найдём диагональ Store
    edge_idx = config.edge_idx_store
    verts_edge_store = bm.edges[edge_idx].verts
    vec_diag_store = verts_edge_store[1].co - verts_edge_store[0].co

    # Получим выделенное ребро
    obj_res = bpy.context.active_object
    mesh_act = obj_res.data
    bm_act = bmesh.new()
    bm_act.from_mesh(mesh_act)
    check_lukap(bm_act)

    edge_idx_act, el = bm_vert_active_get(bm_act)
    if edge_idx_act == None:
        print_error('Selection with active edge is required')
        print('Error: align 03')
        return False

    d_pos = bpy.context.scene.cursor_location - obj_res.location
    if not config.align_dist_z:
        for v in bm_act.verts:
            if v.select:
                v.co -= d_pos

    verts_edge_act = bm_act.edges[edge_idx_act].verts
    vec_diag_act = verts_edge_act[1].co - verts_edge_act[0].co

    # Сравниваем
    aa = vec_diag_act
    if config.align_lock_z:
        aa.z = 0
    aa.normalized()

    bb = vec_diag_store
    if config.align_lock_z:
        bb.z = 0
    bb.normalized()
    q_rot = bb.rotation_difference(aa).to_matrix().to_4x4()

    select_mesh_rot(bm_act, q_rot)
    verts = [v for v in bm_act.verts if v.select == True]
    pos = (verts_edge_store[0].co + obj.location) \
          - (verts_edge_act[0].co + obj_res.location)

    if not config.align_dist_z:
        pos = mathutils.Vector((0, 0, 0))  # bpy.context.scene.cursor_location
    for v in verts:
        pos_z = v.co.z
        v.co = v.co + pos
        if config.align_lock_z:
            v.co.z = pos_z

    if not config.align_dist_z:
        for v in bm_act.verts:
            if v.select:
                v.co += d_pos

    bpy.ops.object.mode_set(mode='OBJECT')

    bm_act.to_mesh(mesh_act)
    bm_act.free()

    bm.free()

    bpy.ops.object.mode_set(mode='EDIT')
    return True


def main_spread(context, mode, influe):
    conf = bpy.context.window_manager.paul_manager
    if not conf.shape_spline: mode = (mode[0], mode[1], mode[2], not mode[3])

    if conf.shape_spline and influe < 51:
        return main_spline(context, mode, influe / 50)
    elif conf.shape_spline and influe < 101:
        if not conf.spline_Bspline2 or main_spline(context, mode, (100 - influe) / 50):
            return main_B_spline_2(context, mode, (influe - 50) / 50)
        else:
            return False
    elif conf.shape_spline and influe < 151:
        if not conf.spline_Bspline2 or main_B_spline_2(context, mode, (150 - influe) / 50):
            return main_B_spline(context, mode, (influe - 100) / 50)
        else:
            return False
    elif conf.shape_spline and influe < 201:
        if not conf.spline_Bspline2 or main_B_spline(context, mode, (200 - influe) / 50):
            return main_Basier_mid(context, mode, (influe - 150) / 50)
        else:
            return False
    elif conf.shape_spline and influe > 200:
        if conf.spline_Bspline2:
            return main_Basier_mid(context, mode, (250 - influe) / 50)
        else:
            return False

    bpy.ops.object.mode_set(mode='OBJECT')
    bpy.ops.object.mode_set(mode='EDIT')

    obj = bpy.context.active_object
    me = obj.data

    verts = find_index_of_selected_vertex(me)
    cou_vs = len(verts) - 1
    if verts != None and cou_vs > 0:
        extreme_vs = find_extreme_select_verts(me, verts)

        if len(extreme_vs) != 2:
            print_error('Single Loop only')
            print('Error: 01')
            return False

        list_koeff = []

        if mode[0]:
            min_v = min([me.vertices[extreme_vs[0]].co.x, extreme_vs[0]], \
                        [me.vertices[extreme_vs[1]].co.x, extreme_vs[1]])
            max_v = max([me.vertices[extreme_vs[0]].co.x, extreme_vs[0]], \
                        [me.vertices[extreme_vs[1]].co.x, extreme_vs[1]])

            if (max_v[0] - min_v[0]) == 0:
                min_v = [me.vertices[extreme_vs[0]].co.x, extreme_vs[0]]
                max_v = [me.vertices[extreme_vs[1]].co.x, extreme_vs[1]]

            sort_list = find_all_connected_verts(me, min_v[1], [])

            if len(sort_list) != len(verts):
                print_error('Incoherent loop')
                print('Error: 020')
                return False

            step = []
            if mode[3]:
                list_length = []
                sum_length = 0.0
                x_sum = 0.0
                for sl in range(cou_vs):
                    subb = me.vertices[sort_list[sl + 1]].co - me.vertices[sort_list[sl]].co
                    length = subb.length
                    sum_length += length
                    list_length.append(sum_length)
                    x_sum += subb.x

                for sl in range(cou_vs):
                    tmp = list_length[sl] / sum_length
                    list_koeff.append(tmp)
                    step.append(x_sum * tmp)
            else:
                diap = (max_v[0] - min_v[0]) / cou_vs
                for sl in range(cou_vs):
                    step.append((sl + 1) * diap)

            bpy.ops.object.mode_set(mode='OBJECT')
            for idx in range(cou_vs):
                me.vertices[sort_list[idx + 1]].co.x = me.vertices[sort_list[0]].co.x + step[idx]

            bpy.ops.object.mode_set(mode='EDIT')

        if mode[1]:
            min_v = min([me.vertices[extreme_vs[0]].co.y, extreme_vs[0]], \
                        [me.vertices[extreme_vs[1]].co.y, extreme_vs[1]])
            max_v = max([me.vertices[extreme_vs[0]].co.y, extreme_vs[0]], \
                        [me.vertices[extreme_vs[1]].co.y, extreme_vs[1]])

            if (max_v[0] - min_v[0]) == 0:
                min_v = [me.vertices[extreme_vs[0]].co.y, extreme_vs[0]]
                max_v = [me.vertices[extreme_vs[1]].co.y, extreme_vs[1]]

            sort_list = find_all_connected_verts(me, min_v[1], [])
            if len(sort_list) != len(verts):
                print_error('Incoherent loop')
                print('Error: 021')
                return False

            step = []
            if mode[3]:
                list_length = []
                sum_length = 0.0
                y_sum = 0.0
                if len(list_koeff) == 0:
                    for sl in range(cou_vs):
                        subb = me.vertices[sort_list[sl + 1]].co - me.vertices[sort_list[sl]].co
                        length = subb.length
                        sum_length += length
                        list_length.append(sum_length)
                        y_sum += subb.y

                    for sl in range(cou_vs):
                        tmp = list_length[sl] / sum_length
                        list_koeff.append(tmp)
                        step.append(y_sum * tmp)
                else:
                    for sl in range(cou_vs):
                        subb = me.vertices[sort_list[sl + 1]].co - me.vertices[sort_list[sl]].co
                        y_sum += subb.y
                        tmp = list_koeff[sl]
                        step.append(y_sum * tmp)

            else:
                diap = (max_v[0] - min_v[0]) / cou_vs
                for sl in range(cou_vs):
                    step.append((sl + 1) * diap)

            bpy.ops.object.mode_set(mode='OBJECT')
            for idx in range(cou_vs):
                me.vertices[sort_list[idx + 1]].co.y = me.vertices[sort_list[0]].co.y + step[idx]

            bpy.ops.object.mode_set(mode='EDIT')

        if mode[2]:
            min_v = min([me.vertices[extreme_vs[0]].co.z, extreme_vs[0]], \
                        [me.vertices[extreme_vs[1]].co.z, extreme_vs[1]])
            max_v = max([me.vertices[extreme_vs[0]].co.z, extreme_vs[0]], \
                        [me.vertices[extreme_vs[1]].co.z, extreme_vs[1]])

            if (max_v[0] - min_v[0]) == 0:
                min_v = [me.vertices[extreme_vs[0]].co.z, extreme_vs[0]]
                max_v = [me.vertices[extreme_vs[1]].co.z, extreme_vs[1]]

            sort_list = find_all_connected_verts(me, min_v[1], [])
            if len(sort_list) != len(verts):
                print_error('Incoherent loop')
                print('Error: 022')
                return False

            step = []
            if mode[3]:
                list_length = []
                sum_length = 0.0
                z_sum = 0.0
                if len(list_koeff) == 0:
                    for sl in range(cou_vs):
                        subb = me.vertices[sort_list[sl + 1]].co - me.vertices[sort_list[sl]].co
                        length = subb.length
                        sum_length += length
                        list_length.append(sum_length)
                        z_sum += subb.z

                    for sl in range(cou_vs):
                        step.append(z_sum * list_length[sl] / sum_length)
                else:
                    for sl in range(cou_vs):
                        subb = me.vertices[sort_list[sl + 1]].co - me.vertices[sort_list[sl]].co
                        z_sum += subb.z
                        tmp = list_koeff[sl]
                        step.append(z_sum * tmp)
            else:
                diap = (max_v[0] - min_v[0]) / cou_vs
                for sl in range(cou_vs):
                    step.append((sl + 1) * diap)

            bpy.ops.object.mode_set(mode='OBJECT')
            for idx in range(cou_vs):
                me.vertices[sort_list[idx + 1]].co.z = me.vertices[sort_list[0]].co.z + step[idx]

            bpy.ops.object.mode_set(mode='EDIT')

    return True


def main_ss(context):
    obj = bpy.context.active_object
    me = obj.data
    space_data = bpy.context.space_data
    trans_ori = 'GLOBAL'
    if hasattr(space_data, 'transform_orientation'):
        trans_ori = space_data.transform_orientation

    bpy.ops.object.mode_set(mode='OBJECT')
    bpy.ops.object.mode_set(mode='EDIT')

    vs_idx = find_index_of_selected_vertex(me)
    if vs_idx:
        x_coos = [v.co.x for v in me.vertices if v.index in vs_idx]
        y_coos = [v.co.y for v in me.vertices if v.index in vs_idx]
        z_coos = [v.co.z for v in me.vertices if v.index in vs_idx]

        min_x = min(x_coos)
        max_x = max(x_coos)

        min_y = min(y_coos)
        max_y = max(y_coos)

        min_z = min(z_coos)
        max_z = max(z_coos)

        len_x = max_x - min_x
        len_y = max_y - min_y

        if trans_ori == '1DTEMP':
            bpy.ops.transform.resize(value=(1, 1, 0), constraint_axis=(False, False, True),
                                     constraint_orientation=trans_ori)
        else:
            if len_y < len_x:
                bpy.ops.transform.resize(value=(1, 0, 1), constraint_axis=(False, True, False),
                                         constraint_orientation=trans_ori)
            else:
                bpy.ops.transform.resize(value=(0, 1, 1), constraint_axis=(True, False, False),
                                         constraint_orientation=trans_ori)


def main_offset(x):
    mode_obj = bpy.context.mode == 'OBJECT'
    mode_obj2 = bpy.context.mode
    bpy.ops.object.mode_set(mode='OBJECT')
    if mode_obj2 == 'EDIT_MESH':
        bpy.ops.object.mode_set(mode='EDIT')

    config = bpy.context.window_manager.paul_manager
    if config.object_name_store == '':
        print_error('Stored Edge is required')
        print('Error: offset 01')
        return False

    obj = bpy.context.active_object
    obj_edge = bpy.data.objects[config.object_name_store]
    if obj:
        vec = mathutils.Vector(config.vec_store)

        if vec.length != 0:
            vec.normalize()
            vec *= x
        me = obj.data

        if mode_obj2 == 'EDIT_MESH':
            bm_act = bmesh.new()
            bm_act.from_mesh(me)
            check_lukap(bm_act)

            verts_act = find_index_of_selected_vertex(me)
            vec = vec * obj.matrix_local
            for v_idx in verts_act:
                if not config.shift_lockX:
                    bm_act.verts[v_idx].co.x += vec.x
                if not config.shift_lockY:
                    bm_act.verts[v_idx].co.y += vec.y
                if not config.shift_lockZ:
                    bm_act.verts[v_idx].co.z += vec.z

            bpy.ops.object.mode_set(mode='OBJECT')
            bm_act.to_mesh(me)
            bm_act.free()
            bpy.ops.object.mode_set(mode='EDIT')
        else:
            bpy.ops.object.mode_set(mode='OBJECT')
            if config.shift_local:
                vec = vec * obj.matrix_world
            if not config.shift_lockX:
                if config.shift_local:
                    mat_loc = mathutils.Matrix.Translation((vec.x, 0, 0))
                else:
                    obj.location.x += vec.x

            if not config.shift_lockY:
                if config.shift_local:
                    mat_loc = mathutils.Matrix.Translation((0, vec.y, 0))
                else:
                    obj.location.y += vec.y

            if not config.shift_lockZ:
                if config.shift_local:
                    mat_loc = mathutils.Matrix.Translation((0, 0, vec.z))
                else:
                    obj.location.z += vec.z

            if config.shift_local:
                obj.matrix_world *= mat_loc
    return True


def scaler_get(sign):
    config = bpy.context.window_manager.paul_manager
    obj_name = config.object_name_store
    if obj_name == '' and obj_name in bpy.data.objects:
        print_error2('Stored key is required', '01 scaler get')
        return False

    if config.active_edge1_store < 0 and config.active_edge2_store < 0:
        print_error2('Stored key is required', '02 scaler get')
        return False

    obj = bpy.data.objects[obj_name]
    edge1 = obj.data.edges[config.active_edge1_store]
    edge2 = obj.data.edges[config.active_edge2_store]
    i11 = edge1.vertices[0]
    i12 = edge1.vertices[1]
    i21 = edge2.vertices[0]
    i22 = edge2.vertices[1]
    length1 = (obj.data.vertices[i11].co - obj.data.vertices[i12].co).length
    length2 = (obj.data.vertices[i21].co - obj.data.vertices[i22].co).length
    l = [length1, length2]
    l.sort()
    if sign > 0:
        ko = l[1] / l[0]
    else:
        ko = l[0] / l[1]

    bpy.ops.transform.resize(value=(ko, ko, ko))
    return True


def main_rotor(angle_):
    mode_obj = bpy.context.mode == 'OBJECT'
    mode_obj2 = bpy.context.mode
    bpy.ops.object.mode_set(mode='OBJECT')
    if mode_obj2 == 'EDIT_MESH':
        bpy.ops.object.mode_set(mode='EDIT')

    config = bpy.context.window_manager.paul_manager
    if config.object_name_store == '':
        print_error2('Stored key is required', '01 rotor 3D')
        return False

    obj = bpy.context.active_object
    obj_cone = bpy.data.objects[config.object_name_store]
    if obj:
        center = mathutils.Vector(config.rotor3d_center)
        axis_ = mathutils.Vector(config.rotor3d_axis)

        me = obj.data

        if mode_obj2 == 'EDIT_MESH':
            bm_act = bmesh.new()
            bm_act.from_mesh(me)
            check_lukap(bm_act)

            verts_act = find_index_of_selected_vertex(me)
            vts_all = [v for v in bm_act.verts if v.index in verts_act]
            edg_all = [e for e in bm_act.edges if e.verts[0].index in verts_act and \
                       e.verts[1].index in verts_act]
            fcs_all = [f for f in bm_act.faces if f.select == True]
            geom_ = vts_all + edg_all + fcs_all

            if config.rotor3d_copy:
                ret = bmesh.ops.spin(bm_act, geom=geom_, cent=center, \
                                     space=mathutils.Matrix(), axis=axis_, angle=angle_, steps=1, use_duplicate=True)
                for v in bm_act.verts:
                    v.select_set(False)
                bm_act.select_flush(False)
                for v in ret['geom_last']:
                    v.select = True
            else:
                mat_rot = mathutils.Matrix.Rotation(angle_, 4, axis_)
                bmesh.ops.rotate(bm_act, cent=center, verts=vts_all, \
                                 matrix=mat_rot, space=mathutils.Matrix())

            bpy.ops.object.mode_set(mode='OBJECT')
            bm_act.to_mesh(me)
            bm_act.free()
            bpy.ops.object.mode_set(mode='EDIT')
        else:
            bpy.ops.object.mode_set(mode='OBJECT')
            axis_ = axis_ * obj_cone.matrix_world
            center = obj_cone.matrix_world * center
            loc = center - obj.location
            mat_loc = mathutils.Matrix.Translation(loc)
            mat_loc2 = mathutils.Matrix.Translation(-loc)
            mat_rot = mathutils.Matrix.Rotation(angle_, 4, axis_)
            mat_rot2 = obj.rotation_euler.copy()
            loc_, rot_, sca_ = obj.matrix_world.decompose()
            rot_inv = rot_.to_matrix().to_4x4().inverted()

            obj.matrix_world *= rot_inv
            mat_out = mat_loc * mat_rot * mat_loc2
            obj.matrix_world = obj.matrix_world * mat_out * rot_.to_matrix().to_4x4()
    return True


def GetDistToCursor():
    # out: vector
    mode = bpy.context.mode
    bpy.ops.object.mode_set(mode='OBJECT')
    bpy.ops.object.mode_set(mode='EDIT')
    obj = bpy.context.active_object
    cursor_location = location_3Dcursor()
    if obj:
        d_pos = cursor_location - obj.location
        center = mathutils.Vector((0, 0, 0))

        if mode == 'EDIT_MESH':
            me = obj.data
            mode = 'EDIT'
            bm = bmesh.new()
            bm.from_mesh(me)
            check_lukap(bm)
            elem, el = bm_vert_active_get(bm)
            if elem != None:
                if el == 'V' and bm.verts[elem].select:
                    center = bm.verts[elem].co
                    # print('VERT')
                elif el == 'E':
                    center = mathutils.Vector(bm.edges[elem].verts[1].co + bm.edges[elem].verts[0].co) / 2
                    # print('EDGE')
                elif el == 'F':
                    center = bm.faces[elem].calc_center_median()
                    # print('FACE')
                center = center * obj.matrix_world.to_3x3().transposed()
    bpy.ops.object.mode_set(mode=mode)
    return d_pos - center


def location_3Dcursor():
    for area in bpy.context.screen.areas:
        if area.type == 'VIEW_3D':
            for space in area.spaces:
                if space.type == 'VIEW_3D':
                    return space.cursor_location
    return bpy.context.scene.cursor_location


def GetDistObjToCursor(obj):
    # out: vector
    cursor_location = location_3Dcursor()
    return cursor_location - obj.location


def GetStoreVecLength():
    config = bpy.context.window_manager.paul_manager
    if config.object_name_store == '':
        print_error('Stored Edge is required')
        print('Error: offset 01')
        return False

    vec = mathutils.Vector(config.vec_store)
    return vec.length


def GetStoreVecAngle():
    bpy.ops.object.editmode_toggle()
    bpy.ops.object.editmode_toggle()

    obj = bpy.context.active_object
    mesh = obj.data
    bm = bmesh.new()
    bm.from_mesh(mesh)
    check_lukap(bm)

    obj_name = obj.name
    config = bpy.context.window_manager.paul_manager
    active_edge, el = bm_vert_active_get(bm)
    old_edge1 = config.active_edge1_store
    old_edge2 = config.active_edge2_store
    old_name = config.object_name_store
    old_step_angle = config.step_angle

    if active_edge != None and el == 'E':
        config.object_name_store = obj_name
        config.active_edge1_store = active_edge
        Edges = mesh.edges
        verts = bm.edges[active_edge].verts
        v0 = verts[0].index
        v1 = verts[1].index
        edges_idx = [i.index for i in Edges \
                     if i.select and i.index != active_edge and \
                     (v1 in i.vertices[:] or v0 in i.vertices[:])]
        if edges_idx:
            config.active_edge2_store = edges_idx[0]
            l_ed2 = [Edges[edges_idx[0]].vertices[0], Edges[edges_idx[0]].vertices[1]]
            (v1, v0) = (v0, v1) if v0 in l_ed2 else (v1, v0)
            l_ed2.pop(l_ed2.index(v1))
            v2 = l_ed2[0]
            v0_ = bm.verts[v0].co
            v1_ = bm.verts[v1].co
            v2_ = bm.verts[v2].co
            config.step_angle = (v0_ - v1_).angle(v2_ - v1_, 0)
            config.rotor3d_center = v1_
            config.rotor3d_axis = mathutils.geometry.normal(v0_, v1_, v2_)
            return True

    if active_edge != None and el == 'V':
        active_vert = active_edge
        config.object_name_store = obj_name

        v2_l = find_all_connected_verts(mesh, active_vert, [], 0)
        control_vs = find_connected_verts_simple(mesh, active_vert)
        if len(v2_l) > 2 and len(control_vs) == 1:
            v1 = v2_l.pop(1)
            edges_idx = []
            for v2 in v2_l[:2]:
                edges_idx.extend([i.index for i in mesh.edges \
                                  if v1 in i.vertices[:] and v2 in i.vertices[:]])

            if len(edges_idx) > 1:
                config.active_edge1_store = edges_idx[0]
                config.active_edge2_store = edges_idx[1]
                v0_ = bm.verts[active_vert].co
                v1_ = bm.verts[v1].co
                v2_ = bm.verts[v2].co
                config.step_angle = (v0_ - v1_).angle(v2_ - v1_, 0)
                config.rotor3d_center = v1_
                config.rotor3d_axis = mathutils.geometry.normal(v0_, v1_, v2_)
                return True

    config.object_name_store = ''
    config.active_edge1_store = -1
    config.active_edge2_store = -1
    config.step_angle = 0
    print_error2('Side is undefined', '01 GetStoreVecAngle')

    bm.free()
    return False


def select_v_on_plane():
    config = bpy.context.window_manager.paul_manager
    obj = bpy.context.active_object
    if obj.type != 'MESH':
        return

    bpy.ops.object.mode_set(mode='OBJECT')
    bpy.ops.object.mode_set(mode='EDIT')
    bpy.ops.mesh.select_mode(type='VERT')

    me = obj.data
    bm = bmesh.new()
    bm.from_mesh(me)
    check_lukap(bm)

    P1 = me.polygons[bm.faces.active.index]
    pols = [p.index for p in me.polygons if p.select and p.index != P1.index]
    vts_all = [v for v in bm.verts if v.select and v.index not in P1.vertices]
    p1_co = me.vertices[P1.vertices[0]].co
    p1_no = P1.normal
    dist_max = bpy.context.tool_settings.double_threshold

    for v in bm.verts:
        v.select_set(False)
        bm.select_flush(False)

    for p2 in vts_all:
        dist = abs(mathutils.geometry.distance_point_to_plane(p2.co, p1_co, p1_no))
        if dist <= dist_max:
            p2.select = True

    bpy.ops.object.mode_set(mode='OBJECT')
    bm.to_mesh(me)
    me.update()
    bm.free()
    bpy.ops.object.mode_set(mode='EDIT')


def crosspols():
    config = bpy.context.window_manager.paul_manager
    obj = bpy.context.active_object
    if obj.type != 'MESH':
        return

    bpy.ops.object.mode_set(mode='OBJECT')
    bpy.ops.object.mode_set(mode='EDIT')

    me = obj.data

    bm = bmesh.new()
    bm.from_mesh(me)
    check_lukap(bm)
    elem, mode = bm_vert_active_get(bm)
    if mode == None:
        mode = 'F'
        elem = bm.faces.active.index

    if mode == 'V':
        sec_vts = find_all_connected_verts(me, elem, not_list=[])

    if mode == 'E':
        v0 = mathutils.Vector(bm.edges[elem].verts[0].co)
        v1 = mathutils.Vector(bm.edges[elem].verts[1].co)
        v2 = v0 + mathutils.Vector((0, 0, 1))
        v3 = v1 + mathutils.Vector((0, 0, 1))
        p1_no_ = mathutils.geometry.normal(v0, v2, v3, v1)

    bpy.ops.mesh.select_mode(type='FACE')
    faceact = bm.faces.active
    if not faceact:
        faceact = [f for f in bm.faces if f.select == True][0]

    if mode == 'E':
        pols = [p.index for p in me.polygons if p.select]
        vts_all = [v for v in bm.verts if v.select]
        eds_all = [e for e in bm.edges if e.select]
        P1 = me.polygons[faceact.index]
        list_p1co = [me.vertices[P1.vertices[0]].co]
    elif mode == 'F':
        P1 = me.polygons[faceact.index]
        pols = [p.index for p in me.polygons if p.select and p.index != P1.index]
        vts_all = [v for v in bm.verts if v.select and v.index not in P1.vertices]
        eds_all = [e for e in bm.edges if e.select and e.verts[0].index not in P1.vertices \
                   and e.verts[1].index not in P1.vertices]
        list_p1co = [me.vertices[P1.vertices[0]].co]
    elif mode == 'V':
        if config.SPLIT:
            sec_vts = [elem]

        pols = [p.index for p in me.polygons if p.select]
        vts_all = [v for v in bm.verts if v.select and v.index not in sec_vts]
        eds_all = [e for e in bm.edges if e.select and e.verts[0].index not in sec_vts \
                   and e.verts[1].index not in sec_vts]
        list_p1co = [me.vertices[i].co for i in sec_vts]

    sel_edges = []
    sel_verts = []
    for l_p1co in list_p1co:
        if not config.filter_verts_top and not config.filter_verts_bottom and not config.filter_edges:
            p1_co = l_p1co
            if mode == 'E':
                p1_co = v0
                p1_no = p1_no_
            elif mode == 'V':
                p1_no = Vector((0, 0, 1))
            else:
                p1_no = P1.normal

            for pol in pols:
                P2 = me.polygons[pol]
                p2_co = me.vertices[P2.vertices[0]].co
                p2_no = P2.normal

                cross_line = mathutils.geometry.intersect_plane_plane(p1_co, p1_no, p2_co, p2_no)
                points = []
                split_ed = []
                for idx, edg in enumerate(P2.edge_keys):
                    pt_a = me.vertices[edg[0]].co
                    pt_b = me.vertices[edg[1]].co
                    cross_pt = mathutils.geometry.intersect_line_plane(pt_a, pt_b, p1_co, p1_no)
                    if cross_pt:
                        pose_pt = mathutils.geometry.intersect_point_line(cross_pt, pt_a, pt_b)
                        if pose_pt[1] <= 1 and pose_pt[1] >= 0:
                            points.append(pose_pt[0])
                            split_ed.append(idx)

                if len(points) == 2:
                    bpy.ops.mesh.select_mode(type='VERT')
                    if not config.SPLIT:
                        v1 = bm.verts.new(points[0])
                        v2 = bm.verts.new(points[1])
                        bm.verts.index_update()
                        edge = (v1, v2)
                        edg_i = bm.edges.new(edge)
                        sel_edges.append(edg_i)
                    else:
                        """ Функция позаимствована из адона Сверчок нод Bisect """
                        verts4cut = vts_all
                        edges4cut = eds_all
                        faces4cut = [fa for fa in bm.faces if fa.index in pols]
                        edges4cut_idx = [ed.index for ed in eds_all]
                        geom_in = verts4cut + edges4cut + faces4cut
                        if mode != 'V' or len(list_p1co) == 1:
                            res = bmesh.ops.bisect_plane(bm, geom=geom_in, dist=0.00001,
                                                         plane_co=p1_co, plane_no=p1_no, use_snap_center=False,
                                                         clear_outer=config.outer_clear, clear_inner=config.inner_clear)
                        else:
                            res = bmesh.ops.bisect_plane(bm, geom=geom_in, dist=0.00001,
                                                         plane_co=p1_co, plane_no=p1_no, use_snap_center=False,
                                                         clear_outer=False, clear_inner=False)

                        fres = bmesh.ops.edgenet_prepare(bm, edges=[e for e in res['geom_cut']
                                                                    if isinstance(e, bmesh.types.BMEdge)])

                        sel_edges = [e for e in fres['edges'] if e.index not in edges4cut_idx]

                        # this needs work function with solid gemometry
                        if config.fill_cuts and len(list_p1co) < 2:
                            fres = bmesh.ops.edgenet_prepare(bm, edges=[e for e in res['geom_cut']
                                                                        if isinstance(e, bmesh.types.BMEdge)])
                            bmesh.ops.edgeloop_fill(bm, edges=fres['edges'])

                        bm.verts.index_update()
                        bm.edges.index_update()
                        bm.faces.index_update()
                        check_lukap(bm)
                        break

        if config.filter_verts_top or config.filter_verts_bottom:
            bpy.ops.mesh.select_mode(type='VERT')
            p1_co = l_p1co
            if mode == 'E':
                p1_co = v0
                p1_no = p1_no_
            elif mode == 'V':
                p1_no = Vector((0, 0, 1))
            else:
                p1_no = P1.normal

            for v in vts_all:
                res = mathutils.geometry.distance_point_to_plane(v.co, p1_co, p1_no)
                if res >= 0:
                    if config.filter_verts_top:
                        sel_verts.append(v)
                else:
                    if config.filter_verts_bottom:
                        sel_verts.append(v)

        if config.filter_edges and not config.filter_verts_top and not config.filter_verts_bottom:
            bpy.ops.mesh.select_mode(type='EDGE')
            p1_co = l_p1co
            if mode == 'E':
                p1_co = v0
                p1_no = p1_no_
            elif mode == 'V':
                p1_no = Vector((0, 0, 1))
            else:
                p1_no = P1.normal

            for idx, edg in enumerate(eds_all):
                pt_a = edg.verts[0].co
                pt_b = edg.verts[1].co
                cross_pt = mathutils.geometry.intersect_line_plane(pt_a, pt_b, p1_co, p1_no)
                if cross_pt:
                    pose_pt = mathutils.geometry.intersect_point_line(cross_pt, pt_a, pt_b)
                    if pose_pt[1] <= 1 and pose_pt[1] >= 0:
                        sel_edges.append(edg)

    bm.edges.index_update()
    for v in bm.verts:
        v.select_set(False)
    bm.select_flush(False)
    for ed in sel_edges:
        ed.select = True
    for ed in sel_verts:
        ed.select = True

    bpy.ops.object.mode_set(mode='OBJECT')
    bm.to_mesh(me)
    me.update()
    bm.free()
    bpy.ops.object.mode_set(mode='EDIT')


class Segment():
    def __init__(self):
        self.points = [Vector() for i in range(4)]

    def calc_p1(self, t, b):
        if t == 0: t = 1e-6
        if t == 1: t -= 1e-6

        nt = 1 - t
        nt2 = nt * nt
        t2 = t * t

        p = Vector()
        p.x = (b.x - nt2 * self.points[0].x - t2 * self.points[2].x) / (2 * t * nt)
        p.y = (b.y - nt2 * self.points[0].y - t2 * self.points[2].y) / (2 * t * nt)
        p.z = (b.z - nt2 * self.points[0].z - t2 * self.points[2].z) / (2 * t * nt)
        self.points[1] = p

    def calc(self, t, b):
        nt = 1 - t
        nt2 = nt * nt
        t2 = t * t

        b.x = nt2 * self.points[0].x + 2 * t * nt * self.points[1].x + t2 * self.points[2].x
        b.y = nt2 * self.points[0].y + 2 * t * nt * self.points[1].y + t2 * self.points[2].y
        b.z = nt2 * self.points[0].z + 2 * t * nt * self.points[1].z + t2 * self.points[2].z


def loopResolve(STEP, dist=None):
    def getTBSegment(segment, Pc, T, R, D):
        kk = (1 - T) * 0.5
        t = kk + T
        k_extr = 0
        b = Vector()
        for cycle in range(100):
            segment.calc(t, b)
            d_ = (b - Pc).length - R

            if abs(d_) <= D: return (t, b)

            if kk == k_extr:
                k = -0.5 if d_ > 0 else 0.5
            else:
                k = -1 if d_ > 0 else 1
                k_extr = kk

            kk *= k
            t += kk
            kk = abs(kk)
        return (t, b)

    edit_mode_out()
    edit_mode_in()

    obj = bpy.context.active_object
    me = obj.data

    verts = find_index_of_selected_vertex(me)

    segments_2d = find_all_segments(me, 3)
    if not segments_2d: return False
    # Запускаем 2д-перестроение по сплайну
    edit_mode_out()
    bm = bmesh.new()
    bm.from_mesh(me)
    check_lukap(bm)
    edit_mode_in()

    lv_for_del = []
    old_len_lfd = 0
    old_len_bmv = 0
    bm_verts = []
    remove_edges = []
    set_verts = set(verts)
    act_vert = bm_vert_active_get(bm)[0]
    for i, sort_list_ in enumerate(segments_2d):
        _is_loop = False
        if len(sort_list_) == 2:
            extreme_vs = sort_list_
        else:
            extreme_vs = find_extreme_select_verts(me, sort_list_)
            if not extreme_vs:
                _is_loop = True
                _loc_idx = sort_list_.index(act_vert)
                _sort_list_ = sort_list_[_loc_idx:] + sort_list_[:_loc_idx]
                sort_list_ = _sort_list_

                len_sort_list_ = len(sort_list_)
                _sub_segment_1 = sort_list_[:len_sort_list_ // 2 + 1]
                _sub_segment_2 = sort_list_[len_sort_list_ // 2:] + [sort_list_[0]]
                segments_2d[i] = _sub_segment_1
                segments_2d.insert(i + 1, _sub_segment_2)
                sort_list_ = _sub_segment_1
                if len(sort_list_) == 2:
                    extreme_vs = sort_list_
                else:
                    extreme_vs = find_extreme_select_verts(me, sort_list_)

        if _is_loop:
            sort_list = sort_list_
        else:
            bl_ = list(set(sort_list_) ^ set_verts)
            sort_list = find_all_connected_verts(me, extreme_vs[0], bl_)

        list_length = []
        sum_length = 0.0
        cou_vs = len(sort_list) - 1
        list_koeff = []
        if cou_vs == 1:
            p1co = me.vertices[sort_list[0]].co.copy()
            p3co = me.vertices[sort_list[1]].co.copy()
            p2co = (p1co + p3co) / 2
            sum_length = (p3co - p1co).length
            # list_length = [sum_length / 2, sum_length]
            list_koeff = [0.5, 0.5]
            values = [p1co, p2co, p3co]
        else:
            for sl in range(cou_vs):
                subb = me.vertices[sort_list[sl + 1]].co - me.vertices[sort_list[sl]].co
                sum_length += subb.length
                list_length.append(subb.length)

            for sl in range(cou_vs):
                tmp = list_length[sl] / sum_length
                list_koeff.append(tmp)

            values = [me.vertices[i].co.copy() for i in sort_list]

        n = len(values) - 1
        bezier = [Segment() for _ in range(n)]

        step_ = STEP - 1
        new_vts = []

        if not dist:
            r = sum_length / (step_)
        else:
            r = dist
            step_ = 1e+6

        pi_ = 0
        delta = 0.001
        for i in range(n):
            if i == n - 1: pi_ = 1

            tl = list_koeff[i - pi_]
            tr = list_koeff[i + 1 - pi_]
            tt = tl / (tl + tr)

            bezier[i].points[0] = values[i - pi_]
            b = values[i + 1 - pi_]
            bezier[i].points[2] = values[i + 2 - pi_]
            bezier[i].calc_p1(tt, b)
            bezier[i].points[3] = b

        for j in range(4):
            segment = bezier[0]
            Pc = segment.points[0].copy()
            t = 0
            i = 0
            ii = 0
            iii = 0
            pi_ = 0
            i_virtual = 0
            dr = 0
            old_point = me.vertices[extreme_vs[0]].co.copy()
            while i < len(bezier):
                ii += 1
                segment = bezier[i]
                if i == len(bezier) - 1: pi_ = 1

                if (Pc - segment.points[3 - pi_]).length < r:
                    t = 0 if i < len(bezier) - 2 else t
                    i += 1
                    if i_virtual < step_: i_virtual += 1
                    if i == len(bezier) and j == 3:
                        t, b = getTBSegment(segment, Pc, t, r, delta)
                        if len(new_vts) < step_: new_vts.append(b.copy())
                    continue

                t, b = getTBSegment(segment, Pc, t, r, delta)
                Pc = b
                if i_virtual < step_ + 1:
                    # Pc1 = Pc.copy()
                    i_virtual += 1

                if j == 3:
                    if len(new_vts) < step_: new_vts.append(b.copy())

                iii += 1
                dr += (old_point - Pc).length
                old_point = Pc.copy()

            r = dr / iii
            if dist:
                r = dist

        new_vts.insert(0, me.vertices[extreme_vs[0]].co)

        # В списке new_vts имеем координаты новых вершин
        edit_mode_out()
        lv_for_del.extend([bm.verts[vi] for vi in sort_list])
        for v in new_vts[1:-1]:
            new_v = bm.verts.new(v)
            new_v.select = True
            bm_verts.append(new_v)

        check_lukap(bm)

        v0_insert = lv_for_del.pop(old_len_lfd)
        v1_insert = lv_for_del.pop(-1)
        if len(sort_list) == 2:
            edge = bm.edges.get([v0_insert, v1_insert], False)
            if edge: remove_edges.append(edge)

        bm_verts.insert(old_len_bmv, v0_insert)
        bm_verts.append(v1_insert)
        bm_verts[old_len_bmv].select = True
        bm_verts[-1].select = True
        bm_edges = list(zip(bm_verts[old_len_bmv:-1], bm_verts[1 + old_len_bmv:]))
        old_len_lfd = len(lv_for_del)
        old_len_bmv = len(bm_verts)

        for edge in bm_edges:
            if not bm.edges.get(edge, False):
                ed_ = bm.edges.new(edge)
                ed_.select = True
            else:
                for i, re in enumerate(remove_edges):
                    if edge[0] in re.verts and edge[1] in re.verts:
                        remove_edges.pop(i)
                        break

    check_lukap(bm)
    for e in remove_edges:
        bm.edges.remove(e)

    for v in lv_for_del:
        if v in bm.verts:
            bm.verts.remove(v)

    check_lukap(bm)
    bm.to_mesh(me)
    bm.free()
    edit_mode_in()
    return True


def loopReduce(STEP, mode=1):
    edit_mode_out()
    edit_mode_in()

    obj = bpy.context.active_object
    me = obj.data

    verts = find_index_of_selected_vertex(me)
    cou_vs = len(verts) - 1
    if verts == None or cou_vs <= 0:
        print_error2("Vertices are not selected", "01 loopReduce2")
        return False

    extreme_vs = find_extreme_select_verts(me, verts)
    if mode == 2:
        segments_2d = find_all_segments(me, 3)
        if not segments_2d: return False
        # Запускаем 2д-перестроение по сплайну
        edit_mode_out()
        bm = bmesh.new()
        bm.from_mesh(me)
        check_lukap(bm)
        edit_mode_in()

        lv_for_del = []
        old_len_lfd = 0
        old_len_bmv = 0
        bm_verts = []
        set_verts = set(verts)
        for sort_list_ in segments_2d:
            extreme_vs = find_extreme_select_verts(me, sort_list_)
            bl_ = list(set(sort_list_) ^ set_verts)
            sort_list = find_all_connected_verts(me, extreme_vs[0], bl_)

            list_length = []
            sum_length = 0.0
            cou_vs = len(sort_list) - 1
            for sl in range(cou_vs):
                subb = me.vertices[sort_list[sl + 1]].co - me.vertices[sort_list[sl]].co
                sum_length += subb.length
                list_length.append(subb.length)

            list_koeff = []
            for sl in range(cou_vs):
                tmp = list_length[sl] / sum_length
                list_koeff.append(tmp)

            values = [me.vertices[i].co.copy() for i in sort_list]
            n = len(sort_list) - 1
            bezier = [Segment() for i in range(n)]

            step_ = STEP - 1
            new_vts = []

            last_portions = 0
            last_steps = 0
            T = 1 / step_
            t_ = 0
            moveto = 0
            pi_ = 0
            for i in range(n):
                if i == n - 1: pi_ = 1

                tl = list_koeff[i - pi_]
                tr = list_koeff[i + 1 - pi_]
                tt = tl / (tl + tr)

                bezier[i].points[0] = values[i - pi_]
                b = values[i + 1 - pi_]
                bezier[i].points[2] = values[i + 2 - pi_]
                bezier[i].calc_p1(tt, b)

                portion = moveto + list_koeff[i]
                all_steps = int(portion * step_)
                delta_steps = all_steps - last_steps
                t_ = moveto - last_portions

                step = 0
                for step in range(delta_steps):
                    if i < n - 1:
                        t = (T * (step + 1) - t_) / list_koeff[i - pi_] * tt
                    else:
                        t = (T * (step + 1) - t_) / list_koeff[i - pi_] * tt + tt
                    new_co = Vector()
                    bezier[i].calc(t, new_co)
                    new_vts.append(new_co)

                last_portions += T * delta_steps
                last_steps += delta_steps
                moveto += list_koeff[i - pi_]

            new_vts.insert(0, me.vertices[extreme_vs[0]].co)
            if last_steps < step_:
                new_vts.append(me.vertices[extreme_vs[-1]].co)

            # В списке new_vts имеем координаты новых вершин
            edit_mode_out()
            lv_for_del.extend([bm.verts[vi] for vi in sort_list])
            for v in new_vts[1:-1]:
                new_v = bm.verts.new(v)
                new_v.select = True
                bm_verts.append(new_v)

            check_lukap(bm)
            v0_insert = lv_for_del.pop(old_len_lfd)
            v1_insert = lv_for_del.pop(-1)
            bm_verts.insert(old_len_bmv, v0_insert)
            bm_verts.append(v1_insert)
            bm_verts[old_len_bmv].select = True
            bm_verts[-1].select = True
            bm_edges = list(zip(bm_verts[old_len_bmv:-1], bm_verts[1 + old_len_bmv:]))
            old_len_lfd = len(lv_for_del)
            old_len_bmv = len(bm_verts)
            for edge in bm_edges:
                bm.edges.new(edge)

        check_lukap(bm)
        for v in lv_for_del:
            bm.verts.remove(v)

        check_lukap(bm)
        bm.to_mesh(me)
        bm.free()
        edit_mode_in()
        return True

    mesh = me
    lEdges_select_idx = [e.index for e in mesh.edges if e.select]

    bpy.ops.mesh.select_mode(type='VERT')
    bpy.ops.mesh.select_mode(type='FACE')

    bpy.ops.object.editmode_toggle()
    bpy.ops.object.editmode_toggle()
    lFaces_select = [p for p in mesh.polygons if p.select]
    lEdges_select = [mesh.edges[i] for i in lEdges_select_idx]

    def findNearestPols(pol, sel_pols):
        lEdges_ = [e for e in pol.edge_keys]
        lEdges = list(add(*zip(*lEdges_)))

        lEdges_pols = [p.edge_keys for p in sel_pols if p != pol]
        lEdges_sel_ = [e for e in lEdges_pols]
        tmp = list(*zip(*zip(lEdges_sel_)))
        tmp_ = []
        for line in tmp:
            tmp_.extend(line)

        lEdges_sel = list(add(*zip(*tmp_)))
        lNearest_pols = set(lEdges) & set(lEdges_sel)
        count = len(lNearest_pols)
        return count, list(lNearest_pols)

    def findNearestEdges(sel_pols, sel_edges):
        lEdges_sel_ = [p.edge_keys for p in sel_pols]
        lEdges_sel = []
        lEdges_for_sel = []
        sel_edges_ = [(e.vertices[0], e.vertices[1]) for e in sel_edges]
        sel_edges_.extend([(e.vertices[1], e.vertices[0]) for e in sel_edges])
        for te in lEdges_sel_:
            for e in te:
                if e in lEdges_sel and e in sel_edges_:
                    lEdges_for_sel.append(e)

            lEdges_sel.extend(te)

        lEdges_ = list(set(lEdges_for_sel))
        lEdges = [e.index for e in sel_edges if (e.vertices[0], e.vertices[1]) in lEdges_ or \
                  (e.vertices[1], e.vertices[0]) in lEdges_]
        return lEdges

    def medianaEdge(edge):
        return (mesh.vertices[edge.vertices[0]].co + mesh.vertices[edge.vertices[1]].co) / 2

    def nextEdgeKey(pol, edge_key, sel_edge_keys, sel_pols):
        edge_ = ((edge_key[0], edge_key[1]), (edge_key[1], edge_key[0]))
        edgekeys_in_pol = pol.edge_keys
        next_edge_key = list(set(edgekeys_in_pol) & set(edge_))[0]
        for p in sel_pols:
            if p == pol: continue
            if next_edge_key in p.edge_keys:
                break

        edgekeys_in_pol_next = p.edge_keys
        next_edge_key = list(({next_edge_key} ^ set(edgekeys_in_pol_next)) & set(sel_edge_keys))
        if not next_edge_key: next_edge_key = [False]
        return next_edge_key[0], p

    lEdgesAll = findNearestEdges(lFaces_select, lEdges_select)

    ######## Second part
    ltFaces_z = [(p.center.z, p) for p in lFaces_select]
    ltFaces_sort = sorted(ltFaces_z, key=itemgetter(0), reverse=True)
    tmp_pol = ltFaces_sort[0][1]

    lFaces_select.insert(0, tmp_pol)
    idx = tmp_pol.index
    for pol in lFaces_select:
        test, npls = findNearestPols(pol, lFaces_select)
        if test == 2:
            idx = pol.index
            break

    lEdges_extr_pol = mesh.polygons[idx].edge_keys  # [(v1,v2),(v3,v4)]
    lEdges_extr_pol_ = []
    for ep in lEdges_extr_pol:
        lEdges_extr_pol_.append((ep[1], ep[0]))  # [(v1,v2),(v3,v4), (v2,v1),(v4,v3)]
    lEdges_extr_pol.extend(lEdges_extr_pol_)
    lEdges_pols = [mesh.edges[e].key for e in lEdgesAll]
    edge_extr_pol = list(set(lEdges_extr_pol) & set(lEdges_pols))
    if edge_extr_pol:
        lEdge_idx = [e.index for e in lEdges_select if e.key in edge_extr_pol]
        if lEdge_idx:
            ed_idx = lEdge_idx[0]
            edge_key_cycle = edge_extr_pol[0]
            ltEdges_sort_ = [edge_key_cycle]
            next_pol = mesh.polygons[idx]
            for i in range(len(lEdgesAll) - 1):
                edge_key_cycle, next_pol = nextEdgeKey(next_pol, edge_key_cycle, lEdges_pols, lFaces_select)
                if not edge_key_cycle: break
                ltEdges_sort_.append(edge_key_cycle)

            lCentr_edges = []
            ltEdges_sort = []

            for ed_key in ltEdges_sort_:
                for e in mesh.edges:
                    if e.key == ed_key:
                        ltEdges_sort.append(e)
                        lCentr_edges.append((mesh.vertices[e.vertices[0]].co + \
                                             mesh.vertices[e.vertices[1]].co) / 2)
                        break

            lSpace_edges = []
            for i, ec in enumerate(lCentr_edges[:-1]):
                lSpace_edges.append((ec - lCentr_edges[i + 1]).length)

            allSpace = sum(lSpace_edges)
            stepSpace = allSpace / STEP
            fSpace_ = 0
            new_gran = [ltEdges_sort[0]]
            lNew_gran = []

            for i, ss in enumerate(lSpace_edges):
                edge_next = ltEdges_sort[i + 1]
                fSpace_ += ss
                if fSpace_ < (len(lNew_gran) + 1) * stepSpace or len(new_gran) == 1:
                    new_gran.append(edge_next)
                else:
                    lNew_gran.append(new_gran)
                    new_gran = [edge_next]

            if len(new_gran) > 0:
                if len(lNew_gran) < STEP:
                    lNew_gran.append(new_gran)
                else:
                    if ((lCentr_edges[0] - lCentr_edges[-1]).length > stepSpace):
                        lNew_gran[-1].extend(new_gran)

            lEdgesAllSelect = []
            for new_gran in lNew_gran[:]:
                for ng in new_gran[:-1]:
                    lEdgesAllSelect.append(ng.index)

            lEdgesAllSelect.append(new_gran[-1].index)

            bpy.ops.mesh.select_all(action='DESELECT')
            bpy.ops.mesh.select_mode(type='EDGE')
            bpy.ops.object.mode_set(mode='OBJECT')
            for i_pol in lEdgesAllSelect:
                mesh.edges[i_pol].select = True
            bpy.ops.object.mode_set(mode='EDIT')

    ########## Fourth part
    bpy.ops.mesh.loop_multi_select(ring=False)
    bpy.ops.mesh.delete_edgeloop()


def main_spline(context, mode, influe):
    bpy.ops.object.mode_set(mode='OBJECT')
    bpy.ops.object.mode_set(mode='EDIT')

    obj = bpy.context.active_object
    me = obj.data

    verts = find_index_of_selected_vertex(me)
    cou_vs = len(verts) - 1
    if verts != None and cou_vs > 0:
        extreme_vs = find_extreme_select_verts(me, verts)

        if len(extreme_vs) != 2:
            print_error('Single Loop only')
            print('Error: 01 simple_spline')
            return False

        sort_list = find_all_connected_verts(me, extreme_vs[0], [])
        all_vts_sort_x = [me.vertices[i].co.x for i in sort_list]
        all_vts_sort_y = [me.vertices[i].co.y for i in sort_list]
        all_vts_sort_z = [me.vertices[i].co.z for i in sort_list]

        max_p = [max(all_vts_sort_x), max(all_vts_sort_y), max(all_vts_sort_z)]
        min_p = [min(all_vts_sort_x), min(all_vts_sort_y), min(all_vts_sort_z)]
        diap_p = list(map(lambda a, b: a - b, max_p, min_p))

        if len(sort_list) != len(verts):
            print_error('Incoherent loop')
            print('Error: 020 simple_spline')
            return False

        list_length = []
        sum_length = 0.0
        for sl in range(cou_vs):
            subb = me.vertices[sort_list[sl + 1]].co - me.vertices[sort_list[sl]].co
            sum_length += subb.length
            list_length.append(sum_length)

        list_koeff = []
        for sl in range(cou_vs):
            tmp = list_length[sl] / sum_length
            list_koeff.append(tmp)

        bpy.ops.object.mode_set(mode='OBJECT')
        bm = bmesh.new()
        bm.from_mesh(me)
        check_lukap(bm)

        pa_idx = bm_vert_active_get(bm)[0]
        if pa_idx == None:
            print_error('Active vert is not detected')
            print('Error: 030 simple_spline')
            return False

        pa_sort = sort_list.index(pa_idx)
        if pa_sort == 0: pa_sort = 1
        pa_perc = list_koeff[pa_sort - 1]
        p0_ = me.vertices[sort_list[0]].co
        p1_ = me.vertices[pa_idx].co
        p2_ = me.vertices[sort_list[-1]].co

        if mode[3]:
            l = len(list_koeff)
            d = 1 / l
            list_koeff = list(map(lambda n: d * n, list(range(1, l + 1))))

        if mode[0]:
            all_vts_sort = [me.vertices[i].co.x for i in sort_list]
            p0 = p0_.x
            p1 = p1_.x - p0
            p2 = p2_.x - p0

            t = pa_perc
            if p1 == 0 or p1 == p2:
                new_vts = list(map(lambda t: p2 * t ** 2, list_koeff))
            else:
                b = (p1 - pa_perc ** 2 * p2) / (2 * pa_perc * (1 - pa_perc) + 1e-8)
                new_vts = list(map(lambda t: 2 * b * t * (1 - t) + p2 * t ** 2, list_koeff))

            for idx in range(cou_vs):
                me.vertices[sort_list[idx + 1]].co.x += (new_vts[idx] + p0 - me.vertices[
                    sort_list[idx + 1]].co.x) * influe

        if mode[1]:
            all_vts_sort = [me.vertices[i].co.y for i in sort_list]
            p0 = p0_.y
            p1 = p1_.y - p0
            p2 = p2_.y - p0

            b = (p1 - pa_perc ** 2 * p2) / (2 * pa_perc * (1 - pa_perc) + 1e-8)
            new_vts = list(map(lambda t: 2 * b * t * (1 - t) + p2 * t ** 2, list_koeff))

            for idx in range(cou_vs):
                me.vertices[sort_list[idx + 1]].co.y += (new_vts[idx] + p0 - me.vertices[
                    sort_list[idx + 1]].co.y) * influe

        if mode[2]:
            all_vts_sort = [me.vertices[i].co.z for i in sort_list]
            p0 = p0_.z
            p1 = p1_.z - p0
            p2 = p2_.z - p0

            b = (p1 - pa_perc ** 2 * p2) / (2 * pa_perc * (1 - pa_perc) + 1e-8)
            new_vts = list(map(lambda t: 2 * b * t * (1 - t) + p2 * t ** 2, list_koeff))

            for idx in range(cou_vs):
                me.vertices[sort_list[idx + 1]].co.z += (new_vts[idx] + p0 - me.vertices[
                    sort_list[idx + 1]].co.z) * influe

        me.update()
        bm.free()

        bpy.ops.object.mode_set(mode='EDIT')

    return True


def main_B_spline(context, mode, influe):
    global steps_smoose
    bpy.ops.object.mode_set(mode='OBJECT')
    bpy.ops.object.mode_set(mode='EDIT')

    obj = bpy.context.active_object
    me = obj.data

    verts = find_index_of_selected_vertex(me)
    cou_vs = len(verts) - 1
    if verts != None and cou_vs > 0:
        extreme_vs = find_extreme_select_verts(me, verts)

        if len(extreme_vs) != 2:
            print_error('Single Loop only')
            print('Error: 01 B_spline')
            return False

        sort_list = find_all_connected_verts(me, extreme_vs[0], [])
        all_vts_sort_x = [me.vertices[i].co.x for i in sort_list]
        all_vts_sort_y = [me.vertices[i].co.y for i in sort_list]
        all_vts_sort_z = [me.vertices[i].co.z for i in sort_list]

        max_p = [max(all_vts_sort_x), max(all_vts_sort_y), max(all_vts_sort_z)]
        min_p = [min(all_vts_sort_x), min(all_vts_sort_y), min(all_vts_sort_z)]
        diap_p = list(map(lambda a, b: a - b, max_p, min_p))

        if len(sort_list) != len(verts):
            print_error('Incoherent loop')
            print('Error: 020 B_spline')
            return False

        list_length = []
        sum_length = 0.0
        for sl in range(cou_vs - 2):
            subb = me.vertices[sort_list[sl + 2]].co - me.vertices[sort_list[sl + 1]].co
            sum_length += subb.length
            list_length.append(sum_length)

        list_koeff = []
        for sl in range(cou_vs - 2):
            tmp = list_length[sl] / sum_length
            list_koeff.append(tmp)

        bpy.ops.object.mode_set(mode='OBJECT')
        bm = bmesh.new()
        bm.from_mesh(me)
        check_lukap(bm)

        pa_idx = bm_vert_active_get(bm)[0]
        if pa_idx == None:
            print_error('Active vert is not detected')
            print('Error: 030 B_spline')
            return False

        pa_sort = sort_list.index(pa_idx)
        if pa_sort < 2: pa_sort = 2
        if pa_sort > len(sort_list) - 3: pa_sort = len(sort_list) - 3
        pa_idx = sort_list[pa_sort]
        pa_perc = list_koeff[pa_sort - 2]
        p0_ = me.vertices[sort_list[1]].co
        p1_ = me.vertices[pa_idx].co
        p2_ = me.vertices[sort_list[-2]].co

        kn1_ = me.vertices[sort_list[0]].co
        kn2_ = me.vertices[sort_list[-1]].co
        nkn1_ = p1_ - kn1_ + p1_
        nkn2_ = p2_ - kn2_ + p2_

        if mode[3]:
            l = len(list_koeff)
            d = 1 / l
            list_koeff = list(map(lambda n: d * n, list(range(1, l + 1))))

        if mode[0]:
            all_vts_sort = [me.vertices[i].co.x for i in sort_list]
            p0 = p0_.x
            p1 = p1_.x - p0
            p2 = p2_.x - p0
            knot_1 = nkn1_.x - p0
            knot_2 = nkn2_.x - p0

            t = pa_perc
            b = (p1 - (4 * knot_1 * t * (1 - t) ** 3) - (4 * t ** 3 * (1 - t) * knot_2 + p2 * t ** 4)) / (
                    4 * t ** 2 * (1 - t) ** 2 + 1e-8)
            new_vts = list(map(lambda t: 4 * knot_1 * t * (1 - t) ** 3 + 4 * b * t ** 2 * (1 - t) ** 2 + 4 * t ** 3 * (
                    1 - t) * knot_2 + p2 * t ** 4, list_koeff))

            if mode[3]:
                for c in range(steps_smoose):
                    new_vts_ = [0] + new_vts
                    V = [vi for vi in new_vts_]
                    P = list(map(lambda x, y: abs(y - x), V[:-1], V[1:]))
                    L = sum(P)
                    lp = len(P)
                    d = L / lp
                    l_ = list(map(lambda y: d * y / L, list(range(1, lp + 1))))
                    l = list(map(lambda x: x / L, P))

                    tmp = 0
                    for i in range(lp):
                        tmp += l[i]
                        m = l_[i] / tmp
                        list_koeff[i] = m * list_koeff[i]
                    new_vts = list(map(
                        lambda t: 4 * knot_1 * t * (1 - t) ** 3 + 4 * b * t ** 2 * (1 - t) ** 2 + 4 * t ** 3 * (
                                1 - t) * knot_2 + p2 * t ** 4, list_koeff))

            for idx in range(cou_vs - 2):
                me.vertices[sort_list[idx + 2]].co.x += (new_vts[idx] + p0 - me.vertices[
                    sort_list[idx + 2]].co.x) * influe

        if mode[1]:
            all_vts_sort = [me.vertices[i].co.y for i in sort_list]
            p0 = p0_.y
            p1 = p1_.y - p0
            p2 = p2_.y - p0
            knot_1 = nkn1_.y - p0
            knot_2 = nkn2_.y - p0

            t = pa_perc
            b = (p1 - (4 * knot_1 * t * (1 - t) ** 3) - (4 * t ** 3 * (1 - t) * knot_2 + p2 * t ** 4)) / (
                    4 * t ** 2 * (1 - t) ** 2 + 1e-8)
            new_vts = list(map(lambda t: 4 * knot_1 * t * (1 - t) ** 3 + 4 * b * t ** 2 * (1 - t) ** 2 + 4 * t ** 3 * (
                    1 - t) * knot_2 + p2 * t ** 4, list_koeff))

            if mode[3]:
                for c in range(steps_smoose):
                    new_vts_ = [0] + new_vts
                    V = [vi for vi in new_vts_]
                    P = list(map(lambda x, y: abs(y - x), V[:-1], V[1:]))
                    L = sum(P)
                    lp = len(P)
                    d = L / lp
                    l_ = list(map(lambda y: d * y / L, list(range(1, lp + 1))))
                    l = list(map(lambda x: x / L, P))

                    tmp = 0
                    for i in range(lp):
                        tmp += l[i]
                        m = l_[i] / tmp
                        list_koeff[i] = m * list_koeff[i]
                    new_vts = list(map(
                        lambda t: 4 * knot_1 * t * (1 - t) ** 3 + 4 * b * t ** 2 * (1 - t) ** 2 + 4 * t ** 3 * (
                                1 - t) * knot_2 + p2 * t ** 4, list_koeff))

            for idx in range(cou_vs - 2):
                me.vertices[sort_list[idx + 2]].co.y += (new_vts[idx] + p0 - me.vertices[
                    sort_list[idx + 2]].co.y) * influe

        if mode[2]:
            all_vts_sort = [me.vertices[i].co.z for i in sort_list]
            p0 = p0_.z
            p1 = p1_.z - p0
            p2 = p2_.z - p0
            knot_1 = nkn1_.z - p0
            knot_2 = nkn2_.z - p0

            t = pa_perc
            b = (p1 - (4 * knot_1 * t * (1 - t) ** 3) - (4 * t ** 3 * (1 - t) * knot_2 + p2 * t ** 4)) / (
                    4 * t ** 2 * (1 - t) ** 2 + 1e-8)
            new_vts = list(map(lambda t: 4 * knot_1 * t * (1 - t) ** 3 + 4 * b * t ** 2 * (1 - t) ** 2 + 4 * t ** 3 * (
                    1 - t) * knot_2 + p2 * t ** 4, list_koeff))

            if mode[3]:
                for c in range(steps_smoose):
                    new_vts_ = [0] + new_vts
                    V = [vi for vi in new_vts_]
                    P = list(map(lambda x, y: abs(y - x), V[:-1], V[1:]))
                    L = sum(P)
                    lp = len(P)
                    d = L / lp
                    l_ = list(map(lambda y: d * y / L, list(range(1, lp + 1))))
                    l = list(map(lambda x: x / L, P))

                    tmp = 0
                    for i in range(lp):
                        tmp += l[i]
                        m = l_[i] / tmp
                        list_koeff[i] = m * list_koeff[i]
                    new_vts = list(map(
                        lambda t: 4 * knot_1 * t * (1 - t) ** 3 + 4 * b * t ** 2 * (1 - t) ** 2 + 4 * t ** 3 * (
                                1 - t) * knot_2 + p2 * t ** 4, list_koeff))

            for idx in range(cou_vs - 2):
                me.vertices[sort_list[idx + 2]].co.z += (new_vts[idx] + p0 - me.vertices[
                    sort_list[idx + 2]].co.z) * influe

        me.update()
        bm.free()

        bpy.ops.object.mode_set(mode='EDIT')

    return True


def main_B_spline_2(context, mode, influe):
    global steps_smoose
    bpy.ops.object.mode_set(mode='OBJECT')
    bpy.ops.object.mode_set(mode='EDIT')

    obj = bpy.context.active_object
    me = obj.data

    verts = find_index_of_selected_vertex(me)
    cou_vs = len(verts) - 1
    if verts != None and cou_vs > 0:
        extreme_vs = find_extreme_select_verts(me, verts)

        if len(extreme_vs) != 2:
            print_error('Single Loop only')
            print('Error: 01 B_spline')
            return False

        sort_list = find_all_connected_verts(me, extreme_vs[0], [])
        all_vts_sort_x = [me.vertices[i].co.x for i in sort_list]
        all_vts_sort_y = [me.vertices[i].co.y for i in sort_list]
        all_vts_sort_z = [me.vertices[i].co.z for i in sort_list]

        max_p = [max(all_vts_sort_x), max(all_vts_sort_y), max(all_vts_sort_z)]
        min_p = [min(all_vts_sort_x), min(all_vts_sort_y), min(all_vts_sort_z)]
        diap_p = list(map(lambda a, b: a - b, max_p, min_p))

        if len(sort_list) != len(verts):
            print_error('Incoherent loop')
            print('Error: 020 B_spline')
            return False

        list_length = []
        sum_length = 0.0
        for sl in range(cou_vs):
            subb = me.vertices[sort_list[sl + 1]].co - me.vertices[sort_list[sl]].co
            sum_length += subb.length
            list_length.append(sum_length)

        list_koeff = []
        for sl in range(cou_vs):
            tmp = list_length[sl] / sum_length
            list_koeff.append(tmp)

        bpy.ops.object.mode_set(mode='OBJECT')
        bm = bmesh.new()
        bm.from_mesh(me)
        check_lukap(bm)

        pa_idx = bm_vert_active_get(bm)[0]
        if pa_idx == None:
            print_error('Active vert is not detected')
            print('Error: 030 B_spline')
            return False

        list_koeff = [0] + list_koeff
        pa_sort = sort_list.index(pa_idx)
        if pa_sort == 0:
            pa_perc = 0
            kn1_i = sort_list[0]
            kn2_i = sort_list[pa_sort + 1]
        elif pa_sort == len(sort_list) - 1:
            pa_perc = 1.0
            kn1_i = sort_list[pa_sort - 1]
            kn2_i = sort_list[-1]
        else:
            kn1_i = sort_list[pa_sort - 1]
            kn2_i = sort_list[pa_sort + 1]
            pa_perc = list_koeff[pa_sort]

        kn1_ = me.vertices[kn1_i].co
        kn2_ = me.vertices[kn2_i].co

        p0_ = me.vertices[sort_list[0]].co
        p1_ = me.vertices[pa_idx].co
        p2_ = me.vertices[sort_list[-1]].co

        if mode[3]:
            l = len(list_koeff) - 1
            d = 1 / l
            list_koeff = list(map(lambda n: d * n, list(range(0, l + 1))))

        if mode[0]:
            p0 = p0_.x
            p1 = p1_.x - p0
            p2 = p2_.x - p0
            knot_1 = kn1_.x - p0
            knot_2 = kn2_.x - p0

            t = pa_perc
            if knot_1 == 0 and p1 != 0:
                b = (p1 - (3 * knot_2 * t ** 2 * (1 - t) + p2 * t ** 3)) / (3 * t * (1 - t) ** 2 + 1e-8)
                new_vts = list(
                    map(lambda t: 3 * b * t * (1 - t) ** 2 + 3 * knot_2 * t ** 2 * (1 - t) + p2 * t ** 3, list_koeff))
            elif p1 == 0:
                new_vts = list(map(lambda t: 2 * knot_2 * t * (1 - t) + p2 * t ** 2, list_koeff))
            elif knot_2 == p2 and p1 != p2:
                b = (p1 - (3 * knot_1 * t * (1 - t) ** 2 + p2 * t ** 3)) / (3 * t ** 2 * (1 - t) + 1e-8)
                new_vts = list(
                    map(lambda t: 3 * knot_1 * t * (1 - t) ** 2 + 3 * b * t ** 2 * (1 - t) + p2 * t ** 3, list_koeff))
            elif p1 == p2:
                new_vts = list(map(lambda t: 2 * knot_1 * t * (1 - t) + p2 * t ** 2, list_koeff))
            else:
                b = (p1 - (4 * knot_1 * t * (1 - t) ** 3 + 4 * t ** 3 * (1 - t) * knot_2 + p2 * t ** 4)) / (
                        4 * t ** 2 * (1 - t) ** 2 + 1e-8)
                new_vts = list(map(
                    lambda t: 4 * knot_1 * t * (1 - t) ** 3 + 4 * b * t ** 2 * (1 - t) ** 2 + 4 * t ** 3 * (
                            1 - t) * knot_2 + p2 * t ** 4, list_koeff))

            if mode[3]:
                for c in range(steps_smoose):
                    new_vts_ = new_vts
                    V = [vi for vi in new_vts_]
                    P = list(map(lambda x, y: abs(y - x), V[:-1], V[1:]))
                    L = sum(P)
                    lp = len(P)
                    d = L / lp
                    l_ = list(map(lambda y: d * y / L, list(range(1, lp + 1))))
                    l = list(map(lambda x: x / L, P))

                    tmp = 1e-8
                    for i in range(lp):
                        tmp += l[i]
                        m = l_[i] / tmp
                        list_koeff[i] = m * list_koeff[i]

                    if knot_1 == 0 and p1 != 0:
                        b = (p1 - (3 * knot_2 * t ** 2 * (1 - t) + p2 * t ** 3)) / (3 * t * (1 - t) ** 2 + 1e-8)
                        new_vts = list(
                            map(lambda t: 3 * b * t * (1 - t) ** 2 + 3 * knot_2 * t ** 2 * (1 - t) + p2 * t ** 3,
                                list_koeff))
                    elif p1 == 0:
                        new_vts = list(map(lambda t: 2 * knot_2 * t * (1 - t) + p2 * t ** 2, list_koeff))
                    elif knot_2 == p2 and p1 != p2:
                        b = (p1 - (3 * knot_1 * t * (1 - t) ** 2 + p2 * t ** 3)) / (3 * t ** 2 * (1 - t) + 1e-8)
                        new_vts = list(
                            map(lambda t: 3 * knot_1 * t * (1 - t) ** 2 + 3 * b * t ** 2 * (1 - t) + p2 * t ** 3,
                                list_koeff))
                    elif p1 == p2:
                        new_vts = list(map(lambda t: 2 * knot_1 * t * (1 - t) + p2 * t ** 2, list_koeff))
                    else:
                        b = (p1 - (4 * knot_1 * t * (1 - t) ** 3 + 4 * t ** 3 * (1 - t) * knot_2 + p2 * t ** 4)) / (
                                4 * t ** 2 * (1 - t) ** 2 + 1e-8)
                        new_vts = list(map(
                            lambda t: 4 * knot_1 * t * (1 - t) ** 3 + 4 * b * t ** 2 * (1 - t) ** 2 + 4 * t ** 3 * (
                                    1 - t) * knot_2 + p2 * t ** 4, list_koeff))

            for idx in range(cou_vs + 1):
                me.vertices[sort_list[idx]].co.x += (new_vts[idx] + p0 - me.vertices[sort_list[idx]].co.x) * influe

        if mode[1]:
            p0 = p0_.y
            p1 = p1_.y - p0
            p2 = p2_.y - p0
            knot_1 = kn1_.y - p0
            knot_2 = kn2_.y - p0

            t = pa_perc
            if knot_1 == 0 and p1 != 0:
                b = (p1 - (3 * knot_2 * t ** 2 * (1 - t) + p2 * t ** 3)) / (3 * t * (1 - t) ** 2 + 1e-8)
                new_vts = list(
                    map(lambda t: 3 * b * t * (1 - t) ** 2 + 3 * knot_2 * t ** 2 * (1 - t) + p2 * t ** 3, list_koeff))
            elif p1 == 0:
                new_vts = list(map(lambda t: 2 * knot_2 * t * (1 - t) + p2 * t ** 2, list_koeff))
            elif knot_2 == p2 and p1 != p2:
                b = (p1 - (3 * knot_1 * t * (1 - t) ** 2 + p2 * t ** 3)) / (3 * t ** 2 * (1 - t) + 1e-8)
                new_vts = list(
                    map(lambda t: 3 * knot_1 * t * (1 - t) ** 2 + 3 * b * t ** 2 * (1 - t) + p2 * t ** 3, list_koeff))
            elif p1 == p2:
                new_vts = list(map(lambda t: 2 * knot_1 * t * (1 - t) + p2 * t ** 2, list_koeff))
            else:
                b = (p1 - (4 * knot_1 * t * (1 - t) ** 3 + 4 * t ** 3 * (1 - t) * knot_2 + p2 * t ** 4)) / (
                        4 * t ** 2 * (1 - t) ** 2 + 1e-8)
                new_vts = list(map(
                    lambda t: 4 * knot_1 * t * (1 - t) ** 3 + 4 * b * t ** 2 * (1 - t) ** 2 + 4 * t ** 3 * (
                            1 - t) * knot_2 + p2 * t ** 4, list_koeff))

            if mode[3]:
                for c in range(steps_smoose):
                    new_vts_ = new_vts
                    V = [vi for vi in new_vts_]
                    P = list(map(lambda x, y: abs(y - x), V[:-1], V[1:]))
                    L = sum(P)
                    lp = len(P)
                    d = L / lp
                    l_ = list(map(lambda y: d * y / L, list(range(1, lp + 1))))
                    l = list(map(lambda x: x / L, P))

                    tmp = 1e-8
                    for i in range(lp):
                        tmp += l[i]
                        m = l_[i] / tmp
                        list_koeff[i] = m * list_koeff[i]

                    if knot_1 == 0 and p1 != 0:
                        b = (p1 - (3 * knot_2 * t ** 2 * (1 - t) + p2 * t ** 3)) / (3 * t * (1 - t) ** 2 + 1e-8)
                        new_vts = list(
                            map(lambda t: 3 * b * t * (1 - t) ** 2 + 3 * knot_2 * t ** 2 * (1 - t) + p2 * t ** 3,
                                list_koeff))
                    elif p1 == 0:
                        new_vts = list(map(lambda t: 2 * knot_2 * t * (1 - t) + p2 * t ** 2, list_koeff))
                    elif knot_2 == p2 and p1 != p2:
                        b = (p1 - (3 * knot_1 * t * (1 - t) ** 2 + p2 * t ** 3)) / (3 * t ** 2 * (1 - t) + 1e-8)
                        new_vts = list(
                            map(lambda t: 3 * knot_1 * t * (1 - t) ** 2 + 3 * b * t ** 2 * (1 - t) + p2 * t ** 3,
                                list_koeff))
                    elif p1 == p2:
                        new_vts = list(map(lambda t: 2 * knot_1 * t * (1 - t) + p2 * t ** 2, list_koeff))
                    else:
                        b = (p1 - (4 * knot_1 * t * (1 - t) ** 3 + 4 * t ** 3 * (1 - t) * knot_2 + p2 * t ** 4)) / (
                                4 * t ** 2 * (1 - t) ** 2 + 1e-8)
                        new_vts = list(map(
                            lambda t: 4 * knot_1 * t * (1 - t) ** 3 + 4 * b * t ** 2 * (1 - t) ** 2 + 4 * t ** 3 * (
                                    1 - t) * knot_2 + p2 * t ** 4, list_koeff))

            for idx in range(cou_vs + 1):
                me.vertices[sort_list[idx]].co.y += (new_vts[idx] + p0 - me.vertices[sort_list[idx]].co.y) * influe

        if mode[2]:
            p0 = p0_.z
            p1 = p1_.z - p0
            p2 = p2_.z - p0
            knot_1 = kn1_.z - p0
            knot_2 = kn2_.z - p0

            t = pa_perc
            if knot_1 == 0 and p1 != 0:
                b = (p1 - (3 * knot_2 * t ** 2 * (1 - t) + p2 * t ** 3)) / (3 * t * (1 - t) ** 2 + 1e-8)
                new_vts = list(
                    map(lambda t: 3 * b * t * (1 - t) ** 2 + 3 * knot_2 * t ** 2 * (1 - t) + p2 * t ** 3, list_koeff))
            elif p1 == 0:
                new_vts = list(map(lambda t: 2 * knot_2 * t * (1 - t) + p2 * t ** 2, list_koeff))
            elif knot_2 == p2 and p1 != p2:
                b = (p1 - (3 * knot_1 * t * (1 - t) ** 2 + p2 * t ** 3)) / (3 * t ** 2 * (1 - t) + 1e-8)
                new_vts = list(
                    map(lambda t: 3 * knot_1 * t * (1 - t) ** 2 + 3 * b * t ** 2 * (1 - t) + p2 * t ** 3, list_koeff))
            elif p1 == p2:
                new_vts = list(map(lambda t: 2 * knot_1 * t * (1 - t) + p2 * t ** 2, list_koeff))
            else:
                b = (p1 - (4 * knot_1 * t * (1 - t) ** 3 + 4 * t ** 3 * (1 - t) * knot_2 + p2 * t ** 4)) / (
                        4 * t ** 2 * (1 - t) ** 2 + 1e-8)
                new_vts = list(map(
                    lambda t: 4 * knot_1 * t * (1 - t) ** 3 + 4 * b * t ** 2 * (1 - t) ** 2 + 4 * t ** 3 * (
                            1 - t) * knot_2 + p2 * t ** 4, list_koeff))

            if mode[3]:
                for c in range(steps_smoose):
                    new_vts_ = new_vts
                    V = [vi for vi in new_vts_]
                    P = list(map(lambda x, y: abs(y - x), V[:-1], V[1:]))
                    L = sum(P)
                    lp = len(P)
                    d = L / lp
                    l_ = list(map(lambda y: d * y / L, list(range(1, lp + 1))))
                    l = list(map(lambda x: x / L, P))

                    tmp = 1e-8
                    for i in range(lp):
                        tmp += l[i]
                        m = l_[i] / tmp
                        list_koeff[i] = m * list_koeff[i]
                    if knot_1 == 0 and p1 != 0:
                        b = (p1 - (3 * knot_2 * t ** 2 * (1 - t) + p2 * t ** 3)) / (3 * t * (1 - t) ** 2 + 1e-8)
                        new_vts = list(
                            map(lambda t: 3 * b * t * (1 - t) ** 2 + 3 * knot_2 * t ** 2 * (1 - t) + p2 * t ** 3,
                                list_koeff))
                    elif p1 == 0:
                        new_vts = list(map(lambda t: 2 * knot_2 * t * (1 - t) + p2 * t ** 2, list_koeff))
                    elif knot_2 == p2 and p1 != p2:
                        b = (p1 - (3 * knot_1 * t * (1 - t) ** 2 + p2 * t ** 3)) / (3 * t ** 2 * (1 - t) + 1e-8)
                        new_vts = list(
                            map(lambda t: 3 * knot_1 * t * (1 - t) ** 2 + 3 * b * t ** 2 * (1 - t) + p2 * t ** 3,
                                list_koeff))
                    elif p1 == p2:
                        new_vts = list(map(lambda t: 2 * knot_1 * t * (1 - t) + p2 * t ** 2, list_koeff))
                    else:
                        b = (p1 - (4 * knot_1 * t * (1 - t) ** 3 + 4 * t ** 3 * (1 - t) * knot_2 + p2 * t ** 4)) / (
                                4 * t ** 2 * (1 - t) ** 2 + 1e-8)
                        new_vts = list(map(
                            lambda t: 4 * knot_1 * t * (1 - t) ** 3 + 4 * b * t ** 2 * (1 - t) ** 2 + 4 * t ** 3 * (
                                    1 - t) * knot_2 + p2 * t ** 4, list_koeff))

            for idx in range(cou_vs + 1):
                me.vertices[sort_list[idx]].co.z += (new_vts[idx] + p0 - me.vertices[sort_list[idx]].co.z) * influe

        me.update()
        bm.free()

        bpy.ops.object.mode_set(mode='EDIT')

    return True


def main_Basier_mid(context, mode, influe):
    global steps_smoose
    bpy.ops.object.mode_set(mode='OBJECT')
    bpy.ops.object.mode_set(mode='EDIT')

    obj = bpy.context.active_object
    me = obj.data

    verts = find_index_of_selected_vertex(me)
    cou_vs = len(verts) - 1
    if verts != None and cou_vs > 0:
        extreme_vs = find_extreme_select_verts(me, verts)

        if len(extreme_vs) != 2:
            print_error('Single Loop only')
            print('Error: 01 Basier_mid')
            return False

        sort_list = find_all_connected_verts(me, extreme_vs[0], [])
        all_vts_sort_x = [me.vertices[i].co.x for i in sort_list]
        all_vts_sort_y = [me.vertices[i].co.y for i in sort_list]
        all_vts_sort_z = [me.vertices[i].co.z for i in sort_list]

        max_p = [max(all_vts_sort_x), max(all_vts_sort_y), max(all_vts_sort_z)]
        min_p = [min(all_vts_sort_x), min(all_vts_sort_y), min(all_vts_sort_z)]
        diap_p = list(map(lambda a, b: a - b, max_p, min_p))

        if len(sort_list) != len(verts):
            print_error('Incoherent loop')
            print('Error: 020 Basier_mid')
            return False

        bpy.ops.object.mode_set(mode='OBJECT')
        bm = bmesh.new()
        bm.from_mesh(me)
        check_lukap(bm)

        pa_idx = bm_vert_active_get(bm)[0]
        if pa_idx == None:
            bm.free()
            print_error('Active vert is not detected')
            print('Error: 030 Basier_mid')
            return False

        pa_sort = sort_list.index(pa_idx)

        list_length_a = []
        list_length_b = []
        sum_length_a = 0.0
        sum_length_b = 0.0
        for sl in range(pa_sort - 1):
            subb = me.vertices[sort_list[sl + 1]].co - me.vertices[sort_list[sl]].co
            sum_length_a += subb.length
            list_length_a.append(sum_length_a)
        for sl in range(cou_vs - pa_sort - 1):
            subb = me.vertices[sort_list[sl + 2 + pa_sort]].co - me.vertices[sort_list[sl + 1 + pa_sort]].co
            sum_length_b += subb.length
            list_length_b.append(sum_length_b)

        list_koeff_a = []
        list_koeff_b = []
        for sl in range(len(list_length_a)):
            tmp = list_length_a[sl] / sum_length_a
            list_koeff_a.append(tmp)
        for sl in range(len(list_length_b)):
            tmp = list_length_b[sl] / sum_length_b
            list_koeff_b.append(tmp)

        list_koeff_a = [0] + list_koeff_a
        list_koeff_b = [0] + list_koeff_b

        if pa_sort == 0:
            kn1_i = sort_list[0]
            kn2_i = sort_list[pa_sort + 1]
        elif pa_sort == len(sort_list) - 1:
            kn1_i = sort_list[pa_sort - 1]
            kn2_i = sort_list[-1]
        else:
            kn1_i = sort_list[pa_sort - 1]
            kn2_i = sort_list[pa_sort + 1]

        nkn1_ = me.vertices[kn1_i].co
        nkn2_ = me.vertices[kn2_i].co

        p0_ = me.vertices[sort_list[0]].co
        p1_ = me.vertices[pa_idx].co
        p2_ = me.vertices[sort_list[-1]].co

        kn1_ = nkn1_ - p1_ + nkn1_
        kn2_ = nkn2_ - p1_ + nkn2_

        if mode[3]:
            la = len(list_koeff_a) - 1
            lb = len(list_koeff_b) - 1
            if la == 0:
                da = 0
            else:
                da = 1 / la

            if lb == 0:
                db = 0
            else:
                db = 1 / lb

            list_koeff_a = list(map(lambda n: da * n, list(range(0, la + 1))))
            list_koeff_b = list(map(lambda n: db * n, list(range(0, lb + 1))))

        if mode[0]:
            p0 = p0_.x
            p1 = p1_.x - p0
            p2 = p2_.x - p0
            knot_1 = kn1_.x - p0
            knot_2 = kn2_.x - p0
            pA = nkn1_.x - p0
            pB = nkn2_.x - p0
            nkn1 = nkn1_.x - p0
            nkn2 = nkn2_.x - p0

            if nkn1 == 0 or p1 == 0:
                new_vts_a = []
                new_vts_b = list(
                    map(lambda t: pB * (1 - t) ** 2 + 2 * knot_2 * t * (1 - t) + p2 * t ** 2, list_koeff_b))
            elif nkn2 == p2 or p1 == p2:
                new_vts_a = list(map(lambda t: 2 * knot_1 * t * (1 - t) + pA * t ** 2, list_koeff_a))
                new_vts_b = []
            else:
                new_vts_a = list(map(lambda t: 2 * knot_1 * t * (1 - t) + pA * t ** 2, list_koeff_a))
                new_vts_b = list(
                    map(lambda t: pB * (1 - t) ** 2 + 2 * knot_2 * t * (1 - t) + p2 * t ** 2, list_koeff_b))

            if mode[3]:
                for c in range(steps_smoose):
                    new_vts_ = new_vts_a
                    V = [vi for vi in new_vts_]
                    P = list(map(lambda x, y: abs(y - x), V[:-1], V[1:]))
                    L = sum(P)
                    lp = len(P)
                    if lp > 0:
                        d = L / lp
                        l_ = list(map(lambda y: d * y / L, list(range(1, lp + 1))))
                        l = list(map(lambda x: x / L, P))

                        tmp = 1e-8
                        for i in range(lp):
                            tmp += l[i]
                            m = l_[i] / tmp
                            list_koeff_a[i] = m * list_koeff_a[i]
                        if nkn1 == 0 or p1 == 0:
                            new_vts_a = []
                            new_vts_b = list(
                                map(lambda t: pB * (1 - t) ** 2 + 2 * knot_2 * t * (1 - t) + p2 * t ** 2, list_koeff_b))
                        elif nkn2 == p2 or p1 == p2:
                            new_vts_a = list(map(lambda t: 2 * knot_1 * t * (1 - t) + pA * t ** 2, list_koeff_a))
                            new_vts_b = []
                        else:
                            new_vts_a = list(map(lambda t: 2 * knot_1 * t * (1 - t) + pA * t ** 2, list_koeff_a))
                            new_vts_b = list(
                                map(lambda t: pB * (1 - t) ** 2 + 2 * knot_2 * t * (1 - t) + p2 * t ** 2, list_koeff_b))

                    new_vts_ = new_vts_b
                    V = [vi for vi in new_vts_]
                    P = list(map(lambda x, y: abs(y - x), V[:-1], V[1:]))
                    L = sum(P)
                    lp = len(P)
                    if lp > 0:
                        d = L / lp
                        l_ = list(map(lambda y: d * y / L, list(range(1, lp + 1))))
                        l = list(map(lambda x: x / L, P))

                        tmp = 1e-8
                        for i in range(lp):
                            tmp += l[i]
                            m = l_[i] / tmp
                            list_koeff_b[i] = m * list_koeff_b[i]
                        if nkn1 == 0 or p1 == 0:
                            new_vts_a = []
                            new_vts_b = list(
                                map(lambda t: pB * (1 - t) ** 2 + 2 * knot_2 * t * (1 - t) + p2 * t ** 2, list_koeff_b))
                        elif nkn2 == p2 or p1 == p2:
                            new_vts_a = list(map(lambda t: 2 * knot_1 * t * (1 - t) + pA * t ** 2, list_koeff_a))
                            new_vts_b = []
                        else:
                            new_vts_a = list(map(lambda t: 2 * knot_1 * t * (1 - t) + pA * t ** 2, list_koeff_a))
                            new_vts_b = list(
                                map(lambda t: pB * (1 - t) ** 2 + 2 * knot_2 * t * (1 - t) + p2 * t ** 2, list_koeff_b))

            if new_vts_a:
                for idx in range(pa_sort):
                    me.vertices[sort_list[idx]].co.x += (new_vts_a[idx] + p0 - me.vertices[
                        sort_list[idx]].co.x) * influe
            if new_vts_b:
                for idx in range(cou_vs - pa_sort):
                    me.vertices[sort_list[idx + pa_sort + 1]].co.x += (new_vts_b[idx] + p0 - \
                                                                       me.vertices[
                                                                           sort_list[idx + pa_sort + 1]].co.x) * influe

        if mode[1]:
            p0 = p0_.y
            p1 = p1_.y - p0
            p2 = p2_.y - p0
            knot_1 = kn1_.y - p0
            knot_2 = kn2_.y - p0
            pA = nkn1_.y - p0
            pB = nkn2_.y - p0
            nkn1 = nkn1_.y - p0
            nkn2 = nkn2_.y - p0

            if nkn1 == 0 or p1 == 0:
                new_vts_a = []
                new_vts_b = list(
                    map(lambda t: pB * (1 - t) ** 2 + 2 * knot_2 * t * (1 - t) + p2 * t ** 2, list_koeff_b))
            elif nkn2 == p2 or p1 == p2:
                new_vts_a = list(map(lambda t: 2 * knot_1 * t * (1 - t) + pA * t ** 2, list_koeff_a))
                new_vts_b = []
            else:
                new_vts_a = list(map(lambda t: 2 * knot_1 * t * (1 - t) + pA * t ** 2, list_koeff_a))
                new_vts_b = list(
                    map(lambda t: pB * (1 - t) ** 2 + 2 * knot_2 * t * (1 - t) + p2 * t ** 2, list_koeff_b))

            if mode[3]:
                for c in range(steps_smoose):
                    new_vts_ = new_vts_a
                    V = [vi for vi in new_vts_]
                    P = list(map(lambda x, y: abs(y - x), V[:-1], V[1:]))
                    L = sum(P)
                    lp = len(P)
                    if lp > 0:
                        d = L / lp
                        l_ = list(map(lambda y: d * y / L, list(range(1, lp + 1))))
                        l = list(map(lambda x: x / L, P))

                        tmp = 1e-8
                        for i in range(lp):
                            tmp += l[i]
                            m = l_[i] / tmp
                            list_koeff_a[i] = m * list_koeff_a[i]
                        if nkn1 == 0 or p1 == 0:
                            new_vts_a = []
                            new_vts_b = list(
                                map(lambda t: pB * (1 - t) ** 2 + 2 * knot_2 * t * (1 - t) + p2 * t ** 2, list_koeff_b))
                        elif nkn2 == p2 or p1 == p2:
                            new_vts_a = list(map(lambda t: 2 * knot_1 * t * (1 - t) + pA * t ** 2, list_koeff_a))
                            new_vts_b = []
                        else:
                            new_vts_a = list(map(lambda t: 2 * knot_1 * t * (1 - t) + pA * t ** 2, list_koeff_a))
                            new_vts_b = list(
                                map(lambda t: pB * (1 - t) ** 2 + 2 * knot_2 * t * (1 - t) + p2 * t ** 2, list_koeff_b))

                    new_vts_ = new_vts_b
                    V = [vi for vi in new_vts_]
                    P = list(map(lambda x, y: abs(y - x), V[:-1], V[1:]))
                    L = sum(P)
                    lp = len(P)
                    if lp > 0:
                        d = L / lp
                        l_ = list(map(lambda y: d * y / L, list(range(1, lp + 1))))
                        l = list(map(lambda x: x / L, P))

                        tmp = 1e-8
                        for i in range(lp):
                            tmp += l[i]
                            m = l_[i] / tmp
                            list_koeff_b[i] = m * list_koeff_b[i]
                        if nkn1 == 0 or p1 == 0:
                            new_vts_a = []
                            new_vts_b = list(
                                map(lambda t: pB * (1 - t) ** 2 + 2 * knot_2 * t * (1 - t) + p2 * t ** 2, list_koeff_b))
                        elif nkn2 == p2 or p1 == p2:
                            new_vts_a = list(map(lambda t: 2 * knot_1 * t * (1 - t) + pA * t ** 2, list_koeff_a))
                            new_vts_b = []
                        else:
                            new_vts_a = list(map(lambda t: 2 * knot_1 * t * (1 - t) + pA * t ** 2, list_koeff_a))
                            new_vts_b = list(
                                map(lambda t: pB * (1 - t) ** 2 + 2 * knot_2 * t * (1 - t) + p2 * t ** 2, list_koeff_b))

            if new_vts_a:
                for idx in range(pa_sort):
                    me.vertices[sort_list[idx]].co.y += (new_vts_a[idx] + p0 - me.vertices[
                        sort_list[idx]].co.y) * influe
            if new_vts_b:
                for idx in range(cou_vs - pa_sort):
                    me.vertices[sort_list[idx + pa_sort + 1]].co.y += (new_vts_b[idx] + p0 - \
                                                                       me.vertices[
                                                                           sort_list[idx + pa_sort + 1]].co.y) * influe

        if mode[2]:
            p0 = p0_.z
            p1 = p1_.z - p0
            p2 = p2_.z - p0
            knot_1 = kn1_.z - p0
            knot_2 = kn2_.z - p0
            pA = nkn1_.z - p0
            pB = nkn2_.z - p0
            nkn1 = nkn1_.z - p0
            nkn2 = nkn2_.z - p0

            if nkn1 == 0 or p1 == 0:
                new_vts_a = []
                new_vts_b = list(
                    map(lambda t: pB * (1 - t) ** 2 + 2 * knot_2 * t * (1 - t) + p2 * t ** 2, list_koeff_b))
            elif nkn2 == p2 or p1 == p2:
                new_vts_a = list(map(lambda t: 2 * knot_1 * t * (1 - t) + pA * t ** 2, list_koeff_a))
                new_vts_b = []
            else:
                new_vts_a = list(map(lambda t: 2 * knot_1 * t * (1 - t) + pA * t ** 2, list_koeff_a))
                new_vts_b = list(
                    map(lambda t: pB * (1 - t) ** 2 + 2 * knot_2 * t * (1 - t) + p2 * t ** 2, list_koeff_b))

            if mode[3]:
                for c in range(steps_smoose):
                    new_vts_ = new_vts_a
                    V = [vi for vi in new_vts_]
                    P = list(map(lambda x, y: abs(y - x), V[:-1], V[1:]))
                    L = sum(P)
                    lp = len(P)
                    if lp > 0:
                        d = L / lp
                        l_ = list(map(lambda y: d * y / L, list(range(1, lp + 1))))
                        l = list(map(lambda x: x / L, P))

                        tmp = 1e-8
                        for i in range(lp):
                            tmp += l[i]
                            m = l_[i] / tmp
                            list_koeff_a[i] = m * list_koeff_a[i]
                        if nkn1 == 0 or p1 == 0:
                            new_vts_a = []
                            new_vts_b = list(
                                map(lambda t: pB * (1 - t) ** 2 + 2 * knot_2 * t * (1 - t) + p2 * t ** 2, list_koeff_b))
                        elif nkn2 == p2 or p1 == p2:
                            new_vts_a = list(map(lambda t: 2 * knot_1 * t * (1 - t) + pA * t ** 2, list_koeff_a))
                            new_vts_b = []
                        else:
                            new_vts_a = list(map(lambda t: 2 * knot_1 * t * (1 - t) + pA * t ** 2, list_koeff_a))
                            new_vts_b = list(
                                map(lambda t: pB * (1 - t) ** 2 + 2 * knot_2 * t * (1 - t) + p2 * t ** 2, list_koeff_b))

                    new_vts_ = new_vts_b
                    V = [vi for vi in new_vts_]
                    P = list(map(lambda x, y: abs(y - x), V[:-1], V[1:]))
                    L = sum(P)
                    lp = len(P)
                    if lp > 0:
                        d = L / lp
                        l_ = list(map(lambda y: d * y / L, list(range(1, lp + 1))))
                        l = list(map(lambda x: x / L, P))

                        tmp = 1e-8
                        for i in range(lp):
                            tmp += l[i]
                            m = l_[i] / tmp
                            list_koeff_b[i] = m * list_koeff_b[i]
                        if nkn1 == 0 or p1 == 0:
                            new_vts_a = []
                            new_vts_b = list(
                                map(lambda t: pB * (1 - t) ** 2 + 2 * knot_2 * t * (1 - t) + p2 * t ** 2, list_koeff_b))
                        elif nkn2 == p2 or p1 == p2:
                            new_vts_a = list(map(lambda t: 2 * knot_1 * t * (1 - t) + pA * t ** 2, list_koeff_a))
                            new_vts_b = []
                        else:
                            new_vts_a = list(map(lambda t: 2 * knot_1 * t * (1 - t) + pA * t ** 2, list_koeff_a))
                            new_vts_b = list(
                                map(lambda t: pB * (1 - t) ** 2 + 2 * knot_2 * t * (1 - t) + p2 * t ** 2, list_koeff_b))

            if new_vts_a:
                for idx in range(pa_sort):
                    me.vertices[sort_list[idx]].co.z += (new_vts_a[idx] + p0 - me.vertices[
                        sort_list[idx]].co.z) * influe
            if new_vts_b:
                for idx in range(cou_vs - pa_sort):
                    me.vertices[sort_list[idx + pa_sort + 1]].co.z += (new_vts_b[idx] + p0 - \
                                                                       me.vertices[
                                                                           sort_list[idx + pa_sort + 1]].co.z) * influe

        me.update()
        bm.free()

        bpy.ops.object.mode_set(mode='EDIT')

    return True


def getMats(context):
    global list_z, mats_idx, list_f, maloe

    obj = bpy.context.active_object
    me = obj.data

    bpy.ops.object.mode_set(mode='OBJECT')
    bpy.ops.object.mode_set(mode='EDIT')
    bpy.ops.mesh.select_mode(type='VERT')

    list_z = [v.co.z for v in me.vertices if v.select]
    list_z = list(set(list_z))
    list_z.sort()
    tz = list_z[0]
    tmp_z = [tz]
    for lz in list(list_z)[1:]:
        if round(abs(lz - tz), 4) > maloe:
            tmp_z.append(lz)
            tz = lz
    list_z = tmp_z

    bpy.ops.mesh.select_mode(type='FACE')
    list_f = [p.index for p in me.polygons if p.select]
    black_list = []
    mats_idx = []
    for z in list_z:
        for p in list_f:
            if p not in black_list:
                for v in me.polygons[p].vertices:
                    if abs(me.vertices[v].co.z - z) < maloe:
                        mats_idx.append(me.polygons[p].material_index)
                        black_list.append(p)
                        break
    bpy.ops.mesh.select_mode(type='VERT')


def main_matExtrude(context):
    global list_z, mats_idx, list_f, maloe

    obj = bpy.context.active_object
    me = obj.data

    bpy.ops.object.mode_set(mode='OBJECT')
    vert = [v.index for v in me.vertices if v.select][0]

    def find_index_of_selected_vertex(obj):
        # TODO force 'OBJECT' mode temporarily.
        selected_verts = [i.index for i in obj.data.vertices if i.select]
        verts_selected = len(selected_verts)
        if verts_selected < 1:
            return None
        else:
            return selected_verts

    def find_connected_verts2(me, found_index, not_list):
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

    def find_all_connected_verts2(me, active_v, not_list=[], step=0):
        vlist = [active_v]
        not_list.append(active_v)
        step += 1
        list_v_1 = find_connected_verts2(me, active_v, not_list)

        for v in list_v_1:
            list_v_2 = find_all_connected_verts2(me, v, not_list, step)
            vlist += list_v_2

        return vlist

    bm = bmesh.new()
    bm.from_mesh(me)
    check_lukap(bm)

    verts = find_all_connected_verts2(me, vert, not_list=[], step=0)
    vert_ = find_extreme_select_verts(me, verts)
    vert = vert_[0]
    verts = find_all_connected_verts2(me, vert, not_list=[], step=0)

    vts = [bm.verts[vr] for vr in verts]
    face_build = []
    face_build.extend(verts)
    fl = len(bm.verts) + 1

    tz = list_z[0]
    tmp_lz = [z - tz for z in list_z]
    list_z = tmp_lz

    z_nul = vts[0].co.z
    for zidx, z in enumerate(list_z):
        vts_tmp = []
        matz = mats_idx[min(zidx, len(mats_idx) - 1)]

        for i, vs in enumerate(vts[:-1]):
            vco1 = vs.co
            vco2 = vts[i + 1].co
            vco1.z = z + z_nul
            vco2.z = z + z_nul
            if i == 0:
                v1 = bm.verts.new(vco1)
                face_build.append(len(bm.verts) - 1)
            else:
                v1 = v2
            v2 = bm.verts.new(vco2)
            face_build.append(len(bm.verts) - 1)
            f = bm.faces.new([vs, v1, v2, vts[i + 1]])
            # check_lukap(bm)
            f.material_index = matz

            if i == 0:
                vts_tmp.append(v1)
            vts_tmp.append(v2)
        vts = vts_tmp.copy()

    bpy.ops.object.mode_set(mode='OBJECT')
    bm.to_mesh(me)
    bm.free()

    bpy.ops.object.mode_set(mode='EDIT')
    bpy.ops.mesh.select_mode(type='FACE')
    bpy.ops.mesh.select_all(action='DESELECT')
    bpy.ops.object.mode_set(mode='OBJECT')
    for p in face_build:
        me.vertices[p].select = True
    bpy.ops.object.mode_set(mode='EDIT')
    bpy.ops.mesh.select_mode(type='VERT')
    bpy.ops.mesh.remove_doubles()


def compMeshesVerts(context, treshold):
    obja = context.scene.objects.active
    objs = context.selected_objects
    if len(objs) < 2 or obja.type != 'MESH':
        print_error2('must be two or more mesh-objects', '01 CompMeshesVerts')
        return False

    bpy.ops.object.mode_set(mode='OBJECT')
    obj1 = obja
    mesh1 = obj1.data

    bpy.context.scene.objects.active = obj1
    bpy.ops.object.mode_set(mode='EDIT', toggle=False)
    bpy.ops.mesh.select_all(action='DESELECT')
    bpy.ops.object.mode_set(mode='OBJECT')

    bm = bmesh.new()
    bm.from_mesh(mesh1)
    check_lukap(bm)

    size = len(bm.verts)
    kd = mathutils.kdtree.KDTree(size)

    for i, v in enumerate(bm.verts):
        kd.insert(v.co, i)

    mesh1.update()
    kd.balance()

    sel_v = 0
    sel_o = 0
    for obj2 in objs:
        if obj2 is obj1: continue
        if obj2.type != 'MESH': continue
        sel_o += 1
        mesh2 = obj2.data

        bpy.context.scene.objects.active = obj2

        bpy.ops.object.mode_set(mode='EDIT', toggle=False)
        bpy.ops.mesh.select_all(action='DESELECT')
        bpy.ops.object.mode_set(mode='OBJECT')

        bm2 = bmesh.new()
        bm2.from_mesh(mesh2)
        check_lukap(bm2)

        size2 = len(bm2.verts)
        kd2 = mathutils.kdtree.KDTree(size2)

        for i, v in enumerate(bm2.verts):
            co, index, dist = kd.find(v.co)
            if dist > treshold:
                v.select_set(True)

            kd2.insert(v.co, i)

        kd2.balance()
        for v_ in bm.verts:
            co, index, dist = kd2.find(v_.co)
            if dist > treshold:
                if not v_.select:
                    v_.select_set(True)
                    sel_v += 1

        bm2.to_mesh(mesh2)
        mesh2.update()
        bm2.free()

    bm.to_mesh(mesh1)
    mesh1.update()
    bm.free()

    bpy.context.scene.objects.active = obja
    bpy.ops.object.mode_set(mode='EDIT')
    bpy.ops.mesh.select_mode(use_expand=True, type='VERT')

    print_error('Compare meshes (VERTS): obj=' + str(sel_o) + ' verts=' + str(sel_v))
    return True


def compMeshesToMats(context):
    obja = context.scene.objects.active
    objs = context.selected_objects
    if len(objs) < 2 or obja.type != 'MESH':
        print_error2('must be two or more mesh-objects', '01 compMeshesToMats')
        return False

    bpy.ops.object.mode_set(mode='OBJECT')
    obj1 = obja
    mesh1 = obj1.data

    context.scene.objects.active = obj1

    size = len(mesh1.polygons)
    kd = mathutils.kdtree.KDTree(size)

    for i, p in enumerate(mesh1.polygons):
        kd.insert(p.center, i)
    kd.balance()

    for obj2 in objs:
        if obj2 is obj1: continue
        if obj2.type != 'MESH': continue
        mesh2 = obj2.data

        context.scene.objects.active = obj2

        for i, p in enumerate(mesh2.polygons):
            co, index, dist = kd.find(p.center)
            p.material_index = mesh1.polygons[index].material_index
        mesh2.update()

    bpy.context.scene.objects.active = obja
    return True


def cheredator(step=1):
    bpy.ops.object.mode_set(mode='OBJECT')
    bpy.ops.object.mode_set(mode='EDIT')

    obj = bpy.context.active_object
    me = obj.data

    verts = find_index_of_selected_vertex(me)
    active = None
    if verts != None:
        extreme_vs = find_extreme_select_verts(me, verts)
        if extreme_vs == []:
            bm = bmesh.new()
            bm.from_mesh(me)
            check_lukap(bm)
            active = bm_vert_active_get(bm)[0]
            extreme_vs = [active, active]
            bm.free()
        elif len(extreme_vs) != 2:
            print_error2('Single Loop only', '01 cheredator')
            return False

        sort_list = find_all_connected_verts(me, extreme_vs[0], [])
        if len(sort_list) != len(verts) and not active:
            print_error2('Incoherent loop', '02 cheredator')
            return False

        if len(sort_list) < 3:
            print_error2('Should be greater than two vertices', '03 cheredator')
            return False

        work_list = sort_list[1:-1]

        bpy.ops.mesh.select_all(action='DESELECT')
        bpy.ops.mesh.select_mode(type='VERT')
        bpy.ops.object.mode_set(mode='OBJECT')

        v_memory = [str(me.vertices[extreme_vs[0]].co)]
        v_memory.append(str(me.vertices[extreme_vs[1]].co))
        most = False
        step_tmp = 0
        for i in work_list:
            step_tmp += 1
            if step_tmp >= step:
                most = True
                step_tmp = 0
            if most:
                me.vertices[i].select = False
                v_memory.append(str(me.vertices[i].co))
                most = False
            else:
                me.vertices[i].select = True

        bpy.ops.object.mode_set(mode='EDIT')
        bpy.ops.mesh.dissolve_verts()
        bpy.ops.mesh.select_all(action='DESELECT')
        bpy.ops.object.mode_set(mode='OBJECT')

        for v in me.vertices:
            if str(v.co) in v_memory:
                v.select = True

        bpy.ops.object.mode_set(mode='EDIT')

        return True


def cheredator_fantom(self):
    step = self.steps
    bpy.ops.object.mode_set(mode='OBJECT')
    bpy.ops.object.mode_set(mode='EDIT')

    obj = bpy.context.active_object
    me = obj.data

    verts = find_index_of_selected_vertex(me)
    active = None
    if verts != None:
        extreme_vs = find_extreme_select_verts(me, verts)
        if extreme_vs == []:
            bm = bmesh.new()
            bm.from_mesh(me)
            check_lukap(bm)
            active = bm_vert_active_get(bm)[0]
            extreme_vs = [active, active]
            bm.free()
        elif len(extreme_vs) != 2:
            print_error2('Single Loop only', '01 cheredator_fantom')
            return False
        sort_list = find_all_connected_verts(me, extreme_vs[0], [])

        if len(sort_list) != len(verts) and not active:
            print_error2('Incoherent loop', '02 cheredator_fantom')
            return False

        if len(sort_list) < 3:
            print_error2('Should be greater than two vertices', '03 cheredator_fantom')
            return False

        work_list = sort_list[1:-1]
        if self.steps > len(work_list):
            self.steps = len(work_list)

        bpy.ops.mesh.select_mode(type='VERT')

        most = False
        data_verts = []
        step_tmp = 0
        for i in work_list:
            step_tmp += 1
            if step_tmp >= step:
                most = True
                step_tmp = 0
            if most:
                data_verts.append(me.vertices[i].co)
                most = False

        data_verts.insert(0, me.vertices[extreme_vs[0]].co)
        data_verts.append(me.vertices[extreme_vs[1]].co)
        drawPointLineGL(obj.matrix_world, data_verts)
    return True


def drawPointLineGL(data_matrix, data_vector):
    from bgl import glVertex3f, glPointSize, glLineStipple, \
        glLineWidth, glBegin, glEnd, GL_POINTS, GL_LINES, \
        glEnable, glDisable, GL_BLEND, glColor4f, GL_LINE_STRIP, GL_LINE_STIPPLE

    glLineWidth(1.0)
    glEnable(GL_BLEND)
    # points
    glPointSize(6.0)
    glColor4f(1.0, 0.0, 0.0, 1.0)
    glBegin(GL_POINTS)
    for vert in data_vector:
        vec_corrected = data_matrix * vert
        glVertex3f(*vec_corrected)
    glEnd()

    # lines
    glLineWidth(3.0)
    glBegin(GL_LINE_STRIP)
    glColor4f(0.0, 1.0, 0.0, 1.0)
    for i, vector in enumerate(data_vector):
        glVertex3f(*data_matrix * data_vector[i])
    glEnd()

    # restore opengl defaults
    glDisable(GL_BLEND)
    glLineWidth(1.0)
    glColor4f(0.0, 0.0, 0.0, 1.0)


def DDDLoop():
    obj = bpy.context.active_object
    if obj.type != 'MESH':
        print_error('You need to select object of MESH type', '3DL_00')
        return False

    bpy.ops.object.mode_set(mode='OBJECT')
    bpy.ops.object.mode_set(mode='EDIT')
    me = obj.data

    selected_verts = [i.index for i in me.vertices if i.select]
    if not selected_verts:
        print_error('You need to select two loops', '3DL_01')
        return False

    act_v = selected_verts[0]
    black_list = []
    loop_1 = find_all_connected_verts(me, act_v, black_list, 0)
    white_list = [i for i in selected_verts if i not in black_list]
    if not white_list:
        print_error('You need to select two loops', '3DL_02')
        return False

    loop_2 = find_all_connected_verts(me, white_list[0], [], 0)

    loop1_x = [me.vertices[idx].co.x for idx in loop_1]
    loop1_y = [me.vertices[idx].co.y for idx in loop_1]

    direct1_x = max(loop1_x) - min(loop1_x)
    direct1_y = max(loop1_y) - min(loop1_y)
    if direct1_x > direct1_y:
        loop_xz = loop_1
        loop_yz = loop_2
    else:
        loop_xz = loop_2
        loop_yz = loop_1

    tmp_x = [(me.vertices[idx].co.z, idx) for idx in loop_xz]
    tmp_y = [(me.vertices[idx].co.z, idx) for idx in loop_yz]
    tmp_x.sort()
    tmp_y.sort()
    loop_xz = [p[1] for p in tmp_x]
    loop_yz = [p[1] for p in tmp_y]

    lz_xz = [me.vertices[idx].co.z for idx in loop_xz]
    lz_yz = [me.vertices[idx].co.z for idx in loop_yz]
    lz = lz_xz + lz_yz

    lz.sort()
    points = []

    plxz = me.vertices[loop_xz[0]].co
    for lxz in loop_xz[1:]:
        co = me.vertices[lxz].co
        for z in lz:
            if z >= plxz.z and z <= co.z:
                delitel = co.z - plxz.z
                if delitel == 0: delitel = 1e-6
                x = (z - plxz.z) * (co.x - plxz.x) / delitel + plxz.x
                points.append([z, 0, x])
            elif z > co.z:
                continue
        plxz = co

    plyz = me.vertices[loop_yz[0]].co
    for lyz in loop_yz[1:]:
        co = me.vertices[lyz].co
        for z in lz:
            if z >= plyz.z and z <= co.z:
                delitel = co.z - plyz.z
                if delitel == 0: delitel = 1e-6
                y = (z - plyz.z) * (co.y - plyz.y) / delitel + plyz.y
                points.append([z, y, 0])
            elif z > co.z:
                continue
        plyz = co

    points.sort()
    plxz = me.vertices[loop_xz[0]].co
    for lxz in loop_xz[1:]:
        co = me.vertices[lxz].co
        for idx, p in enumerate(points):
            if p[0] >= plxz.z and p[0] <= co.z and p[2] == 0:
                delitel = co.z - plxz.z
                if delitel == 0: delitel = 1e-6
                x = (p[0] - plxz.z) * (co.x - plxz.x) / delitel + plxz.x
                points[idx] = (p[0], p[1], x)
            elif p[0] > co.z:
                continue
        plxz = co

    plyz = me.vertices[loop_yz[0]].co
    for lyz in loop_yz[1:]:
        co = me.vertices[lyz].co
        for idx, p in enumerate(points):
            if p[0] >= plyz.z and p[0] <= co.z and p[1] == 0:
                delitel = co.z - plyz.z
                if delitel == 0: delitel = 1e-6
                y = (p[0] - plyz.z) * (co.y - plyz.y) / delitel + plyz.y
                points[idx] = (p[0], y, p[2])
            elif p[0] > co.z:
                continue
        plyz = co

    points_ = []
    for p in points[1:]:
        points_.append(mathutils.Vector(reversed(p)))

    edges = []
    lvs = len(me.vertices)
    for idx, po in enumerate(points_[:-1]):
        edges.append([idx, idx + 1])

    bpy.ops.mesh.select_all(action='TOGGLE')
    bpy.ops.object.mode_set(mode='OBJECT')

    nam = 'slurm_' + str(obj.name)
    mesh = bpy.data.meshes.new(nam + 'Mesh')
    ob = mk_ob(mesh, nam, obj.location)

    mesh.from_pydata(points_, edges, [])
    mesh.update(calc_edges=True)
    ob.select = True

    bpy.ops.object.mode_set(mode='OBJECT')
    bpy.ops.object.join()

    bpy.ops.object.mode_set(mode='EDIT')
    maloe = bpy.context.scene.tool_settings.double_threshold
    bpy.ops.mesh.remove_doubles(threshold=maloe, use_unselected=False)


def barc_cursorToCenter():
    bpy.ops.object.mode_set(mode='OBJECT')
    bpy.ops.object.mode_set(mode='EDIT')

    obj = bpy.context.active_object
    me = obj.data

    verts = find_index_of_selected_vertex(me)
    cou_vs = len(verts) - 1
    if verts != None and cou_vs > 0:
        extreme_vs = find_extreme_select_verts(me, verts)
        if len(extreme_vs) != 2:
            print_error2('Single Loop only', '01 barc_cursorToCenter')
            return False

        sort_list = find_all_connected_verts(me, extreme_vs[0], [])
        if len(sort_list) != len(verts):
            print_error2('Incoherent loop', '02 barc_cursorToCenter')
            return False

        bpy.ops.object.mode_set(mode='OBJECT')
        bm = bmesh.new()
        bm.from_mesh(me)
        check_lukap(bm)

        pa_idx = bm_vert_active_get(bm)[0]
        if pa_idx == None:
            print_error2('Active vert is not detected', '03 barc_cursorToCenter')
            return False

        p_a_ = me.vertices[extreme_vs[0]].co
        p_b_ = me.vertices[pa_idx].co
        p_c_ = me.vertices[extreme_vs[1]].co

        normal_B = getNormalPlane([p_a_, p_b_, p_c_], mathutils.Matrix())
        normal_z = mathutils.Vector((0, 0, -1))
        mat_rot_norm = normal_B.rotation_difference(normal_z).to_matrix().to_4x4()

        p_a = mat_rot_norm * p_a_
        p_b = mat_rot_norm * p_b_
        p_c = mat_rot_norm * p_c_
        p_ab = (p_a + p_b) / 2
        p_bc = (p_b + p_c) / 2
        ab = p_b - p_a
        bc = p_c - p_b
        k_ab = -ab.y / (ab.x + 1e-7)
        k_bc = -bc.y / (bc.x + 1e-7)
        z = p_a.z
        ab_d = mathutils.Vector((k_ab, 1, 0)).normalized()
        bc_d = mathutils.Vector((k_bc, 1, 0)).normalized()
        p_d_ = mathutils.geometry.intersect_line_line(p_ab, p_ab + ab_d, p_bc, p_bc + bc_d)
        if p_d_ == None:
            print_error2('Impossible to construct the arc radius', '04 barc_cursorToCenter')
            return False

        p_d = p_d_[0]
        mat_rot_norm_inv = mat_rot_norm.inverted()
        center = mat_rot_norm_inv * p_d

        bpy.context.scene.cursor_location = obj.matrix_basis * center


def barc(rad):
    bpy.ops.object.mode_set(mode='OBJECT')
    bpy.ops.object.mode_set(mode='EDIT')

    obj = bpy.context.active_object
    me = obj.data

    verts = find_index_of_selected_vertex(me)
    cou_vs = len(verts) - 1
    if verts != None and cou_vs > 0:
        extreme_vs = find_extreme_select_verts(me, verts)
        if len(extreme_vs) != 2:
            print_error2('Single Loop only', '01 barc')
            return False

        sort_list = find_all_connected_verts(me, extreme_vs[0], [])
        if len(sort_list) != len(verts):
            print_error2('Incoherent loop', '02 barc')
            return False

        bpy.ops.object.mode_set(mode='OBJECT')
        bm = bmesh.new()
        bm.from_mesh(me)
        check_lukap(bm)

        pa_idx = bm_vert_active_get(bm)[0]
        if pa_idx == None:
            print_error2('Active vert is not detected', '03 barc')
            return False

        cursor_loc = bpy.context.scene.cursor_location * obj.matrix_world

        p_a_ = me.vertices[extreme_vs[0]].co
        p_b_ = me.vertices[pa_idx].co
        p_c_ = me.vertices[extreme_vs[1]].co
        if pa_idx in extreme_vs:
            p_b_ = cursor_loc

        new_origin = (p_a_ + p_b_ + p_c_) / 3
        p_a_ = p_a_ - new_origin
        p_b_ = p_b_ - new_origin
        p_c_ = p_c_ - new_origin

        normal_B = getNormalPlane([p_a_, p_b_, p_c_], mathutils.Matrix())
        normal_z = mathutils.Vector((0, 0, -1))
        mat_rot_norm = normal_B.rotation_difference(normal_z).to_matrix().to_4x4()

        p_a = mat_rot_norm * p_a_
        p_b = mat_rot_norm * p_b_
        p_c = mat_rot_norm * p_c_
        p_ab = (p_a + p_b) / 2
        p_bc = (p_b + p_c) / 2
        ab = p_b - p_a
        bc = p_c - p_b
        k_ab = -ab.y / (ab.x + 1e-7)
        k_bc = -bc.y / (bc.x + 1e-7)
        z = p_a.z
        ab_d = mathutils.Vector((k_ab, 1, 0)).normalized()
        bc_d = mathutils.Vector((k_bc, 1, 0)).normalized()
        p_d_ = mathutils.geometry.intersect_line_line(p_ab, p_ab + ab_d, p_bc, p_bc + bc_d)
        if p_d_ == None:
            print_error2('Impossible to construct the arc radius', '04 barc')
            return False

        p_d = p_d_[0]
        ad = p_a - p_d
        config = bpy.context.window_manager.paul_manager
        if rad != None:
            radius = rad
            ac = p_c - p_a
            p_d_ = p_a + ac / 2
            ac_div_2_len = ac.length / 2
            k_ac = -ac.y / (ac.x + 1e-7)
            ac_d = mathutils.Vector((k_ac, 1, 0)).normalized()
            if rad < ac_div_2_len:
                radius = ac_div_2_len

            l1 = (p_b - (p_d_ + ac_d)).length
            l2 = (p_b - (p_d_ - ac_d)).length
            if l2 > l1:
                ac_d = -ac_d

            tmp_ld = sqrt(radius ** 2 - ac_div_2_len ** 2)
            p_d = tmp_ld * ac_d + p_d_
            ad = p_a - p_d

        else:
            radius = ad.length

        config.barc_rad = radius
        angle = ad.angle(p_c - p_d)
        section_angle = angle / (len(sort_list) - 1)
        vector_zero = mathutils.Vector((1, 0, 0))
        angle_zero = pi / 2 + ad.angle(vector_zero)
        test_x = sin(section_angle * (len(sort_list) - 1) + angle_zero) * radius + p_d.x
        test_y = cos(section_angle * (len(sort_list) - 1) + angle_zero) * radius + p_d.y
        test_by_x = abs(test_x - p_c.x) < maloe
        test_by_y = abs(test_y - p_c.y) < maloe
        if not test_by_x or not test_by_y:
            angle_zero = pi / 2 - ad.angle(vector_zero)
            test_x = sin(angle_zero) * radius + p_d.x
            test_y = cos(angle_zero) * radius + p_d.y
            test_by_x = abs(test_x - p_a.x) < maloe
            test_by_y = abs(test_y - p_a.y) < maloe
            if not test_by_x or not test_by_y:
                angle = 2 * pi - angle
                angle_zero = pi / 2 + ad.angle(vector_zero)
                section_angle = angle / (len(sort_list) - 1)
            else:
                test_x = sin(section_angle * (len(sort_list) - 1) + angle_zero) * radius + p_d.x
                test_y = cos(section_angle * (len(sort_list) - 1) + angle_zero) * radius + p_d.y
                test_by_x = abs(test_x - p_c.x) < maloe
                test_by_y = abs(test_y - p_c.y) < maloe
                if not test_by_x or not test_by_y:
                    angle = 2 * pi - angle
                    angle_zero = pi / 2 - ad.angle(vector_zero)
                    section_angle = angle / (len(sort_list) - 1)

        mat_rot_norm_inv = mat_rot_norm.inverted()
        for i, v_idx in enumerate(sort_list):
            x = sin(section_angle * i + angle_zero) * radius + p_d.x
            y = cos(section_angle * i + angle_zero) * radius + p_d.y
            me.vertices[v_idx].co = mat_rot_norm_inv * Vector((x, y, z)) + new_origin


def ignore_instance():
    names = {}
    for obj in bpy.data.objects:
        if not obj.select \
                or obj.type != 'MESH' and obj.type != 'CURVE': continue

        dataname = obj.type + obj.data.name

        if dataname in names:
            obj.select = False
            bpy.data.objects[names[dataname]].select = False
        else:
            names[dataname] = obj.name


def select_modifiers_objs():
    for obj in bpy.data.objects:
        if obj.type != 'MESH' and obj.type != 'CURVE': continue
        obj.select = len(obj.modifiers) > 0


def switch_matnodes():
    flag = False
    mode = False
    for mat in bpy.data.materials:
        if not flag:
            mode = not mat.use_nodes
            flag = True
        mat.use_nodes = mode


def all_mats_to_active():
    obj = bpy.context.scene.objects.active
    if obj:
        mats = []
        for mat in obj.material_slots:
            mats.append(mat.name)
        for m in bpy.data.materials:
            if m.name not in mats:
                bpy.ops.object.material_slot_add()
                obj.material_slots[-1].material = bpy.data.materials[m.name]


def selected_mats_to_active():
    obj = bpy.context.scene.objects.active
    if obj:
        mats = []
        for mat in obj.material_slots:
            mats.append(mat.name)
        for obj2 in bpy.data.objects:
            if not obj2.select or obj2 is obj: continue
            if obj.type == 'MESH':
                for mat2 in obj2.material_slots:
                    mat_name = mat2.name
                    if mat_name and mat_name not in mats:
                        mats.append(mat_name)
                        bpy.ops.object.material_slot_add()
                        obj.material_slots[-1].material = bpy.data.materials[mat_name]


def select_2d_curves():
    for obj in bpy.data.objects:
        if not obj.select: continue
        if obj.type != 'CURVE':
            obj.select = False
        elif obj.data.dimensions != '2D':
            obj.select = False


def filter_dubles_origins(mode_verts=False):
    maloe = bpy.context.tool_settings.double_threshold
    locs = []
    lnumb_vts = []
    objs = bpy.context.selected_objects
    for obj in objs:  # bpy.context.scene.objects:
        if obj.type == 'CURVE' or obj.type == 'MESH':
            loc = obj.location
            if obj.type == 'CURVE':
                numb_vts = ('CURVE', obj.data.resolution_u)
            else:
                numb_vts = ('MESH', len(obj.data.vertices))

            flag = False
            for i, l in enumerate(locs):
                nvts = lnumb_vts[i]
                ll = (l - loc).length
                if ll < maloe:
                    if mode_verts and nvts != numb_vts: continue
                    flag = True
                    break

            obj.select = flag
            if not flag:
                locs.append(loc)
                lnumb_vts.append(numb_vts)


def swap_curve():
    i = None
    dim = {'2D': '3D', '3D': '2D'}
    for obj in bpy.context.selected_objects:
        if obj.type == 'CURVE':
            if i == None:
                i = dim[obj.data.dimensions]
            obj.data.dimensions = i


def hue_2matneme():
    for matik in bpy.data.materials:
        H_ = min(round(matik.diffuse_color.h, 2), 0.99)
        V_ = min(round(matik.diffuse_color.v, 2), 0.99)
        S_ = min(round(matik.diffuse_color.s, 2), 0.99)

        H = ("%.2f" % (H_))[-2:]
        V = ("%.2f" % (V_))[-2:]
        S = ("%.2f" % (S_))[-2:]

        name_ = matik.name.split('---')[-1]
        mat_name = H + V + S + '---' + name_
        matik.name = mat_name


def HVS_from_mathame():
    for matik in bpy.data.materials:
        mat_name = matik.name.split('---')[-1]
        matik.name = mat_name


def supress_materials():
    all_mats = {}
    del_mats = []
    for matik in bpy.data.materials:
        name = matik.name
        diffcolor = str(matik.diffuse_color.r) + str(matik.diffuse_color.g) + \
                    str(matik.diffuse_color.b)
        if diffcolor in all_mats:
            del_mats.append(name)
        else:
            all_mats[diffcolor] = name

    for obj in bpy.data.objects:
        for m in obj.material_slots:
            mat = m.material
            if mat == None: continue
            diffcolor_ = str(mat.diffuse_color.r) + str(mat.diffuse_color.g) + \
                         str(mat.diffuse_color.b)
            m.material = bpy.data.materials[all_mats[diffcolor_]]

    for del_m in del_mats:
        dm = bpy.data.materials[del_m]
        bpy.data.materials.remove(dm)


def matsUnclone():
    """replace numeral duplicated materials in scene"""
    mats = bpy.data.materials
    objs = bpy.context.scene.objects
    number_basis = {}
    for obj in objs:
        len_mats_m1 = len(obj.material_slots) - 1
        for i, slt in enumerate(obj.material_slots):
            part = slt.name.rpartition('.')
            if part[2].isnumeric():
                if part[0] in mats:
                    slt.material = mats.get(part[0])
                    number_basis[part[0]] = part[0]
                else:
                    if part[0] not in number_basis:
                        tmp_matname = slt.name
                        if i < len_mats_m1:
                            for slt_ in obj.material_slots[i + 1:]:
                                part_ = slt_.name.rpartition('.')
                                if part_[0] == part[0] and \
                                        part_[2].isnumeric() and \
                                        part_[2] < part[2]:
                                    tmp_matname = slt_.name

                        mats.get(tmp_matname).name = part[0]
                        number_basis[part[0]] = part[0]
                        slt.material = mats.get(part[0])
                    else:
                        slt.material = mats.get(number_basis[part[0]])


def matsPurgeout():
    """delete unused material slots from selected objects"""
    bpy.ops.object.mode_set(mode='OBJECT', toggle=False)
    for ob in bpy.context.selected_objects:
        bpy.context.scene.objects.active = ob
        if ob.type != 'MESH':
            continue
        mat_slots = {}
        for p in ob.data.polygons:
            mat_slots[p.material_index] = 1
        mat_slots = mat_slots.keys()
        for i in range(len(ob.material_slots) - 1, -1, -1):
            if i not in mat_slots:
                bpy.context.object.active_material_index = i
                bpy.ops.object.material_slot_remove()


def matsDatafix():
    """turn materials slots to data and remove cloned slots for selection"""
    ###############################
    """Материалы в данные"""
    # author: Nikita Gorodetskiy
    obj = bpy.context.selected_objects
    mode = 'DATA'
    for o in obj:
        mats_inst = [m.material for m in o.material_slots]
        materials = bpy.data.objects[o.name].material_slots
        for i, m in enumerate(materials):
            m.link = mode
            # print('материал "'+str(m.name)+'", объект "'+o.name+'", режим материала: '+mode)
            bpy.data.objects[o.name].material_slots[i].material = mats_inst[i]
    ###############################################

    """clear slot duples"""
    obj = bpy.context.selected_objects
    for o in obj:
        bpy.context.scene.objects.active = o
        mats_inst = [m.material for m in o.material_slots]
        slots = bpy.data.objects[o.name].material_slots
        mat_info = namedtuple('mat_info', 'mat slot index')
        clear_mats = [mat_info(None, None, None)]
        remove_slots = []
        for i, slot in enumerate(slots):
            mat = slot.material
            cell = mat_info(mat, slot, i)
            mats_ = [m.mat for m in clear_mats]
            if mat not in mats_:
                clear_mats.append(cell)
            else:
                idx = mats_.index(mat)
                bpy.ops.object.editmode_toggle()
                bpy.ops.mesh.select_all(action='DESELECT')
                bpy.context.object.active_material_index = i
                bpy.ops.object.material_slot_select()
                bpy.context.object.active_material_index = idx - 1
                bpy.ops.object.material_slot_select()
                bpy.ops.object.material_slot_assign()
                bpy.ops.object.editmode_toggle()
                remove_slots.append(cell)

        for slot in remove_slots[::-1]:
            bpy.context.object.active_material_index = slot.index
            bpy.ops.object.material_slot_remove()


def matsActSortSlots():
    obj_act = bpy.context.scene.objects.active

    mat_info = namedtuple('mat_info', 'mat slot index')
    need_mats = {}

    slots = obj_act.material_slots
    for i, slot in enumerate(slots):
        mat = slot.material
        cell = mat_info(mat, slot, i)
        need_mats[slot.name] = cell

    slots = [s.name for s in bpy.data.objects[obj_act.name].material_slots]
    sort_mats = sorted(slots)

    len_need_mats = len(sort_mats)
    for j in range(len_need_mats):
        cell = need_mats[sort_mats[j]]
        slot_name = cell.mat.name
        slots = [s.name for s in bpy.data.objects[obj_act.name].material_slots]

        for i, slot_ in enumerate(slots):
            if slot_ == slot_name:
                print(slot_, cell.index)
                idx_move = j - i
                bpy.context.object.active_material_index = i
                if idx_move > 0:
                    for j in range(idx_move):
                        bpy.ops.object.material_slot_move(direction="DOWN")
                elif idx_move < 0:
                    for j in range(-idx_move):
                        bpy.ops.object.material_slot_move(direction="UP")


def getMatsAct2Pas():
    objs = bpy.context.selected_objects
    obj_act = bpy.context.scene.objects.active

    mat_info = namedtuple('mat_info', 'mat slot index')
    need_mats = []

    # 1) Берём полный список материалов активного объекта
    i_base = 0
    slots = obj_act.material_slots
    for i, slot in enumerate(slots):
        mat = slot.material
        cell = mat_info(mat, slot, i_base)
        need_mats.append(cell)
        i_base += 1

    # 2) Дополняем его нехватающими материалами пассивных объектов
    for o in objs:
        if o == obj_act:
            continue

        slots = bpy.data.objects[o.name].material_slots
        for i, slot in enumerate(slots):
            mat = slot.material
            mats_ = [m.mat for m in need_mats]
            if mat not in mats_:
                bpy.ops.object.material_slot_add()
                new_slot = bpy.data.objects[obj_act.name].material_slots[-1]
                new_slot.material = bpy.data.materials[mat.name]
                cell = mat_info(mat, new_slot, i_base)
                need_mats.append(cell)
                i_base += 1

    # 3) Назначаем этот список всем выделенным объектам таким образом,
    #    чтобы внешне они выглядели так же

    slots = bpy.data.objects[obj_act.name].material_slots
    for o in objs:
        if o == obj_act:
            continue

        bpy.context.scene.objects.active = o
        mats_ = [s.material.name for s in bpy.data.objects[o.name].material_slots]
        for i, slot in enumerate(slots):
            mat = slot.material.name
            if mat not in mats_:
                bpy.ops.object.material_slot_add()
                new_slot = bpy.data.objects[o.name].material_slots[-1]
                new_slot.material = bpy.data.materials[mat]

    for o in objs:
        bpy.context.scene.objects.active = o
        len_need_mats = len(need_mats)
        for j in range(len_need_mats):
            cell = need_mats[j]
            slot_name = cell.mat.name
            slots = [s.name for s in bpy.data.objects[o.name].material_slots]
            for i, slot_ in enumerate(slots):
                if slot_ == slot_name:
                    idx_move = cell.index - i
                    bpy.context.object.active_material_index = i
                    if idx_move > 0:
                        for j in range(idx_move):
                            bpy.ops.object.material_slot_move(direction="DOWN")
                    elif idx_move < 0:
                        for j in range(-idx_move):
                            bpy.ops.object.material_slot_move(direction="UP")

    bpy.context.scene.objects.active = obj_act


def matchProp():
    cont = bpy.context
    obj = cont.active_object
    pps_ = dir(obj)
    pps = [p for p in pps_ if p.find('show_') == 0]
    wpps = {}
    typ = obj.type
    for p in pps:
        if hasattr(obj, p):
            wpps[p] = getattr(obj, p)

    for o in cont.selected_objects:
        if obj is o: continue
        if o.type != typ: continue

        for p in wpps:
            if hasattr(o, p):
                setattr(o, p, wpps[p])


def filter_chunks_main():
    obj = bpy.context.active_object
    me = obj.data
    me.update()

    bm = bmesh.new()
    bm.from_mesh(me)
    check_lukap(bm)

    # Получаем список выделенных вершин
    verts = [v for v in bm.verts if v.select]

    # Каждую вершину проверяем на смежные рёбра
    for v in verts:
        edges_ = v.link_edges

        if not edges_:
            v.select = False

        # Проверка рёбер на то, что выделено ли оно
        for e in edges_:
            if not e.select:
                v.select = False
                faces_ = v.link_faces
                for f in faces_:
                    f.select = False
                break

    edit_mode_out()
    bm.to_mesh(me)
    bm.free()
    edit_mode_in()


def Select_chunks(maloe, setting):
    maloe = maloe / 1e+6
    obj = bpy.context.active_object
    if obj.type != 'MESH': return
    if obj.mode != 'EDIT': return

    bpy.ops.object.mode_set(mode='OBJECT')
    bpy.ops.object.mode_set(mode='EDIT')
    mesh = obj.data

    chunk_obj = list(obj.get('chunk_key', []))
    chunk_obj_curr = [len(mesh.vertices), len(mesh.edges), len(mesh.polygons)]

    if setting != 'SF':
        mesh.update()
        mem_v_start = [v.index for v in mesh.vertices if v.select == True]
        mem_f_start = [f.index for f in mesh.polygons if f.select == True]
        # if chunk_obj_curr != chunk_obj:
        if setting == 'V':
            bpy.ops.mesh.select_mode(type='VERT')
            set_chunks_v = []
            bpy.ops.mesh.select_all(action='DESELECT')
            vl = len(mesh.vertices)
            black_list = []
            for v_ in range(vl):
                if v_ in black_list: continue
                v = mesh.vertices[v_]
                bpy.ops.object.mode_set(mode='OBJECT')
                mesh.vertices[v_].select = True
                bpy.ops.object.mode_set(mode='EDIT')
                bpy.ops.mesh.select_linked()
                bpy.ops.object.editmode_toggle()
                bpy.ops.object.editmode_toggle()
                bl = [v1.index for v1 in mesh.vertices if v1.select == True]
                set_chunks_v.append(bl)
                black_list.extend(bl)

                bpy.ops.mesh.select_all(action='DESELECT')

            bpy.ops.object.mode_set(mode='OBJECT')
            for i in mem_v_start:
                mesh.vertices[i].select = True

        if setting == 'F':
            black_list = []
            set_chunks_f = []
            fl = len(mesh.polygons)
            for f_ in range(fl):
                if f_ in black_list: continue
                f = mesh.polygons[f_]
                bpy.ops.object.mode_set(mode='OBJECT')
                mesh.polygons[f_].select = True
                bpy.ops.object.mode_set(mode='EDIT')
                bpy.ops.mesh.select_linked()
                bpy.ops.object.editmode_toggle()
                bpy.ops.object.editmode_toggle()
                bl = [f1.index for f1 in mesh.polygons if f1.select == True]
                black_list.extend(bl)
                set_chunks_f.append(bl)

                bpy.ops.mesh.select_all(action='DESELECT')

            for i in mem_f_start:
                mesh.polygons[i].select = True

            bpy.ops.object.mode_set(mode='EDIT')
            # obj['set_chunks_v'] = set_chunks_v
            # obj['set_chunks_f'] = set_chunks_f
            # obj['chunk_key'] = chunk_obj_curr

    if setting == 'V':
        if not mem_v_start: return

        count_v = len(mem_v_start)
        white_list_v = mem_v_start.copy()
        # set_chunks_v = list(obj['set_chunks_v'])
        for chunk in set_chunks_v:
            if count_v == len(chunk) and mem_v_start[0] not in chunk:
                white_list_v.extend(chunk)

        bpy.ops.object.mode_set(mode='OBJECT')
        for i in white_list_v:
            mesh.vertices[i].select = True

        bpy.ops.object.mode_set(mode='EDIT')
        bpy.ops.mesh.select_mode(type='VERT')

    if setting == 'F':
        if not mem_f_start: return

        count_f = len(mem_f_start)
        white_list_f = mem_f_start.copy()
        # set_chunks_f = list(obj['set_chunks_f'])
        for chunk in set_chunks_f:
            if count_f == len(chunk) and mem_f_start[0] not in chunk:
                white_list_f.extend(chunk)

        bpy.ops.object.mode_set(mode='OBJECT')
        for i in white_list_f:
            mesh.polygons[i].select = True

        bpy.ops.object.mode_set(mode='EDIT')
        bpy.ops.mesh.select_mode(type='FACE')

    if setting == 'SF':
        bm = bmesh.new()
        bm.from_mesh(mesh)
        check_lukap(bm)

        lifaces = [f.index for f in bm.faces if f.select == True]
        lifs = []

        for finst in lifaces:
            face_inst = bm.faces[finst]
            area = face_inst.calc_area()
            perim = face_inst.calc_perimeter()
            if area <= maloe or perim <= maloe:
                continue

            k = area / perim

            for face in bm.faces:
                if face.index in lifaces: continue
                area2 = face.calc_area()
                perim2 = face.calc_perimeter()
                sigma = sqrt(area2 / area)
                k2 = area2 / perim2
                k_ = k2 / sigma

                if abs(k_ - k) < maloe:
                    lifs.append(face.index)

        bpy.ops.object.mode_set(mode='OBJECT')
        for i in lifs:
            mesh.polygons[i].select = True

        bm.free()
        bpy.ops.object.mode_set(mode='EDIT')
        bpy.ops.mesh.select_mode(type='FACE')

    if setting == "FC":
        edit_mode_out()
        edit_mode_in()
        time_start = time.time()
        cou = bpy.context.active_object.data.total_vert_sel
        cou_old = 0
        cycle = 200
        while (cou != cou_old and cycle > 0):
            filter_chunks_main()
            cycle -= 1
            cou_old = cou
            cou = bpy.context.active_object.data.total_vert_sel

        print("Filter Chunks Script Finished: %.4f sec" % (time.time() - time_start))
        print("Filter Chunks cycles: ", 200 - cycle)


def intersection(start1, end1, start2, end2, out_intersection):
    dir1 = end1 - start1
    dir2 = end2 - start2

    # считаем уравнения прямых проходящих через отрезки
    a1 = -dir1.y
    b1 = +dir1.x
    d1 = -(a1 * start1.x + b1 * start1.y)

    a2 = -dir2.y
    b2 = +dir2.x
    d2 = -(a2 * start2.x + b2 * start2.y)

    # подставляем концы отрезков, для выяснения в каких полуплоскотях они
    seg1_line2_start = a2 * start1.x + b2 * start1.y + d2
    seg1_line2_end = a2 * end1.x + b2 * end1.y + d2

    seg2_line1_start = a1 * start2.x + b1 * start2.y + d1
    seg2_line1_end = a1 * end2.x + b1 * end2.y + d1

    u = seg1_line2_start / (seg1_line2_start - seg1_line2_end)
    out_intersection = start1 + u * dir1

    return out_intersection


def get_active_edge(bm):
    result = None
    elem, el = bm_vert_active_get(bm)
    if elem != None:
        mode_ = str(el)[3:4]
        bpy.ops.object.mode_set(mode='EDIT')
        bpy.ops.mesh.select_mode(type='EDGE')
        bm.edges[elem].verts[1]
        elem, el = bm_vert_active_get(bm)
        if elem != None:
            result = [bm.edges[elem].verts[0].index, bm.edges[elem].verts[1].index]

        if mode_ == 'V':
            bpy.ops.mesh.select_mode(type='VERT')
        elif mode_ == 'E':
            bpy.ops.mesh.select_mode(type='EDGE')
        elif mode_ == 'F':
            bpy.ops.mesh.select_mode(type='FACE')
        bpy.ops.object.mode_set(mode='OBJECT')
    return result


def corner_corner(active, to_active):
    obj = bpy.context.active_object
    me = obj.data

    bm = bmesh.new()
    bm.from_mesh(me)
    check_lukap(bm)

    loop1 = get_active_edge(bm)
    if not loop1:
        print_error2('It should be active loop', '01 corner_corner')
        bm.free()
        return False

    sel_edges = [e for e in bm.edges if e.select and e.verts[0].index not in loop1]
    loops = [[e.verts[0].index, e.verts[1].index] for e in sel_edges]
    if len(loops) == 0:
        print_error2('It should be many loops', '02 corner_corner')
        bm.free()
        return False

    for loop2 in loops:
        verts = me.vertices
        v1 = verts[loop1[0]].co
        v2 = verts[loop1[1]].co
        v3 = verts[loop2[0]].co
        v4 = verts[loop2[1]].co

        out_intersection = Vector()
        p_cross = intersection(v1, v2, v3, v4, out_intersection)
        if not p_cross:
            print_error2('lines do not intersect!', '03 corner_corner')
            bm.free()
            return False

        l1 = (p_cross - v1).length
        l2 = (p_cross - v2).length
        i1 = 0
        i1_ = 1
        if l2 < l1:
            i1 = 1
            i1_ = 0

        l1 = (p_cross - v3).length
        l2 = (p_cross - v4).length
        i2 = 0
        i2_ = 1
        if l2 < l1:
            i2 = 1
            i2_ = 0

        v2 = me.vertices[loop1[i1]].co
        v1 = me.vertices[loop1[i1_]].co
        vec1 = v2 - v1
        ll = sqrt(abs((p_cross.x - v1[0]) ** 2 + (p_cross.y - v1[1]) ** 2))
        kl = ll / sqrt(abs((v2.x - v1[0]) ** 2 + (v2.y - v1[1]) ** 2))
        zz1 = v1 + vec1 * kl

        v4 = me.vertices[loop2[i2]].co
        v3 = me.vertices[loop2[i2_]].co
        vec2 = v4 - v3
        ll = sqrt(abs((p_cross.x - v3[0]) ** 2 + (p_cross.y - v3[1]) ** 2))
        kl = ll / sqrt(abs((v4.x - v3[0]) ** 2 + (v4.y - v3[1]) ** 2))
        zz2 = v3 + vec2 * kl

        if (active or to_active) and loop1:
            if me.vertices[loop1[i1]].index in loop1:
                if active:
                    me.vertices[loop1[i1]].co = zz1
                else:
                    me.vertices[loop2[i2]].co = zz2
            else:
                if active:
                    me.vertices[loop2[i2]].co = zz2
                else:
                    me.vertices[loop1[i1]].co = zz1
        else:
            me.vertices[loop1[i1]].co = zz1
            me.vertices[loop2[i2]].co = zz2

    bm.free()
    return True


def corner_extend(active, to_active):
    obj = bpy.context.active_object
    me = obj.data

    bm = bmesh.new()
    bm.from_mesh(me)
    check_lukap(bm)

    loop1 = get_active_edge(bm)
    if not loop1:
        print_error2('It should be active loop', '01 corner_extend')
        bm.free()
        return False

    sel_edges = [e for e in bm.edges if e.select and e.verts[0].index not in loop1]
    loops = [[e.verts[0].index, e.verts[1].index] for e in sel_edges]
    if len(loops) == 0:
        print_error2('It should be many loops', '02 corner_extend')
        bm.free()
        return False

    for loop2 in loops:
        verts = me.vertices
        v1 = verts[loop1[0]].co
        v2 = verts[loop1[1]].co
        v3 = verts[loop2[0]].co
        v4 = verts[loop2[1]].co
        p_cross = intersect_line_line(v1, v2, v3, v4)

        l1 = (p_cross[0] - v1).length
        l2 = (p_cross[0] - v2).length
        i1 = 0
        if l2 < l1: i1 = 1

        l1 = (p_cross[1] - v3).length
        l2 = (p_cross[1] - v4).length
        i2 = 0
        if l2 < l1: i2 = 1

        if (active or to_active) and loop1:
            if me.vertices[loop1[i1]].index in loop1:
                if active:
                    me.vertices[loop1[i1]].co = p_cross[0]
                else:
                    me.vertices[loop2[i2]].co = p_cross[1]
            else:
                if active:
                    me.vertices[loop2[i2]].co = p_cross[1]
                else:
                    me.vertices[loop1[i1]].co = p_cross[0]
        else:
            me.vertices[loop1[i1]].co = p_cross[0]
            me.vertices[loop2[i2]].co = p_cross[1]

    bm.free()
    return True


def objSwitchOn(vizing, select, render, off=False):
    scene = bpy.context.scene
    lays = [l for l in scene.layers]
    objects = [o for o in scene.objects \
               if lays[list(o.layers).index(True)]]

    vizing_, select_, render_ = (True, True, True) if off else (False, False, False)

    for obj in objects:
        if not vizing: obj.hide = vizing_
        if not select: obj.hide_select = select_
        if not render: obj.hide_render = render_

    return True


################# UV Scaler #############
# Get object and UV map given their names
def GetObjectAndUVMap(objName, uvMapName):
    try:
        obj = bpy.data.objects[objName]

        if obj.type == 'MESH':
            uvMap = obj.data.uv_layers[uvMapName]
            return obj, uvMap
    except:
        pass

    return None, None


# Scale a 2D vector v, considering a scale s and a pivot point p
def Scale2D(v, s, p):
    return (p[0] + s[0] * (v[0] - p[0]), p[1] + s[1] * (v[1] - p[1]))


# Scale a UV map iterating over its coordinates to a given scale and with a pivot point
def ScaleUV(uvMap, scale, pivot):
    for uvIndex in range(len(uvMap.data)):
        uvMap.data[uvIndex].uv = Scale2D(uvMap.data[uvIndex].uv, scale, pivot)


def instancesSelectUnique():
    objs = bpy.context.selected_objects

    isolate = {}
    for obj in objs:
        if obj.type != "MESH":
            continue

        o_name = obj.name
        m_name = obj.data.name
        if m_name not in isolate:
            isolate[m_name] = o_name

    bpy.ops.object.select_all(action="DESELECT")
    for key, isolated in isolate.items():
        bpy.data.objects[isolated].select = True


def mainUvScaler(SIZE):
    # UV data are not accessible in edit mode
    bpy.ops.object.mode_set(mode="OBJECT")
    instancesSelectUnique()
    objs = [o for o in bpy.context.scene.objects if o.select]
    uvMap = bpy.context.active_object.data.uv_layers.active
    if uvMap is None:
        return

    uvMapName = uvMap.name
    for obj in objs:
        # The names of the object and map
        bpy.context.scene.objects.active = obj
        objName = obj.name

        # Defines the pivot and scale
        pivot = Vector((0, 0))
        scale = Vector((SIZE, SIZE))

        # Get the object from names
        obj, uvMap = GetObjectAndUVMap(objName, uvMapName)

        # If the object is found, scale its UV map
        if obj is not None:
            ScaleUV(uvMap, scale, pivot)


class UvScalerOperator(bpy.types.Operator):
    """UV Operator scaler"""
    bl_idname = "uv.scaler"
    bl_label = "Scaler UV Operator"
    bl_options = {'REGISTER', 'UNDO'}

    size = FloatProperty(name="Size", default=0.5)

    def draw(self, context):
        layout = self.layout
        obj = context.object
        row = layout.row()
        row.label(text="UV Scaler", icon='GROUP_UVS')
        row = layout.row()
        row.prop(self, 'size')

    def execute(self, context):
        mainUvScaler(self.size)
        return {'FINISHED'}


######### UV Scaler END #################


def read_camera_setup_obj(self, obj):
    if obj.type != 'CAMERA': return False
    name = obj.data.name
    li = name.rfind('(') + 1
    ri = name.rfind(')')
    if li > -1 and ri > -1:
        mem = name[li:ri]
        resol = mem.split('+')
        if len(resol) == 2:
            if resol[1].isdigit() and resol[0].isdigit():
                w, h = list(map(int, resol))
                bpy.context.scene.render.resolution_x = w
                bpy.context.scene.render.resolution_y = h
            else:
                print_error3('not readable digits resolution', 'rcs_01', self)
                return False
        else:
            print_error3('resolution is not readable', 'rcs_02', self)
            return False
    else:
        print_error3('camera res not found', 'rcs_03', self)
        return False

    self.report({'INFO'}, "[%s]" % mem)
    return True


class PaRCS(bpy.types.Operator):
    '''Read objname of active camera and set the resolution of render'''
    bl_idname = "paul.read_camera_setup"
    bl_label = "RCS Read Camera Setup"

    @classmethod
    def poll(cls, context):
        return context.active_object is not None and context.active_object.type == 'CAMERA'

    def execute(self, context):
        o = context.active_object
        result = read_camera_setup_obj(self, o)
        if result:
            return {'FINISHED'}
        else:
            return {'CANCELLED'}


############## PlyCams Render #################
class ExportSomeData(Operator, ExportHelper):
    """This appears in the tooltip of the operator and in the generated docs"""
    bl_idname = "export_test.some_data"  # important since its how bpy.ops.import_test.some_data is constructed
    bl_label = "Export Some Data"

    # ExportHelper mixin class uses this
    filename_ext = ""

    def execute(self, context):
        return render_me(self.filepath)


def render_me(filepath):
    config = bpy.context.window_manager.paul_manager
    sceneName = bpy.context.scene.name
    glob_res = [bpy.context.scene.render.resolution_x, bpy.context.scene.render.resolution_y]

    bpy.data.scenes[sceneName].render.filepath = filepath
    if not os.path.exists(filepath):
        os.mkdir(filepath)
    outputfile_s = os.path.join(filepath, 'stat.txt')

    if os.path.isfile(outputfile_s):
        os.remove(outputfile_s)

    file_stat = open(outputfile_s, 'a', encoding='utf8')
    file_stat.write('Batch stats:\n' + '_________________________________\n')

    camsi = []
    progress = 0
    sline = ''
    backet_x = bpy.context.scene.render.tile_x
    backet_y = bpy.context.scene.render.tile_y
    sq_backet = backet_x * backet_y
    rp = bpy.context.scene.render.resolution_percentage
    for cam in bpy.data.objects:
        if (cam.type == 'CAMERA' and not cam.hide_render):
            flag = False
            res = cam.data.name.split('(')
            res_x = glob_res[0]
            res_y = glob_res[1]
            if len(res) == 2:
                res = res[1].split(')')
                if len(res) == 2:
                    res = res[0].split('+')
                    if len(res) == 2:
                        res_x = int(res[0])
                        res_y = int(res[1])
                        flag = True

            camsi.append((res_x, res_y))
            p_tmp = res_x * res_y
            p_tmp_scale = round(p_tmp * rp / 100)
            progress += p_tmp
            if flag:
                sline = sline + cam.name + ' | ' + str(res_x) + 'x' + str(res_y) + ' | ' + \
                        str(round(res_x * rp / 100)) + 'x' + str(round(res_y * rp / 100)) + ' | ' + \
                        str(round(p_tmp_scale / sq_backet)) + '\n'
            else:
                sline = sline + cam.name + ' | default | ' + \
                        str(round(res_x * rp / 100)) + 'x' + str(round(res_y * rp / 100)) + ' | ' + \
                        str(round(p_tmp_scale / sq_backet)) + '\n'

    file_stat.write('Total resolution = ' + str(round(math.sqrt(progress))) + 'x' + str(round(math.sqrt(progress))) +
                    ' (' + str(round(math.sqrt(progress) * rp / 100)) + 'x' + str(
        round(math.sqrt(progress) * rp / 100)) + ')' + '\n')
    file_stat.write('Default Resolution = ' + str(glob_res[0]) + 'x' + str(glob_res[1]) + ' (' + str(rp) + '%)' + '\n')
    file_stat.write('Tiles = ' + str(backet_x) + 'x' + str(backet_y) + '\n')
    file_stat.write('Total tiles = ' + str(round(progress * rp / (sq_backet * 100))) + '\n\n')
    file_stat.write('Cameras:\n' + 'Name | resolution | scaled (' + str(rp) + '%) | tiles\n' +
                    '________________________________________\n')
    file_stat.write(sline)

    outputfile = os.path.join(filepath, 'log.txt')
    if os.path.isfile(outputfile):
        os.remove(outputfile)

    file_log = open(outputfile, 'a', encoding='utf8')
    file_log.write('Cameras:\n' + 'Name | resolution | scaled (' + str(
        rp) + '%) | progress % | remaining time | elapsed time\n' + \
                   '_____________________________________________________________________________\n')

    p_tmp = 0
    time_start = time.time()
    i = 0
    for cam in bpy.data.objects:
        if (cam.type == 'CAMERA' and not cam.hide_render):
            bpy.data.scenes[sceneName].camera = cam
            bpy.context.scene.render.resolution_x = camsi[i][0]
            bpy.context.scene.render.resolution_y = camsi[i][1]
            bpy.data.scenes[sceneName].render.filepath = filepath + '\\' + cam.name
            if config.batch_opengl:
                bpy.ops.render.opengl(animation=False, write_still=True, view_context=False)
            else:
                bpy.ops.render.render(animation=False, write_still=True)

            p_tmp += camsi[i][0] * camsi[i][1]
            proc = max(round(p_tmp * 100 / progress), 1)
            r_time = time.time() - time_start
            time_tmp = r_time * (100 - proc) / proc
            time_tmp = round(time_tmp)

            s_rt = time.strftime('%H:%M:%S', time.gmtime(r_time))
            s_lt = time.strftime('%H:%M:%S', time.gmtime(time_tmp))
            file_log.write(cam.name + ' | ' + str(camsi[i][0]) + 'x' + str(camsi[i][1]) + ' | ' + \
                           str(round(camsi[i][0] * rp / 100)) + 'x' + str(round(camsi[i][1] * rp / 100)) + ' | ' + \
                           str(proc) + ' | ' + s_lt + ' | ' + s_rt + '\n')
            i += 1

    bpy.context.scene.render.resolution_x = glob_res[0]
    bpy.context.scene.render.resolution_y = glob_res[1]
    file_stat.close()
    file_log.close()
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


############# End PolyCams Render ################


class PaImageTPanel(bpy.types.Panel):
    bl_label = "1D_Scripts "
    bl_space_type = 'IMAGE_EDITOR'
    bl_region_type = 'TOOLS'
    bl_category = '1D'
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        layout = self.layout
        col = layout.column(align=True)
        row = col.row(align=False)
        row.operator("suv.spreads", text='Print loop')


def panel_add_button(base_layout, operator, text, align=False):
    row = base_layout.row(align=align)
    row.operator(operator.bl_idname, text=text)
    return row


def panel_add_spoiler(base_layout, prop, text):
    lt = bpy.context.window_manager.paul_manager
    split = base_layout.split()
    if getattr(lt, prop, False):
        split.prop(lt, prop, text=text, icon='DOWNARROW_HLT')
    else:
        split.prop(lt, prop, text=text, icon='RIGHTARROW')

    if getattr(lt, prop, False):
        box = base_layout.column(align=True).box().column(align=True)
        col_top = box.column(align=True)
        return col_top
    return None


def panel_add_button_and_box(base_layout, operator, text, spoiler, align=False):
    lt = bpy.context.window_manager.paul_manager
    row = base_layout.row(align=align)
    row.operator(operator, text=text)
    row.prop(lt, spoiler, text='', icon='DOWNARROW_HLT' if getattr(lt, spoiler, False) else 'RIGHTARROW')
    if getattr(lt, spoiler, False):
        row = base_layout.row()
        box2 = row.box().box()
        col2 = box2.column()
        return col2
    return None


class LayoutSSPanel(bpy.types.Panel):
    def axe_select(self, context):
        axes = ['X', 'Y', 'Z']
        return [tuple(3 * [axe]) for axe in axes]

    def project_select(self, context):
        projects = ['XY', 'XZ', 'YZ', 'XYZ']
        return [tuple(3 * [proj]) for proj in projects]

    bl_label = "1D_Scripts %d.%d.%d" % bl_info["version"]
    bl_idname = "Paul_Operator"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    bl_category = '1D'
    # bl_context = "mesh_edit"
    bl_options = {'DEFAULT_CLOSED'}

    bpy.types.Scene.AxesProperty = bpy.props.EnumProperty(items=axe_select)
    bpy.types.Scene.ProjectsProperty = bpy.props.EnumProperty(items=project_select)
    bpy.types.Scene.path_obj = bpy.props.StringProperty(name="Path")
    bpy.types.Scene.corner_obj = bpy.props.StringProperty(name="Corner")
    bpy.types.Scene.linear_obj = bpy.props.StringProperty(name="Linear")

    '''
    @classmethod
    def poll(cls, context):
        return context.active_object is not None'''

    @property
    def props(self):
        return self.scene.batch_panel_settings

    def draw(self, context):
        lt = bpy.context.window_manager.paul_manager
        scene = context.scene
        self.scene = scene

        layout = self.layout
        col_main = layout.column(align=True)

        row = col_main.row(align=False)
        row.operator("mesh.simple_scale_operator", text='Get Orientation').type_op = 1

        row = col_main.row(align=False)
        row.operator("mesh.simple_scale_operator", text='XYcollapse').type_op = 0

        col = col_main

        lay_cad = panel_add_spoiler(base_layout=col_main, prop='disp_cad', text='CAD')
        if lay_cad:
            lay_aligner = panel_add_spoiler(base_layout=lay_cad, prop='display_align', text='Aligner')
            if lay_aligner:
                if lt.display_align and context.mode == 'EDIT_MESH':
                    col_top = lay_aligner.column(align=True)
                    row = col_top.row(align=True)
                    row.operator("mesh.align_operator", text='Store Edge').type_op = 1
                    row = col_top.row(align=True)
                    row.operator("mesh.align_operator", text='Align').type_op = 0
                    row = col_top.row(align=True)
                    row.prop(lt, 'align_dist_z', text='Superpose')
                    row = col_top.row(align=True)
                    row.prop(lt, 'align_lock_z', text='lock Z')

                if lt.display_align and context.mode == 'OBJECT':
                    col_top = lay_aligner.column(align=False)
                    row = col_top.row(align=True)
                    row.operator("mesh.align_operator", text='Store Edge').type_op = 1
                    row = col_top.row(align=True)
                    row.operator("mesh.align_operator", text='Align').type_op = 2
                    col_top = col_top.column(align=False)
                    row = col_top.row(align=True)
                    row.prop(context.scene, 'AxesProperty', text='Axis')
                    row = col_top.row(align=True)
                    row.prop(context.scene, 'ProjectsProperty', text='Projection')

            lay_sideshift = panel_add_spoiler(base_layout=lay_cad, prop='display_offset', text='Sideshift')
            if lay_sideshift:
                col_top = lay_sideshift.column(align=True)
                row = col_top.row(align=True)
                row.operator("paul.sideshift_dist", text='Store dist')
                row = col_top.row(align=True)
                row.operator("paul.sideshift_cursor", text='Active » Cursor')

                row = col_top.row(align=True)
                row.prop(lt, "shift_lockX", text="X", icon='FREEZE')
                row.prop(lt, "shift_lockY", text="Y", icon='FREEZE')
                row.prop(lt, "shift_lockZ", text="Z", icon='FREEZE')

                col_top.row(align=True)
                split = col_top.split(percentage=0.76)
                split.prop(lt, 'step_len', text='dist')
                split.operator("mesh.offset_operator", text="Restore").type_op = 1
                col_top.row(align=True)
                split = col_top.split(percentage=0.5)
                split.operator("paul.sideshift_backward", text="", icon='TRIA_LEFT')
                split.operator("paul.sideshift_forward", text="", icon='TRIA_RIGHT')
                row = col_top.row(align=True)
                if context.mode == 'EDIT_MESH':
                    row.prop(lt, "shift_copy", text="Copy")
                else:
                    row.prop(lt, "instance", text='Instance')
                    row = col_top.row(align=True)
                    row.prop(lt, "shift_copy", text="Copy")

            lay_3dmatch = panel_add_spoiler(base_layout=lay_cad, prop='display_3dmatch', text='3D Match')
            if lay_3dmatch:
                col_top = lay_3dmatch.column(align=True)
                row = col_top.row(align=True)
                row.operator("mesh.align_operator", text='Store key').type_op = 3
                row = col_top.row(align=True)
                row.operator("mesh.align_operator", text='mirrorside').type_op = 7
                row = col_top.row(align=True)
                split = row.split(0.33, True)
                split.scale_y = 1.5
                split.operator("mesh.align_operator", text='Flip').type_op = 6
                split.operator("mesh.align_operator", text='3D Match').type_op = 5

            lay_polycross = panel_add_spoiler(base_layout=lay_cad, prop='disp_cp', text='Polycross')
            if lay_polycross:
                col_top = lay_polycross.column(align=True)
                row = col_top.row(align=True)
                split = row.split()
                if lt.disp_cp_project:
                    split.prop(lt, "disp_cp_project", text="Project active", icon='DOWNARROW_HLT')
                else:
                    split.prop(lt, "disp_cp_project", text="Project active", icon='RIGHTARROW')

                if lt.disp_cp_project:
                    box = col_top.column(align=True).box().column()
                    row = box.row(align=True)
                    split = row.split(0.5, True)
                    split.operator("mesh.polycross", text='Section').type_op = 0  # section and clear filter
                    split.operator("mesh.polycross", text='Cut').type_op = 1  # cross
                    row = box.row(align=True)
                    row.prop(lt, "fill_cuts", text="fill cut")
                    row = box.row(align=True)
                    row.prop(lt, "outer_clear", text="remove front")
                    row = box.row(align=True)
                    row.prop(lt, "inner_clear", text="remove bottom")

                row = col_top.row(align=True)
                split = row.split()
                if lt.disp_cp_filter:
                    split.prop(lt, "disp_cp_filter", text="Selection Filter", icon='DOWNARROW_HLT')
                else:
                    split.prop(lt, "disp_cp_filter", text="Selection Filter", icon='RIGHTARROW')

                if lt.disp_cp_filter:
                    box = col_top.column(align=True).box().column()
                    row = box.row(align=True)
                    row.operator("mesh.polycross", text='to SELECT').type_op = 2  # only filter
                    row = box.row(align=True)
                    row.prop(lt, "filter_edges", text="Filter Edges")
                    row = box.row(align=True)
                    row.prop(lt, "filter_verts_top", text="Filter Top")
                    row = box.row(align=True)
                    row.prop(lt, "filter_verts_bottom", text="Filter Bottom")

            lay_rotor_scaler = panel_add_spoiler(base_layout=lay_cad, prop='disp_3drotor', text='3D Rotor/Scaler')
            if lay_rotor_scaler:
                col_top = lay_rotor_scaler.column(align=True)
                row = col_top.row(align=True)
                row.operator("mesh.rotor_operator", text='Store key').type_op = 1
                row = col_top.row(align=True)
                row.label(text='Scaler')
                col_top.row(align=True)
                split = col_top.split(percentage=0.5)
                left_op = split.operator("mesh.rotor_operator", text="", icon='TRIA_LEFT')
                left_op.type_op = 5
                left_op.sign_op = -1
                right_op = split.operator("mesh.rotor_operator", text="", icon='TRIA_RIGHT')
                right_op.type_op = 5
                right_op.sign_op = 1
                row = col_top.row(align=True)
                row.label(text='Rotor')
                split = col_top.split(percentage=0.5)
                left_op = split.operator("mesh.rotor_operator", text="", icon='TRIA_LEFT')
                left_op.type_op = 0
                left_op.sign_op = -1
                right_op = split.operator("mesh.rotor_operator", text="", icon='TRIA_RIGHT')
                right_op.type_op = 0
                right_op.sign_op = 1
                row = col_top.row(align=True)
                if context.mode == 'EDIT_MESH':
                    row.prop(lt, "rotor3d_copy", text="Copy")
                else:
                    row.prop(lt, "rotor3d_instance", text='Instance')
                    row = col_top.row(align=True)
                    row.prop(lt, "rotor3d_copy", text="Copy")

            lay_corner = panel_add_spoiler(base_layout=lay_cad, prop='disp_corner', text='Corner Edges')
            if lay_corner:
                layout = lay_corner.column(align=True)
                layout.operator("mesh.corner", text='Corner').type_op = 0
                layout.operator("mesh.corner", text='Extend').type_op = 1
                coner_act = lt.corner_active_edge
                coner_to_act = lt.to_corner_active_edge
                row = layout.row(align=True)
                if coner_to_act:
                    row.active = False
                    lt.corner_active_edge = False
                row.prop(lt, "corner_active_edge", text='Only active edge')
                row = layout.row(align=True)
                if coner_act:
                    row.active = False
                    lt.to_corner_active_edge = False
                row.prop(lt, "to_corner_active_edge", text='To active edge')

                col_in = layout.column(align=True)
                col_in.operator(AMCornerCross.bl_idname, text="Extend cross")
                col_in.operator(AMExtendCross.bl_idname, text="Corner cross")
                col_in.prop(lt, "corner_overlap", text="Overlap")

            row = lay_cad.row(align=True)
            row.operator("paul.verts_project_on_edge", text='Verts project')
            row.prop(lt, "vproj_active", text='', icon='EDGESEL' if lt.vproj_active else 'MATCUBE')

        lay_edgloop = panel_add_spoiler(base_layout=col_main, prop='display_edgloop', text='Edges/Loops')
        if lay_edgloop:
            col_top = lay_edgloop.column(align=True)

            # Loop Resolve
            row = col_top.row(align=True)
            row.operator("paul.loop_resolve", text='Loop Resolve')
            row.prop(lt, "disp_loopresolve", text='', icon='DOWNARROW_HLT' if lt.disp_loopresolve else 'RIGHTARROW')
            if lt.disp_loopresolve:
                row = col_top.row(align=True)
                row2 = row.box().box()
                if lt.loopresolve_relative:
                    row2.prop(lt, 'loopresolve_step', text='Step')
                else:
                    row2.prop(lt, 'loopresolve_dist', text='Dist')

                row2.prop(lt, 'loopresolve_relative', text='', icon='ALIGN')

            # Spread Loop
            row = col_top.row(align=True)
            row.operator("mesh.spread_operator", text='Spread Loop')
            row.prop(lt, "display", text='', icon='DOWNARROW_HLT' if lt.display else 'RIGHTARROW')
            if lt.display:
                row = col_top.row(align=True)
                box2 = row.box().box()
                col2 = box2.column(align=True)
                row2 = col2.row(align=True)
                row2.prop(lt, 'spread_x', text='Spread X')
                row2 = col2.row(align=True)
                row2.prop(lt, 'spread_y', text='Spread Y')
                row2 = col2.row(align=True)
                row2.prop(lt, 'spread_z', text='Spread Z')
                row2 = col2.row(align=True)
                row2.prop(lt, 'relation', text='Uniform')
                box2 = col2.box().column()
                row2 = box2.row(align=True)
                row2.prop(lt, 'shape_spline', text='Shape spline')
                row2 = box2.row(align=True)
                row2.active = lt.shape_spline
                row2.prop(lt, 'spline_Bspline2', text='Smooth transition')

            # Create B-Arc
            row = col_top.row(align=True)
            row.operator("mesh.barc", text='Create B-Arc').type_op = 0
            row.prop(lt, "disp_barc", text='', icon='DOWNARROW_HLT' if lt.disp_barc else 'RIGHTARROW')
            if lt.disp_barc:
                row2 = col_top.row(align=True)
                box2 = row2.box().box()
                col_top2 = box2.column(align=True)
                row = col_top2.row(align=True)
                row.prop(lt, "barc_rad", text="Radius")
                col_top2 = box2.column(align=True)
                row = col_top2.row(align=True)
                row.operator("mesh.barc", text="Set radius").type_op = 1
                col_top2 = box2.column(align=True)
                row = col_top2.row(align=True)
                row.operator("mesh.barc", text="Cursor to center").type_op = 2

            # Ed reduce x2'
            row = col_top.row(align=True)
            row.operator("mesh.modal_cheredator", text='Ed reduce x2').type_op = 0
            row.prop(lt, "disp_reduce", text='', icon='DOWNARROW_HLT' if lt.disp_reduce else 'RIGHTARROW')
            if lt.disp_reduce:
                row = col_top.row(align=True)
                box2 = row.box().box()
                row2 = box2.column(align=True)
                row2.operator("mesh.modal_cheredator", text='run reduce loop').type_op = 1

            # Set Edges Length
            row = col_top.column(align=True)
            lay_sel = panel_add_spoiler(base_layout=row, prop='disp_sel', text='Set Edges Length')
            if lay_sel:
                row = lay_sel.column(align=True)
                row.operator("mesh.setedgslen", text='Set from MID').type_op = 0
                row.operator("mesh.setedgslen", text='Set from cursor').type_op = 3
                row.operator("mesh.setedgslen", text='Set to cursor').type_op = 1
                row.operator("mesh.setedgslen", text='Set Key').type_op = 2
                row.prop(lt, "active_length_ratio", text='Active length Ratio')

            # AutoFaceAngleSharp
            row = col_top.row(align=True)
            row.operator("object.afas", text='AutoFaceAngleSharp')
            row.prop(lt, "disp_afas", text='', icon='DOWNARROW_HLT' if lt.disp_afas else 'RIGHTARROW')
            if lt.disp_afas:
                row = col_top.row(align=True)
                row2 = row.box().box()
                row2.prop(lt, 'afas_angle', text='Angle')

            # Edges pairfill'
            row = col_top.row(align=True)
            row.operator("paul.edges_pairfill", text='Edges pairfill')
            row.prop(lt, "disp_pairfill", text='', icon='DOWNARROW_HLT' if lt.disp_pairfill else 'RIGHTARROW')
            if lt.disp_pairfill:
                row = col_top.row(align=True)
                row2 = row.box().box()
                row2.prop(lt, 'pairfill_options', text='Method')

            # Ring reduce
            row = col_top.row(align=True)
            row.operator("paul.loop_reduce", text='Ring Reduce')
            row.prop(lt, "disp_loopreduce", text='', icon='DOWNARROW_HLT' if lt.disp_loopreduce else 'RIGHTARROW')
            if lt.disp_loopreduce:
                row = col_top.row(align=True)
                row2 = row.box().box()
                row2.prop(lt, 'loopreduce_step', text='Step')

            # 3DLoop
            row = col_top.row(align=True)
            row.operator("mesh.projectloop", text='3DLoop')

        lay_naminginstances = panel_add_spoiler(base_layout=col_main, prop='disp_naminginstances', text='Naming/Instances')
        if lay_naminginstances:
            col_top = lay_naminginstances.column(align=True)
            row = col_top.row(align=True)
            row.operator("paul.select_instances", text='Select iinstances')
            row = col_top.row(align=True)
            row.operator("paul.filter_instances", text='Filter iiinstances')
            row = col_top.row(align=True)
            row.operator("paul.obname_to_meshname", text='Obname to Meshname >')
            row = col_top.row(align=True)
            row.operator("paul.meshname_to_obname", text='Meshname to Obname <')
            row = col_top.row(align=True)
            row.operator("paul.obj_distribute_by_x", text='Obj Distribute by X')
            row = col_top.row(align=True)
            row.operator("paul.drop_instances", text='Drop Instances')
            row = col_top.row(align=True)
            row.operator("paul.isolate_layers", text='Isolate layers')
            row = col_top.row(align=True)
            row.operator("object.misc", text='Obj ignore instances').type_op = 0
            row = col_top.row(align=True)
            row.operator("paul.instances_sel_pair", text='Instances select pair')
            row = col_top.row(align=True)
            row.operator("paul.propagate_obname", text='Propagate Obname')
            row = col_top.row(align=True)
            row.operator("paul.instances_rename", text='Instances Rename')
            row = col_top.row(align=True)
            row.operator("paul.obname_mat", text='Obname materials')
            row = col_top.row(align=True)
            row.operator("paul.instances_meshname_replace", text='Instances ++ replace')
            row.prop(lt, "disp_inst_repl", text='', icon='DOWNARROW_HLT' if lt.disp_inst_repl else 'RIGHTARROW')
            if lt.disp_inst_repl:
                row = col_top.row(align=True)
                col2 = row.box().box().column()
                col2.prop(lt, 'inst_repl_use_translation', text='Use translation')
                col2 = col2.column()
                col2.active = lt.inst_repl_use_translation
                col2.prop(lt, 'inst_repl_select', text='Selected only')
                col2.prop(lt, 'inst_repl_from', text='From')
                col2.prop(lt, 'inst_repl_to', text='To')
            row = col_top.row(align=True)
            row.operator("paul.instances_sel_unique", text='Instances select unique')
            row = col_top.row(align=True)
            row.operator("paul.search_instanses_1", text='Guess Active Instances')
            row.prop(lt, "disp_si1", text='', icon='DOWNARROW_HLT' \
                if lt.disp_si1 else 'RIGHTARROW')
            if lt.disp_si1:
                row = col_top.row(align=True)
                row2 = row.box().box().row()
                row2.prop(lt, 'si_percent', text='Percent')
                row2.prop(lt, 'filter_mats', icon='MATERIAL', text='')
            row = col_top.row(align=True)
            row.operator("paul.search_instanses_2", text='Guess Chain Instances')
            row.prop(lt, "disp_si2", text='', icon='DOWNARROW_HLT' \
                if lt.disp_si2 else 'RIGHTARROW')
            if lt.disp_si2:
                row = col_top.row(align=True)
                row2 = row.box().box().row()
                row2.prop(lt, 'si_percent', text='Percent')
                row2.prop(lt, 'filter_mats', icon='MATERIAL', text='')
            row = col_top.row(align=True)
            row.operator("paul.gsl", text='Group Select Linked')

        lay_objed = panel_add_spoiler(base_layout=col_main, prop='disp_objed', text='Object/Edit')
        if lay_objed:
            col_top = lay_objed.column(align=True)
            row = col_top.row(align=True)
            row.operator("paul.instances_recount", text='Obj Verts report')
            row.prop(lt, "disp_ovr", text='', icon='DOWNARROW_HLT' if lt.disp_ovr else 'RIGHTARROW')

            if lt.disp_ovr:
                row = col_top.row(align=True)
                row2 = row.box().box()
                row2.prop(lt, 'ovr_options', text='Sorting option')
                row2 = row2.row(align=True)
                row2.prop(lt, 'ovr_count')

            row = lay_objed.row(align=True)
            row_ = row.split(0.7, align=True)
            row_.operator("object.switch", text='Outliner set on').type_op = 16
            row_.operator("object.switch", text='off').type_op = 17
            row.prop(lt, "oso_vizing", text='', icon='RESTRICT_VIEW_ON' if lt.oso_vizing else 'RESTRICT_VIEW_OFF')
            row.prop(lt, "oso_select", text='', icon='RESTRICT_SELECT_ON' if lt.oso_select else 'RESTRICT_SELECT_OFF')
            row.prop(lt, "oso_render", text='', icon='RESTRICT_RENDER_ON' if lt.oso_render else 'RESTRICT_RENDER_OFF')

            lay_obj_compare = panel_add_spoiler(base_layout=lay_objed, prop='disp_compmeshes', text='Objects Compare')
            if lay_obj_compare:
                row = lay_obj_compare.column(align=True)
                row.operator("object.compare_meshes", text='Read mats from active').type_op = 1
                row = lay_obj_compare.column(align=True)
                row.operator("object.compare_meshes", text='Compare vertices').type_op = 0
                row = lay_obj_compare.column(align=False)
                row.prop(lt, 'compmeshes_treshold', text='treshold')

            row = lay_objed.row(align=True)
            row.operator("object.select_modified", text='Obj select Modified')

            row = lay_objed.row(align=True)
            row.operator("paul.filter_dupes_origins", text='Obj Filter dupes')
            row.prop(lt, "verts_activate", text='', icon='EDITMODE_HLT' if lt.verts_activate else 'MATCUBE')

            row = lay_objed.row(align=True)
            row.operator("paul.obj_filter_local_rotated", text='Obj Filter local rotated')

            row = lay_objed.row(align=True)
            row.operator("paul.obj_filter_neg_scale", text='Obj Filter negative scale')

            row = lay_objed.row(align=True)
            row.operator(PaNJoin.bl_idname, text='Negative join')

            row = lay_objed.row(align=True)
            row.operator("paul.set_autosmooth", text='Set Autosmooth')

            row = lay_objed.row(align=True)
            row.operator("object.curves_select_2d", text='Curves select 2D')

            row = lay_objed.row(align=True)
            row.operator("object.curve_swap", text='Curve swap 2D/3D')

            lay_chunks = panel_add_button_and_box(base_layout=lay_objed, operator='mesh.sel_chunks',
                                                  text='Select Chunks', spoiler='disp_chunks', align=True)
            if lay_chunks:
                col = lay_chunks.column(align=False)
                row = col.row(align=False)
                row.prop(lt, "chunks_clamp", text='clamp')
                row = col.row(align=False)
                row.prop(lt, "chunks_setting", text='Variant')

            if context.mode == 'EDIT_MESH':
                lay_dist_verts = panel_add_spoiler(base_layout=lay_objed, prop='disp_distverts', text='Dist Vertices')
                if lay_dist_verts:
                    row = lay_dist_verts.column(align=False)
                    row.prop(lt, 'dist_verts', text='dist')
                    row = lay_dist_verts.column(align=True)
                    row.operator("mesh.dist_verts", text='Find doubles verts').type_op = 0
                    row.operator("mesh.dist_verts", text='Select radius verts').type_op = 1

            col = lay_objed.column(align=False)
            row = col.row(align=True)
            row.operator(PaVolumeSelect.bl_idname, text='Volume Select')
            row.prop(lt, "valsel_objectmode", text='', icon='OBJECT_DATAMODE' if lt.valsel_objectmode
            else 'EDITMODE_HLT')

        col = col_main
        lay_misc = panel_add_spoiler(base_layout=col_main, prop='disp_materials', text='Materials')
        if lay_misc:
            col_top = lay_misc.column(align=True)
            row = col_top.row(align=True)
            row.operator("paul.mats_datafix", text='Mats Datafix')
            row = col_top.row(align=True)
            row.operator("paul.mats_sel_multiple", text='Mats select multiple')
            row = col_top.row(align=True)
            row.operator("object.misc", text='MatchProp').type_op = 13
            row = col_top.row(align=True)
            row.operator("object.misc", text='Mats all to active').type_op = 8
            row = col_top.row(align=True)
            row.operator("object.misc", text='Mats selected to active').type_op = 14
            row = col_top.row(align=True)
            row.operator("material.paul_sort", text='Mats sort')
            row = col_top.row(align=True)
            row.operator("object.misc", text='Mats suppress RGB').type_op = 4
            row = col_top.row(align=True)
            row.operator("paul.mats_unclone", text='Mats Unclone')
            row = col_top.row(align=True)
            row.operator("paul.mats_purgeout", text='Mats Purgeout')
            row = col_top.row(align=True)
            row.operator("object.misc", text='Matname HVS set').type_op = 9
            row = col_top.row(align=True)
            row.operator("object.misc", text='Matname HVS del').type_op = 10
            row = col_top.row(align=True)
            row.operator("object.misc", text='Matnodes switch').type_op = 7

        lay_build = panel_add_spoiler(base_layout=col_main, prop='disp_build', text='Build')
        if lay_build:
            if context.mode == 'OBJECT':
                lay_railer = panel_add_spoiler(base_layout=lay_build, prop='display_railer', text='Railer')
                if lay_railer:
                    col_top = lay_railer.column(align=True)
                    row = col_top.row(align=True)

                    row.prop(context.scene, 'path_obj', icon='OBJECT_DATAMODE')
                    row.operator("object.railer_operator", icon='EYEDROPPER', text='').type_op = 1
                    row = col_top.row(align=True)
                    row.prop(context.scene, 'corner_obj', icon='OBJECT_DATAMODE')
                    row.operator("object.railer_operator", icon='EYEDROPPER', text='').type_op = 2
                    row = col_top.row(align=True)
                    row.prop(context.scene, 'linear_obj', icon='OBJECT_DATAMODE')
                    row.operator("object.railer_operator", icon='EYEDROPPER', text='').type_op = 3

                    col_top = lay_railer.column(align=True)
                    row = col_top.row(align=False)
                    row.prop(lt, 'railer_dist', text='dist')

                    col_top = lay_railer.column(align=True)
                    row = col_top.row(align=True)
                    row.operator("object.railer_operator", text='Build').type_op = 4

            row = lay_build.row(align=True)
            row.operator("paul.make_border", text='Make Border')
            row.prop(lt, "disp_mborder", text='', icon='DOWNARROW_HLT' if lt.disp_mborder else 'RIGHTARROW')
            if lt.disp_mborder:
                row = lay_build.row(align=True)
                row2 = row.box()
                row2.prop(lt, 'mborder_size', text='Size')

            row = lay_build.row(align=True)
            row.operator("paul.stairs_maker", text='Stairs Maker')

            lay_wall_extrude = panel_add_spoiler(base_layout=lay_build, prop='disp_matExtrude', text='WallExtrude')
            if lay_wall_extrude:
                row = lay_wall_extrude.row(align=True)
                row.operator("mesh.get_mat4extrude", text='Get Mats')
                row = lay_wall_extrude.row(align=True)
                row.operator("mesh.mat_extrude", text='Template Extrude')

        split = col.split()
        if lt.disp_render:
            split.prop(lt, "disp_render", text="Render", icon='DOWNARROW_HLT')
        else:
            split.prop(lt, "disp_render", text="Render", icon='RIGHTARROW')

        if lt.disp_render:
            box = col.column(align=True).box().column()
            col_render = box.column(align=True)

            row = col_render.row(align=True)
            row.operator('scene.camswitch', text='Prev', icon='TRIA_LEFT').next = False
            row.operator('scene.camswitch', text='Next', icon='TRIA_RIGHT').next = True

            col_top = col_render.column(align=True)

            split = col_top.split()
            if lt.disp_batch:
                split.prop(lt, "disp_batch", text="Batch Render", icon='DOWNARROW_HLT')
            else:
                split.prop(lt, "disp_batch", text="Batch Render", icon='RIGHTARROW')

            if lt.disp_batch:
                box = col_render.column(align=True).box().column()
                col_top = box.column(align=True)
                col_top.prop(lt, "batch_opengl", text="OpenGL Render")
                col_top = box.column(align=True)
                col_top.operator("scene.render_me", text='Batch Render')
                col_top = box.column(align=True)
                col_top.operator("paul.read_camera_setup", text='RCS Read Camera setup')

            col_top = col_render.column(align=False)
            col_top.operator('timelinerender.start', icon='TIME', text='Start TimeLine Render')

        split = col.split()
        if lt.disp_bremover:
            split.prop(lt, "disp_bremover", text="Batch Remover", icon='DOWNARROW_HLT')
        else:
            split.prop(lt, "disp_bremover", text="Batch Remover", icon='RIGHTARROW')
        if lt.disp_bremover:
            box = col.column(align=True).box().column()
            col_top = box.column(align=False)
            create_panel_batch_remover(col=col_top, scene=scene)

        def _FEDGE():
            pass

        split = col.split(percentage=0.15)
        if lt.disp_fedge:
            split.prop(lt, "disp_fedge", text="", icon='DOWNARROW_HLT')
        else:
            split.prop(lt, "disp_fedge", text="", icon='RIGHTARROW')

        split.operator("object.fedge", text='Fedge')
        if lt.disp_fedge:
            box = col.column(align=True).box().column()
            col_top = box.column(align=True)
            row = col_top.row(align=True)
            row.prop(lt, 'fedge_verts', text='verts')
            row = col_top.row(align=True)
            row.prop(lt, 'fedge_edges', text='edges')
            row = col_top.row(align=True)
            row.prop(lt, 'fedge_nonquads', text='nonquads')
            row = col_top.row(align=True)
            row.prop(lt, 'fedge_three', text='ngons')
            row = col_top.row(align=True)
            row.prop(lt, 'fedge_tris', text='tris')
            row = col_top.row(align=True)
            row.prop(lt, 'fedge_snm', text='non manifold')
            row = col_top.row(align=True)
            row.prop(lt, 'fedge_angle', text='angle <0.5\'')
            row = col_top.row(align=True)
            split = row.split(0.4, True)
            split.prop(lt, 'fedge_zerop', text='area')
            split.prop(lt, 'fedge_WRONG_AREA', text='')

        split = col.split(percentage=0.15)
        if lt.disp_obj:
            split.prop(lt, "disp_obj", text="", icon='DOWNARROW_HLT')
        else:
            split.prop(lt, "disp_obj", text="", icon='RIGHTARROW')

        split.operator("import_scene.multiple_objs", text='Multiple obj import')
        if lt.disp_obj:
            box = col.column(align=True).box().column()
            layout = box.column(align=True)

            row = layout.row(align=True)
            row.prop(lt, "by_layers_setting")
            row = layout.row(align=True)
            row.prop(lt, "ngons_setting")
            row = layout.row(align=True)
            row.prop(lt, "edges_setting")

            layout.prop(lt, "smooth_groups_setting")

            box = layout.box()
            row = box.row()
            row.prop(lt, "split_mode_setting", expand=True)

            row = box.row()
            if lt.split_mode_setting == 'ON':
                row.label(text="Split by:")
                row.prop(lt, "split_objects_setting")
                row.prop(lt, "split_groups_setting")
            else:
                row.prop(lt, "groups_as_vgroups_setting")

            row = layout.split(percentage=0.67)
            row.prop(lt, "clamp_size_setting")
            layout.prop(lt, "axis_forward_setting")
            layout.prop(lt, "axis_up_setting")
            layout.prop(lt, "image_search_setting")

        split = col.split()
        if lt.disp_zmj100:
            split.prop(lt, "disp_zmj100", text="Integrated addons", icon='DOWNARROW_HLT')
        else:
            split.prop(lt, "disp_zmj100", text="Integrated addons", icon='RIGHTARROW')

        if lt.disp_zmj100:
            box = col.column(align=True).box().column()
            col_top = box.column(align=True)
            if lt.disp_eap:
                col_top.prop(lt, "disp_eap", text="ZMJ Extrude Along Path", icon='DOWNARROW_HLT')
            else:
                col_top.prop(lt, "disp_eap", text="ZMJ Extrude Along Path", icon='RIGHTARROW')

            if lt.disp_eap:
                box = col_top.column(align=True).box().column()
                box_ = box.box().column()
                row = box_.row(align=True)
                row = row.split(0.60, align=True)
                row.label('Path:')
                row.operator('eap.op0_id', text='Store')
                row = box_.split(0.60, align=True)
                row.label('Start point:')
                row.operator('eap.op1_id', text='Store')
                row = box_.split(0.60, align=True)
                row.label('Both:')
                row.operator('eap.op3_id', text='Store')
                row = box_.row(align=True)
                row.operator('eap.op2_id', text='Extrude')

            col_top = box.column(align=True)
            row = col_top.row(align=True)
            row.operator('f.op0_id', text='ZMJ Fillet')

            col_top = box.column(align=True)
            if lt.disp_milovsky:
                col_top.prop(lt, "disp_milovsky", text="Sure UVW Map v.0.5.1", icon='DOWNARROW_HLT')
            else:
                col_top.prop(lt, "disp_milovsky", text="Sure UVW Map v.0.5.1", icon='RIGHTARROW')

            if lt.disp_milovsky:
                box_ = box.box().column()
                row = box_.row(align=True)
                row.label("Alexander Milovsky (www.milovsky.ru)")
                row = box_.row(align=True)
                # row.operator('paul.multy_sureuv', text = 'Obj Multy SureUV')
                row = box_.row(align=True)

                split = box_.split(percentage=0.15)
                if lt.disp_omsureuv:
                    split.prop(lt, "disp_omsureuv", text="", icon='DOWNARROW_HLT')
                else:
                    split.prop(lt, "disp_omsureuv", text="", icon='RIGHTARROW')

                split.operator('paul.multy_sureuv', text='Obj Multy SureUV')
                row = box_.row(align=True)
                row.prop(lt, 'omsureuv_all_scale_def', text="Size")
                if lt.disp_omsureuv:
                    box2 = box_.box().column()
                    layout = box2.column(align=True)
                    layout.label("XYZ rotation")
                    col2 = layout.column()
                    col2.prop(lt, 'omsureuv_rot', text="")
                    layout.label("XYZ offset")
                    col2 = layout.column()
                    col2.prop(lt, 'omsureuv_offset', text="")
                    layout.label("Texture squash (optional)")
                    layout.label("Always must be 1.0 !!!")
                    layout.prop(lt, 'omsureuv_tex_aspect', text="")

                row = box_.row(align=True)
                row.label("Press this button first:")
                row = box_.row(align=True)
                row.operator("object.sureuvw_operator", text="Show active texture on object").action = 'showtex'
                row = box_.row(align=True)
                row.label("UVW Mapping:")
                row = box_.row(align=True)
                row.operator("object.sureuvw_operator", text="UVW Box Map").action = 'box'
                row = box_.row(align=True)
                row.operator("object.sureuvw_operator", text="Best Planar Map").action = 'bestplanar'
                row = box_.row(align=True)
                row.label("1. Make Material With Raster Texture!")
                row = box_.row(align=True)
                row.label("2. Set Texture Mapping Coords: UV!")
                row = box_.row(align=True)
                row.label("3. Use Addon buttons")

        def _BLENDCLEANUP():
            pass

        split = col.split()
        if lt.disp_blendupcleanup:
            split.prop(lt, "disp_blendupcleanup", text="Misc", icon='DOWNARROW_HLT')
        else:
            split.prop(lt, "disp_blendupcleanup", text="Misc", icon='RIGHTARROW')
        if lt.disp_blendupcleanup:
            box = col.column(align=True).box().column()
            col_top = box.column(align=True)

            row = col_top.row(align=True)
            row.operator("paul.sel_same_verts", text='Select same vertices')

            row = col_top.row(align=True)
            row.operator("paul.heavy_ngons", text='Heavy NGons')
            row = col_top.row(align=True)
            row.operator("paul.clean_glass", text='Clean Glass')

        def _TESTZONE():
            pass

        split = col.split()
        if lt.disp_test:
            split.prop(lt, "disp_test", text="Test Zone", icon='DOWNARROW_HLT')
        else:
            split.prop(lt, "disp_test", text="Test Zone", icon='RIGHTARROW')

        if lt.disp_test:
            box = col.column(align=True).box().column()
            col_top = box.column(align=True)

            row = col_top.row(align=True)
            row.operator("paul.instance_resizer", text='Instance Resizer')

            row = col_top.row(align=True)
            row.operator("paul.mats_equalize", text='Mats equalize')

            row = col_top.row(align=True)
            row.operator("uv.scaler", text='UV Scaler')

            row = col_top.row(align=True)
            row.operator(PaPolyedgeSelect.bl_idname, text='Polyedge select')

            row = col_top.row(align=True)
            row.operator(PaSsmooth.bl_idname, text='Ssmooth')


class D1_fedge(bpy.types.Operator):
    ''' \
    Select loose parts. edges first, vertices second, non-quad polygons third. \
    Выделяет потеряные рёбра, потом вершины и грани, каждый раз вызываясь. \
    '''
    bl_idname = "object.fedge"
    bl_label = "Fffedge"

    selected_show = False
    selected_hide = False

    def make_edges(self, edges):
        for e in edges:
            if e.is_loose:
                return True
        return False

    def make_edges2(self, bm_edges):
        for edge in bm_edges:
            if len(edge.link_faces) == 0:
                return True
        return False

    def make_non_manifold(self, data):
        edit_mode_in()
        bpy.ops.mesh.select_mode(type='EDGE')
        bpy.ops.mesh.select_all(action='DESELECT')
        bpy.ops.mesh.select_non_manifold()
        edit_mode_out()
        for e in data.edges:
            if e.select:
                return True
        return False

    # makes indexes set for compare with vertices
    # in object and find difference
    def make_indeces(self, list, vertices):
        for e in list:
            for i in e.vertices:
                vertices.add(i)

    def make_areas(self, pols):
        config = bpy.context.window_manager.paul_manager
        zerop = config.fedge_zerop
        three = config.fedge_three
        WRONG_AREA = config.fedge_WRONG_AREA / 100
        for p in pols:
            if p.area <= WRONG_AREA and zerop:
                return True
        return False

    def make_loose_angle(self, obj):
        config = bpy.context.window_manager.paul_manager
        mesh = obj.data
        ltEdges = [((e.vertices[0], e.vertices[1]), e.index) for e in mesh.edges]
        ltFaces = [([v for v in f.vertices], f.index) for f in mesh.polygons]
        for vert in mesh.vertices:
            lEdges = [e for e in ltEdges if vert.index in e[0]]
            for i, edge1 in enumerate(lEdges):
                for edge2 in lEdges[i + 1:]:
                    v2_i, v3_i = tuple(set(edge1[0]) ^ set(edge2[0]))
                    v1 = vert.co
                    v2 = mesh.vertices[v2_i].co
                    v3 = mesh.vertices[v3_i].co
                    vec1 = v2 - v1
                    vec2 = v3 - v1
                    angle = vec1.angle(vec2) * 180 / pi
                    if angle < 0.5:  # Here set angle
                        lFaces = [f[1] for f in ltFaces if v2_i in f[0]] + \
                                 [f[1] for f in ltFaces if v3_i in f[0]]
                        if len(lFaces) > 1 and lFaces[0] != lFaces[1] and len(lFaces) < 3: continue
                        return True
        return False

    def verts(self, obj, selected_hide, selected_show):
        # stage two verts
        config = bpy.context.window_manager.paul_manager
        if not config.fedge_verts:
            return selected_show, selected_hide
        bpy.ops.mesh.select_mode(type='VERT')
        bpy.ops.mesh.select_all(action='DESELECT')
        bpy.ops.object.editmode_toggle()
        vertices = set()
        self.make_indeces(obj.data.edges, vertices)
        self.make_indeces(obj.data.polygons, vertices)
        for i, ver in enumerate(obj.data.vertices):
            if i not in vertices and not ver.hide:
                ver.select = True
                selected_show = True
            elif i not in vertices and ver.hide:
                selected_hide = True
        bpy.ops.object.editmode_toggle()
        return selected_show, selected_hide

    def edges(self, obj, selected_hide, selected_show):
        # stage one edges
        config = bpy.context.window_manager.paul_manager
        if not config.fedge_edges:
            return selected_show, selected_hide
        if not selected_show:
            bpy.ops.mesh.select_mode(type='EDGE')
            bpy.ops.mesh.select_all(action='DESELECT')
            bpy.ops.object.editmode_toggle()
            for edg in obj.data.edges:
                if edg.is_loose and not edg.hide:
                    edg.select = True
                    selected_show = True
                elif edg.is_loose and edg.hide:
                    selected_hide = True
            bpy.ops.object.editmode_toggle()
        return selected_show, selected_hide

    def non_manifold(self, obj, selected_hide, selected_show):
        # stage one edges
        config = bpy.context.window_manager.paul_manager
        if not config.fedge_snm:
            return selected_show, selected_hide
        if not selected_show:
            edit_mode_out()
            edit_mode_in()
            bpy.ops.mesh.select_mode(type='EDGE')
            bpy.ops.mesh.select_all(action='DESELECT')
            bpy.ops.mesh.select_non_manifold()
            edit_mode_out()
            for edg in obj.data.edges:
                if edg.select and not edg.hide:
                    selected_show = True
                elif edg.select and edg.hide:
                    selected_hide = True
            edit_mode_in()
        return selected_show, selected_hide

    def zero(self, obj, selected_hide, selected_show):
        # stage area 0
        config = bpy.context.window_manager.paul_manager
        WRONG_AREA = config.fedge_WRONG_AREA / 100
        if not config.fedge_zerop:
            return selected_show, selected_hide
        if not selected_show:
            bpy.ops.mesh.select_mode(type='FACE')
            bpy.ops.mesh.select_all(action='DESELECT')
            bpy.ops.object.editmode_toggle()
            for pol in obj.data.polygons:
                if pol.area <= WRONG_AREA and not pol.hide:
                    pol.select = True
                    selected_show = True
                elif pol.area <= WRONG_AREA and pol.hide:
                    selected_hide = True
            bpy.ops.object.editmode_toggle()
        return selected_show, selected_hide

    def nonquads(self, obj, selected_hide, selected_show):
        # stage non quads polygons
        config = bpy.context.window_manager.paul_manager
        if not config.fedge_nonquads:
            return selected_show, selected_hide
        if not selected_show:
            bpy.ops.mesh.select_mode(type='FACE')
            bpy.ops.mesh.select_all(action='DESELECT')
            bpy.ops.object.editmode_toggle()
            for pol in obj.data.polygons:
                if len(pol.vertices) != 4 and not pol.hide:
                    pol.select = True
                    selected_show = True
                elif len(pol.vertices) != 4 and pol.hide:
                    selected_hide = True
            bpy.ops.object.editmode_toggle()
        return selected_show, selected_hide

    def three(self, obj, selected_hide, selected_show):
        # stage three polygons
        config = bpy.context.window_manager.paul_manager
        if not config.fedge_three:
            return selected_show, selected_hide
        if not selected_show:
            bpy.ops.mesh.select_mode(type='FACE')
            bpy.ops.mesh.select_all(action='DESELECT')
            bpy.ops.object.editmode_toggle()
            for pol in obj.data.polygons:
                if len(pol.vertices) > 4 and not pol.hide:
                    pol.select = True
                    selected_show = True
                elif len(pol.vertices) > 4 and pol.hide:
                    selected_hide = True
            bpy.ops.object.editmode_toggle()
        return selected_show, selected_hide

    def tris(self, obj, selected_hide, selected_show):
        # stage three polygons
        config = bpy.context.window_manager.paul_manager
        if not config.fedge_tris:
            return selected_show, selected_hide
        if not selected_show:
            bpy.ops.mesh.select_mode(type='FACE')
            bpy.ops.mesh.select_all(action='DESELECT')
            bpy.ops.object.editmode_toggle()
            for pol in obj.data.polygons:
                if len(pol.vertices) == 3 and not pol.hide:
                    pol.select = True
                    selected_show = True
                elif len(pol.vertices) == 3 and pol.hide:
                    selected_hide = True
            bpy.ops.object.editmode_toggle()
        return selected_show, selected_hide

    def loose_angle(self, obj, selected_hide, selected_show):
        config = bpy.context.window_manager.paul_manager
        if not config.fedge_angle:
            return selected_show, selected_hide
        if not selected_show:
            bpy.ops.object.editmode_toggle()
            bpy.ops.object.editmode_toggle()
            edit_mode_in
            bpy.ops.mesh.select_mode(type='EDGE')
            bpy.ops.mesh.select_all(action='DESELECT')

            mesh = obj.data
            ltEdges = [((e.vertices[0], e.vertices[1]), e.index) for e in mesh.edges]
            ltFaces = [([v for v in f.vertices], f.index) for f in mesh.polygons]
            lEdges_select = []
            for vert in mesh.vertices:
                lEdges = [e for e in ltEdges if vert.index in e[0]]
                for i, edge1 in enumerate(lEdges):
                    for edge2 in lEdges[i + 1:]:
                        v2_i, v3_i = tuple(set(edge1[0]) ^ set(edge2[0]))
                        v1 = vert.co
                        v2 = mesh.vertices[v2_i].co
                        v3 = mesh.vertices[v3_i].co
                        vec1 = v2 - v1
                        vec2 = v3 - v1
                        if vec1.length != 0 and vec2.length != 0:
                            angle = vec1.angle(vec2) * 180 / pi
                            if angle < 0.5:  # Here set angle
                                lFaces = [f[1] for f in ltFaces if v2_i in f[0]] + \
                                         [f[1] for f in ltFaces if v3_i in f[0]]
                                if len(lFaces) > 1 and lFaces[0] != lFaces[1] and len(lFaces) < 3: continue
                                lEdges_select.extend([edge1[1], edge2[1]])

            bpy.ops.object.editmode_toggle()
            for edg in lEdges_select:
                if not mesh.edges[edg].hide:
                    mesh.edges[edg].select = True
                    selected_show = True
                else:
                    selected_hide = True
            bpy.ops.object.editmode_toggle()
        return selected_show, selected_hide

    def select_loose_objt(self):
        config = bpy.context.window_manager.paul_manager
        objects = [o for o in bpy.context.selected_objects]
        if not objects:
            print_error2('Fedge founds no objects selected. ' + \
                         'Select objects or enter edit mode.', '01 fedge')
            return
        bpy.ops.object.select_all(action='DESELECT')

        def dosel(obj, renam):
            obj.select = True
            if obj.name[:9] != '__empty__' and renam:
                obj.name = '__empty__' + obj.name

        for obj in objects:
            if obj.type != 'MESH':
                continue
            data = obj.data
            bpy.context.scene.objects.active = obj
            # zero-verts objs
            if config.fedge_empty:
                if not len(data.vertices):
                    dosel(obj, True)
            # loose verts objs
            if config.fedge_verts:
                vertices = set()
                self.make_indeces(data.edges, vertices)
                self.make_indeces(data.polygons, vertices)
                v = set([i for i in range(len(data.vertices))])
                if v.difference(vertices):
                    dosel(obj, False)
            # loose edges
            if config.fedge_edges:
                bm = bmesh.new()
                bm.from_mesh(data)
                if self.make_edges2(bm.edges):
                    dosel(obj, False)

            # nonquads
            if config.fedge_nonquads:
                for p in data.polygons:
                    if len(p.vertices) != 4:
                        dosel(obj, False)

            # ngons
            if config.fedge_three:
                for p in data.polygons:
                    if len(p.vertices) > 4:
                        dosel(obj, False)
            # triangles
            if config.fedge_tris:
                for p in data.polygons:
                    if len(p.vertices) == 3:
                        dosel(obj, False)
            # non manifold
            if config.fedge_snm:
                if self.make_non_manifold(data):
                    dosel(obj, False)
            # loose angle
            if config.fedge_angle:
                if self.make_loose_angle(data.edges):
                    dosel(obj, False)
            # zero area pols condition in def
            if config.fedge_zerop:
                if self.make_areas(obj.data.polygons):
                    dosel(obj, False)

    def select_loose_edit(self):
        obj = bpy.context.active_object
        selected_show = False
        selected_hide = False

        mess_info = ''
        # stage two verts
        selected_show, selected_hide = self.verts(obj, selected_hide, selected_show)
        if selected_show:
            mess_info = 'verts'

        # stage one edges
        selected_show, selected_hide = self.edges(obj, selected_hide, selected_show)
        if selected_show and not mess_info:
            mess_info = 'edges'

        # stage non quads polygons
        selected_show, selected_hide = self.nonquads(obj, selected_hide, selected_show)
        if selected_show and not mess_info:
            mess_info = 'nonquads'

        # stage three polygons
        selected_show, selected_hide = self.three(obj, selected_hide, selected_show)
        if selected_show and not mess_info:
            mess_info = 'ngons'

        selected_show, selected_hide = self.tris(obj, selected_hide, selected_show)
        if selected_show and not mess_info:
            mess_info = 'tris'

        selected_show, selected_hide = self.non_manifold(obj, selected_hide, selected_show)
        if selected_show and not mess_info:
            mess_info = 'non manifold'

        # stage loose angle <0.5
        selected_show, selected_hide = self.loose_angle(obj, selected_hide, selected_show)
        if selected_show and not mess_info:
            mess_info = 'angle <0.5\''

        # stage area 0
        selected_show, selected_hide = self.zero(obj, selected_hide, selected_show)
        if selected_show and not mess_info:
            mess_info = 'zero area'

        # object mode if mesh clean
        if mess_info:
            mess_info = 'FEDGE: ' + mess_info
            self.report({'INFO'}, mess_info)
        elif selected_hide:
            self.report({'INFO'}, 'FEDGE: Nothing found (but hidden)')
        else:
            bpy.ops.object.editmode_toggle()
            self.report({'INFO'}, 'FEDGE: Your object is clean')

    def execute(self, context):
        if bpy.context.mode == 'OBJECT':
            self.select_loose_objt()
        elif bpy.context.mode == 'EDIT_MESH':
            self.select_loose_edit()
        return {'FINISHED'}


def selFromMid(alr=False):
    bpy.ops.object.mode_set(mode='OBJECT')
    bpy.ops.object.mode_set(mode='EDIT')
    config = bpy.context.window_manager.paul_manager
    step_len = config.step_len
    obj = bpy.context.active_object
    me = obj.data
    me.update()

    bm = bmesh.new()
    bm.from_mesh(me)
    check_lukap(bm)

    act_ = get_active_edge(bm)
    if not act_:
        print_error2('DIST is not in store', '02 selFromMid')
        bm.free()
        return False

    act = bm.verts[act_[0]].co - bm.verts[act_[1]].co
    ko_ = step_len / act.length

    sel_edges = [e for e in bm.edges if e.select]
    for se in sel_edges:
        v1 = se.verts[0]
        v2 = se.verts[1]

        vec = v2.co - v1.co
        if vec.length == 0:
            print_error2('Zero-length edge', '01 selFromMid')
            bm.free()
            return False

        koef = ko_ if alr else step_len / vec.length
        vec_c = vec / 2 + v1.co
        vec_ = vec * koef / 2
        v1.co = vec_c - vec_
        v2.co = vec_c + vec_

    bpy.ops.object.mode_set(mode='OBJECT')
    bm.to_mesh(me)
    bm.free()
    bpy.ops.object.mode_set(mode='EDIT')
    return True


def selToCursor(alr=False):
    bpy.ops.object.mode_set(mode='OBJECT')
    bpy.ops.object.mode_set(mode='EDIT')
    config = bpy.context.window_manager.paul_manager
    step_len = config.step_len
    obj = bpy.context.active_object
    me = obj.data
    me.update()

    bm = bmesh.new()
    bm.from_mesh(me)
    check_lukap(bm)

    cur3d = bpy.context.scene.cursor_location

    act_ = get_active_edge(bm)
    if not act_:
        print_error2('DIST is not in store', '02 selToCursor')
        bm.free()
        return False

    act = bm.verts[act_[0]].co - bm.verts[act_[1]].co
    ko_ = step_len / act.length

    sel_edges = [e for e in bm.edges if e.select]
    for se in sel_edges:
        v1 = se.verts[0]
        v2 = se.verts[1]

        v1_glob = obj.matrix_world * v1.co
        v2_glob = obj.matrix_world * v2.co

        v1_d = (v1_glob - cur3d).length
        v2_d = (v2_glob - cur3d).length
        v_a = v1 if v1_d <= v2_d else v2
        v_b = v1 if v_a is v2 else v2

        vec = v_a.co - v_b.co
        if vec.length == 0:
            print_error2('Zero-length edge', '01 selToCursor')
            bm.free()
            return False

        koef = ko_ if alr else step_len / vec.length
        vec_ = vec * koef
        v_a.co = v_b.co + vec_

    bpy.ops.object.mode_set(mode='OBJECT')
    bm.to_mesh(me)
    bm.free()
    bpy.ops.object.mode_set(mode='EDIT')
    return True


def selFromCursor(alr=False):
    bpy.ops.object.mode_set(mode='OBJECT')
    bpy.ops.object.mode_set(mode='EDIT')
    config = bpy.context.window_manager.paul_manager
    step_len = config.step_len
    obj = bpy.context.active_object
    me = obj.data
    me.update()

    bm = bmesh.new()
    bm.from_mesh(me)
    check_lukap(bm)

    cur3d = bpy.context.scene.cursor_location

    act_ = get_active_edge(bm)
    if not act_:
        print_error2('DIST is not in store', '02 selFromCursor')
        bm.free()
        return False

    act = bm.verts[act_[0]].co - bm.verts[act_[1]].co
    ko_ = step_len / act.length

    sel_edges = [e for e in bm.edges if e.select]
    for se in sel_edges:
        v1 = se.verts[0]
        v2 = se.verts[1]

        v1_glob = obj.matrix_world * v1.co
        v2_glob = obj.matrix_world * v2.co

        v1_d = (v1_glob - cur3d).length
        v2_d = (v2_glob - cur3d).length
        v_a = v1 if v1_d >= v2_d else v2
        v_b = v1 if v_a is v2 else v2

        vec = v_a.co - v_b.co
        if vec.length == 0:
            print_error2('Zero-length edge', '01 selFromCursor')
            bm.free()
            return False

        koef = ko_ if alr else step_len / vec.length
        vec_ = vec * koef
        v_a.co = v_b.co + vec_

    bpy.ops.object.mode_set(mode='OBJECT')
    bm.to_mesh(me)
    bm.free()
    bpy.ops.object.mode_set(mode='EDIT')
    return True


def selKey(alr=False):
    def get_active_vert(bm):
        elem, el = bm_vert_active_get(bm)
        print("elem, el", elem, el)
        result = False
        if elem != None:
            if el == 'V':
                # bpy.ops.object.mode_set(mode = 'EDIT')
                # bpy.ops.mesh.select_mode(type='VERT')
                result = bm.verts[elem]
        return result

    bpy.ops.object.mode_set(mode='OBJECT')
    bpy.ops.object.mode_set(mode='EDIT')
    config = bpy.context.window_manager.paul_manager
    step_len = config.step_len
    obj = bpy.context.active_object
    me = obj.data
    me.update()

    bm = bmesh.new()
    bm.from_mesh(me)
    check_lukap(bm)

    # Получили активную вершину
    act_v = get_active_vert(bm)
    if not act_v:
        print_error2('Active vertex is not selected', '01 selKey')
        bm.free()
        return False

    # Ищем ребра выделенные, которым принадлежит эта вершина
    edges_ = [e for e in bm.edges if e.select and act_v in e.verts]

    # Если результат - пусто или несколько ребер, выводим сообщение об ошибке
    if not edges_:
        print_error2('Key edge is not detected', '02 selKey')
        bm.free()
        return False
    elif len(edges_) > 1:
        print_error2('Too many edges from the active vertex', '03 selKey')
        bm.free()
        return False

    # Если ребро одно - запоминаем его
    act_edge = edges_[0]

    # Ищем пассивную вершину этого ребра
    pass_v = [v for v in act_edge.verts if v.index != act_v.index][0]

    # Ищем выделенные рёбра с пассивной вершиной этого ребра
    edges_ = [e for e in bm.edges if e.select and pass_v in e.verts \
              and act_v not in e.verts]

    # Если ребер несколько или пусто - выводим сообщение об ощибке
    if not edges_:
        print_error2('Key edge is not detected', '04 selKey')
        bm.free()
        return False
    elif len(edges_) > 1:
        print_error2('Too many edges from the passive vertex', '05 selKey')
        bm.free()
        return False

    # Находим третью вершину ключа
    pass_edge = edges_[0]
    third_v = [v for v in pass_edge.verts if v.index != pass_v.index][0]

    # Двигаем третью вершину ключа
    act_vec = act_v.co - pass_v.co
    pass_vec = (third_v.co - pass_v.co).normalized()
    third_v.co = pass_v.co + pass_vec * act_vec.length

    bpy.ops.object.mode_set(mode='OBJECT')
    bm.to_mesh(me)
    bm.free()
    bpy.ops.object.mode_set(mode='EDIT')
    return True


def getChoseSelection(collection, prop=None):
    res = prop
    for c in collection:
        if c.select:
            if hasattr(c, 'name'):
                res = c.name
            elif hasattr(c, 'index'):
                res = c.index

    prop = res
    return res


def main_railer(dist=1, z_up=False, follow_path=False, flat=False, instance=False, seed=0):
    def getDeltaVec(v1, v2, dist_l, norm=True):
        v = v2 - v1
        if norm:
            v.normalize()
        v = v * dist
        if flat and z_up:
            l = v.length
            v_ = mathutils.Vector((v.x, v.y, 0))
            l_ = v_.length
            k = l / l_
            v = v * k
        return mathutils.Vector(v)

    scn = bpy.context.scene
    if scn.path_obj not in scn.objects or \
            scn.corner_obj not in scn.objects or \
            scn.linear_obj not in scn.objects:
        print_error2('Non-existent objects', 'main_railer 00')
        return False

    obj_path = scn.objects[scn.path_obj]
    obj_corner = scn.objects[scn.corner_obj]
    obj_linear = scn.objects[scn.linear_obj]

    if not obj_path.type == 'CURVE':
        print_error2('Path should be the curve', 'main_railer 01')
        return False

    if not obj_corner.type == 'MESH' or not obj_linear.type == 'MESH':
        print_error2('Corner and Linear should be the curve', 'main_railer 02')
        return False

    for spline in obj_path.data.splines:
        corners = [p.co for p in spline.points]
        bpy.ops.object.select_all(action='DESELECT')
        bpy.ops.object.select_pattern(pattern=obj_corner.name)

        bm = bmesh.new()
        bm.from_mesh(obj_corner.data)
        check_lukap(bm)
        geom_ = bm.verts[:] + bm.edges[:] + bm.faces[:]

        bm_l = bmesh.new()
        bm_l.from_mesh(obj_linear.data)
        check_lukap(bm_l)
        geom_l = bm_l.verts[:] + bm_l.edges[:] + bm_l.faces[:]
        c0 = obj_path.matrix_world * corners[0]
        c0 = Vector((c0.x, c0.y, c0.z))

        if seed == 0:
            vec_1 = mathutils.Vector((1, 0, 0))
        else:
            vec_1 = mathutils.Vector((0, 1, 0))

        vec_top = mathutils.Vector((0, 0, 1))

        for vec in corners:
            location = obj_path.matrix_world * vec
            location = Vector((location.x, location.y, location.z))

            dir = location - c0
            dist_c = dir.length
            count = int(dist_c // dist)
            dist_l0 = dist_c % dist / 2

            mat_rot = vec_1.rotation_difference(dir).to_matrix().to_4x4()
            if z_up:
                vec_nor = mat_rot * vec_top
                mat_top_rot = vec_nor.rotation_difference(vec_top).to_matrix().to_4x4()
                mat_rot = mat_top_rot * mat_rot

                vec_norx = mat_rot * vec_1
                vec_norx.z = 0
                vec_nort = dir.copy()
                vec_nort.z = 0
                mat_norx = vec_norx.rotation_difference(vec_nort).to_matrix().to_4x4()
                mat_rot = mat_norx * mat_rot

            bpy.ops.object.select_all(action='DESELECT')
            bpy.ops.object.select_pattern(pattern=obj_linear.name)

            if not follow_path:
                mat_rot = mathutils.Matrix()

            sum_l = 0
            if dist_c > 0:
                locs = []
                for i in range(count):
                    if i == 0:
                        dist_l = dist_l0
                    else:
                        dist_l = dist

                    dvec = getDeltaVec(c0, location, dist_l, True)
                    sum_l += dvec.length
                    if sum_l > dist_c:
                        break

                    loc = c0 + dvec

                    if not instance:
                        ret_l = bmesh.ops.duplicate(bm_l, geom=geom_l)
                        geom_dup_l = ret_l['geom']
                        verts_dupe_l = [ele for ele in geom_dup_l
                                        if isinstance(ele, bmesh.types.BMVert)]
                        del ret_l

                        bmesh.ops.rotate(
                            bm_l,
                            verts=verts_dupe_l,
                            cent=(0.0, 0.0, 0.0),
                            matrix=mat_rot)

                        bmesh.ops.translate(
                            bm_l,
                            verts=verts_dupe_l,
                            vec=loc)

                    c0 = loc
                    locs.append(loc)

                if instance:
                    for loc in locs:
                        bpy.ops.object.mode_set(mode='OBJECT')
                        bpy.context.scene.objects.active = obj_linear
                        bpy.ops.object.select_all(action='DESELECT')
                        bpy.ops.object.select_pattern(pattern=obj_linear.name)
                        bpy.ops.object.duplicate(linked=True)

                        obja = bpy.context.scene.objects.active

                        loc2 = loc - obja.location
                        mat_loc = mathutils.Matrix.Translation(loc2)
                        mat_loc2 = mathutils.Matrix.Translation(-loc2)
                        mat_rot2 = obja.rotation_euler.copy()
                        loc_, rot_, sca_ = obja.matrix_world.decompose()
                        rot_inv = rot_.to_matrix().to_4x4().inverted()

                        obja.matrix_world *= rot_inv
                        mat_out = mat_loc * mat_rot * mat_loc2
                        obja.matrix_world = obja.matrix_world * mat_out * rot_.to_matrix().to_4x4()
                        obja.location = loc

            c0 = location

            if dist_c == 0 and len(corners) > 1 and follow_path:
                c1 = obj_path.matrix_world * corners[1]
                c1 = Vector((c1.x, c1.y, c1.z))
                dir = c1 - location
                mat_rot = vec_1.rotation_difference(dir).to_matrix().to_4x4()

                if z_up:
                    vec_nor = mat_rot * vec_top
                    mat_top_rot = vec_nor.rotation_difference(vec_top).to_matrix().to_4x4()
                    mat_rot = mat_top_rot * mat_rot

                    vec_norx = mat_rot * vec_1
                    vec_norx.z = 0
                    vec_nort = dir.copy()
                    vec_nort.z = 0
                    mat_norx = vec_norx.rotation_difference(vec_nort).to_matrix().to_4x4()
                    mat_rot = mat_norx * mat_rot

            bpy.ops.object.select_all(action='DESELECT')
            bpy.ops.object.select_pattern(pattern=obj_corner.name)

            if not instance:
                ret = bmesh.ops.duplicate(bm, geom=geom_)
                geom_dup = ret['geom']
                verts_dupe = [ele for ele in geom_dup
                              if isinstance(ele, bmesh.types.BMVert)]
                del ret

                bmesh.ops.rotate(
                    bm,
                    verts=verts_dupe,
                    cent=(0.0, 0.0, 0.0),
                    matrix=mat_rot)

                bmesh.ops.translate(
                    bm,
                    verts=verts_dupe,
                    vec=location)

            else:
                bpy.ops.object.mode_set(mode='OBJECT')
                bpy.context.scene.objects.active = obj_corner
                bpy.ops.object.select_all(action='DESELECT')
                bpy.ops.object.select_pattern(pattern=obj_corner.name)
                bpy.ops.object.duplicate(linked=True)

                obja = bpy.context.scene.objects.active

                loc2 = location - obja.location
                mat_loc = mathutils.Matrix.Translation(loc2)
                mat_loc2 = mathutils.Matrix.Translation(-loc2)
                mat_rot2 = obja.rotation_euler.copy()
                loc_, rot_, sca_ = obja.matrix_world.decompose()
                rot_inv = rot_.to_matrix().to_4x4().inverted()

                obja.matrix_world *= rot_inv
                mat_out = mat_loc * mat_rot * mat_loc2
                obja.matrix_world = obja.matrix_world * mat_out * rot_.to_matrix().to_4x4()
                obja.location = location

        bmesh.ops.delete(bm, geom=geom_, context=1)
        bmesh.ops.delete(bm_l, geom=geom_l, context=1)

        if not instance:
            # Corners
            me = bpy.data.meshes.new("Mesh")
            bm.to_mesh(me)

            scene = bpy.context.scene
            obj = bpy.data.objects.new("Object", me)
            scene.objects.link(obj)
            obj.location = obj_path.location

            # Linears
            me = bpy.data.meshes.new("Mesh")
            bm_l.to_mesh(me)

            scene = bpy.context.scene
            obj = bpy.data.objects.new("Object", me)
            scene.objects.link(obj)
            obj.location = obj_path.location

        bm.free()
        bm_l.free()
    return True


class PaMatsSort(bpy.types.Operator):
    bl_idname = "material.paul_sort"
    bl_label = "Mats sort"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.object.misc(type_op=15)
        return {'FINISHED'}


class PaCurveSwap2D3D(bpy.types.Operator):
    """switch selected curve type """
    bl_idname = "object.curve_swap"
    bl_label = "Curve swap 2D/3D"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.object.misc(type_op=3)
        return {'FINISHED'}


class PaCurvesSelect2D(bpy.types.Operator):
    """select all 2D curves"""
    bl_idname = "object.curves_select_2d"
    bl_label = "Curves select 2D"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.object.misc(type_op=1)
        return {'FINISHED'}


class PaObjSwitchOnOff(bpy.types.Operator):
    """resetting outliner options"""
    bl_idname = "object.switch"
    bl_label = "Outliner set"
    bl_options = {'REGISTER', 'UNDO'}

    type_op = bpy.props.IntProperty(name='type_op', default=16, options={'HIDDEN'})

    def execute(self, context):
        bpy.ops.object.misc(type_op=self.type_op)
        return {'FINISHED'}


class PaObjSelectModified(bpy.types.Operator):
    """select objects with modifiers"""
    bl_idname = "object.select_modified"
    bl_label = "Object select modified"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.object.misc(type_op=6)
        return {'FINISHED'}


class PaNJoin(bpy.types.Operator):
    """join objects autofixing negative scale """
    bl_idname = "paul.njoin"
    bl_label = "NJoin"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.active_object is not None and context.active_object.type == 'MESH'

    def execute(self, context):
        def _flip_normals():
            bpy.ops.object.editmode_toggle()
            bpy.ops.mesh.reveal()
            bpy.ops.mesh.select_all(action="SELECT")
            bpy.ops.mesh.flip_normals()
            bpy.ops.object.editmode_toggle()

        selected_objs = [obj for obj in bpy.context.selected_objects if obj.type == 'MESH']
        act_obj = bpy.context.active_object
        bpy.ops.paul.obj_filter_neg_scale()
        count_neg_objs = len(bpy.context.selected_objects)
        bpy.context.scene.objects.active = act_obj
        act_obj.select = True

        if count_neg_objs > 0:
            _flip_normals()
            bpy.ops.object.join()
            _flip_normals()
        else:
            bpy.ops.object.join()

        for obj in selected_objs:
            obj.select = True
        bpy.ops.object.join()
        return {'FINISHED'}


class PaMakeBorder(bpy.types.Operator):
    """make border from selected polygons"""
    bl_idname = "paul.make_border"
    bl_label = "Make Border"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.active_object is not None and context.active_object.type == 'MESH'

    def execute(self, context):
        config = bpy.context.window_manager.paul_manager
        Hc = 1.0  # конструктивная высота бордюра, для перекрытия возможных перепадов

        зелёнка = 0
        дорога = 1

        size = config.mborder_size
        if size < 0:
            mode = дорога
            Wgw = Hgw = -size
        else:
            mode = зелёнка
            Wgw, Hgw = -size, size

        mat_find = 'BORDER_20W' if mode else 'BORDER_10W'

        objs_ = [o.name for o in bpy.context.scene.objects]
        bpy.ops.mesh.duplicate_move(MESH_OT_duplicate={"mode": 1}, TRANSFORM_OT_translate={"value": (0, 0, Hgw - Hc)})
        bpy.ops.mesh.separate(type='SELECTED')
        bpy.ops.object.mode_set(mode='OBJECT')
        obj_ = [o.name for o in bpy.context.scene.objects if o.name not in objs_]
        obj = bpy.context.scene.objects[obj_[0]]
        bpy.context.active_object.select = False
        obj.select = True
        me = obj.data
        bpy.context.scene.objects.active = obj
        bpy.ops.object.mode_set(mode='EDIT')
        bm = bmesh.from_edit_mesh(obj.data)
        bm.faces.ensure_lookup_table()
        bpy.ops.mesh.select_all(action="SELECT")
        faces = [f for f in bm.faces]
        bpy.ops.mesh.extrude_region_move(TRANSFORM_OT_translate={"value": (0, 0, Hc)})
        bm.faces.ensure_lookup_table()
        for f in faces:
            f.select = True

        bm.free()
        bpy.ops.mesh.delete(type='FACE')
        bpy.ops.mesh.select_all(action="SELECT")
        bpy.ops.mesh.extrude_region_shrink_fatten(TRANSFORM_OT_shrink_fatten={"value": Wgw, "use_even_offset": True})
        bpy.ops.mesh.select_all(action="SELECT")

        mats = bpy.data.materials
        set_mat = [m for m in mats if m.name.find(mat_find) > 0]
        if set_mat:
            set_mat = set_mat[0]
            idx_mat = me.materials.find(set_mat.name)
            obj.active_material = set_mat
        else:
            print('Make Border: Required material not found')

        bpy.ops.object.mode_set(mode='OBJECT')

        i = len(obj.material_slots) - 1
        for slot in reversed(obj.material_slots):
            bpy.context.object.active_material_index = i
            mat = slot.material
            i -= 1
            if mat == set_mat: continue
            bpy.ops.object.material_slot_remove()

        return {'FINISHED'}


class PaPropagateObname(bpy.types.Operator):
    bl_idname = "paul.propagate_obname"
    bl_label = "Propagate Obname"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.active_object is not None and context.active_object.type == 'MESH'

    def execute(self, context):
        edit_mode_out()
        selected_objs = context.selected_objects[:]
        must_select_objs = []
        candidates_active_objs = []
        messages = []
        for act_obj in selected_objs:
            if act_obj in must_select_objs:
                continue
            bpy.ops.object.select_all(action="DESELECT")
            context.scene.objects.active = act_obj
            act_obj.select = True
            bpy.ops.paul.obname_to_meshname()
            bpy.ops.paul.select_instances()
            messages.append(context.scene['report'])
            active_obj_name = act_obj.name
            objs = bpy.context.selected_objects
            for solve_obj in objs:
                solve_obj.name = active_obj_name

            act_obj.name = active_obj_name
            must_select_objs.extend(objs)
            candidates_active_objs.append(active_obj_name)

        bpy.ops.object.select_all(action="DESELECT")
        for obj in must_select_objs:
            obj.select = True

        active_obj_name = sorted(candidates_active_objs)[0]
        context.scene.objects.active = context.scene.objects[active_obj_name]
        total_selected_objects = 0
        total_instances = 0
        total_unique = 0
        for message in messages:
            row_line = message.split()
            total_selected_objects += int(row_line[0])
            total_instances += int(row_line[2])
            total_unique += int(row_line[4])

        message = "{} selected, {} inst, {} unique".format(total_selected_objects, total_instances, total_unique)
        self.report({'INFO'}, message)
        return {'FINISHED'}


class PaSideShiftStoreDist(bpy.types.Operator):
    """Sideshift store dist"""
    bl_idname = "paul.sideshift_dist"
    bl_label = "Sideshift store dist"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.active_object is not None and context.active_object.type == 'MESH'

    def execute(self, context):
        config = bpy.context.window_manager.paul_manager
        bpy.ops.mesh.align_operator(type_op=1)
        self.report({'INFO'}, 'dist: ' + str(round(config.step_len, 4)))
        return {'FINISHED'}


class PaSideShiftActiveCursor(bpy.types.Operator):
    """Sideshift Active to cursor"""
    bl_idname = "paul.sideshift_cursor"
    bl_label = "Sideshift Active to cursor"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.active_object is not None and context.active_object.type == 'MESH'

    def execute(self, context):
        bpy.ops.mesh.offset_operator(type_op=3)
        return {'FINISHED'}


class PaSideShiftBackward(bpy.types.Operator):
    """Sideshift backward"""
    bl_idname = "paul.sideshift_backward"
    bl_label = "Sideshift backward"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.active_object is not None and context.active_object.type == 'MESH'

    def execute(self, context):
        bpy.ops.mesh.offset_operator(type_op=0, sign_op=-1)
        return {'FINISHED'}


class PaSideShiftForward(bpy.types.Operator):
    """Sideshift forward"""
    bl_idname = "paul.sideshift_forward"
    bl_label = "Sideshift forward"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.active_object is not None and context.active_object.type == 'MESH'

    def execute(self, context):
        bpy.ops.mesh.offset_operator(type_op=0, sign_op=1)
        return {'FINISHED'}


def AFASMain(ANGLE_RAD, context):
    if context.mode == 'EDIT_MESH':
        bpy.ops.object.editmode_toggle()
        bpy.ops.object.editmode_toggle()
        config = bpy.context.window_manager.paul_manager
        obj = context.active_object
        mesh = obj.data
        bm = bmesh.new()
        bm.from_mesh(mesh)
        check_lukap(bm)
        idx, mod = bm_vert_active_get(bm)
        if mod == 'E' and idx != None:
            angle = bm.edges[idx].calc_face_angle()
            if angle != None:
                config.afas_angle = angle

        bm.free()
        return True

    objs = [o for o in bpy.context.scene.objects if o.select]
    for obj in objs:
        bpy.context.scene.objects.active = obj
        mesh = obj.data

        bpy.ops.object.mode_set(mode='OBJECT')
        bpy.ops.object.mode_set(mode='EDIT')

        bpy.ops.mesh.select_all(action='SELECT')
        bpy.ops.mesh.mark_sharp(clear=True)
        bpy.ops.mesh.select_all(action='DESELECT')

        bpy.ops.object.mode_set(mode='OBJECT')
        bpy.ops.object.mode_set(mode='EDIT')

        bm = bmesh.new()
        bm.from_mesh(mesh)
        check_lukap(bm)

        ################ First part
        for edge in bm.edges:
            angle = edge.calc_face_angle(0)
            if angle >= ANGLE_RAD and angle > 0:
                edge.select_set(True)
            else:
                edge.select_set(False)

        bpy.ops.object.mode_set(mode='OBJECT')
        bm.to_mesh(mesh)

        bm.free()
        bpy.ops.object.mode_set(mode='EDIT')

        ################ Second part
        bpy.ops.mesh.mark_sharp()
        bpy.ops.object.mode_set(mode='OBJECT')
    return True


class AFASOperator(bpy.types.Operator):
    """Set sharp on object"""
    bl_idname = "object.afas"
    bl_label = "Auto Face Angle Sharp"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.active_object is not None and context.active_object.type == 'MESH'

    def execute(self, context):
        config = bpy.context.window_manager.paul_manager
        if AFASMain(config.afas_angle, context):
            return {'FINISHED'}
        else:
            return {'CANCELLED'}


class EExtrudeAlongPath(bpy.types.Operator):
    """Auto Extrude along path"""
    bl_idname = "eap.op4_id"
    bl_label = "EExtrude along path"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.active_object is not None and context.active_object.type == 'MESH'

    def EEAPMain(self, context):
        edit_mode_out()
        edit_mode_in()
        obj = context.active_object
        mesh = obj.data
        bme = bmesh.new()
        bme.from_mesh(mesh)
        check_lukap(bme)
        av = bm_vert_active_get(bme)
        if av[1] == 'V':
            v = bme.verts[av[0]]
            vi = v.index
            if v.select and v.is_valid:
                vts_idx = [v.index for v in bme.verts if v.select]
                con_vts = find_all_connected_verts(mesh, vi, not_list=[])
                vts_inv_idx = [i for i in vts_idx if i not in con_vts]
                vts_tmp = []
                cou = 0
                while (len(vts_idx) > len(con_vts) and cou < 50):
                    cou += 1
                    bpy.ops.mesh.select_linked_pick(deselect=True, delimit=set(), index=vts_inv_idx[0])
                    vts_tmp.append(vts_inv_idx[0])
                    edit_mode_out()
                    edit_mode_in()
                    vts_idx = [v.index for v in mesh.vertices if v.select]
                    vts_inv_idx = [i for i in vts_idx if i not in con_vts]

                bpy.ops.eap.op3_id()
                for vi_ in vts_tmp:
                    bpy.ops.mesh.select_linked_pick(deselect=False, delimit=set(), index=vi_)

                bpy.ops.eap.op2_id()

        bme.free()
        return {'FINISHED'}

    def execute(self, context):
        config = bpy.context.window_manager.paul_manager
        if self.EEAPMain(context):
            return {'FINISHED'}
        else:
            return {'CANCELLED'}


class DisableDubleSideOperator(bpy.types.Operator):
    """Disable show duble side all meshes"""
    bl_idname = "mesh.disable_duble_sided"
    bl_label = "DDDisableDoubleSided"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        for mesh in bpy.data.meshes:
            mesh.show_double_sided = False
        return {'FINISHED'}


class DistVerticesOperator(bpy.types.Operator):
    """Volumetric vertices selection"""
    bl_idname = "mesh.dist_verts"
    bl_label = "Dist Vertices"
    bl_options = {'REGISTER', 'UNDO'}

    type_op = bpy.props.IntProperty(name='type_op', default=0, options={'HIDDEN'})

    @classmethod
    def poll(cls, context):
        return context.active_object is not None and context.active_object.type == 'MESH'

    def execute(self, context):
        config = bpy.context.window_manager.paul_manager
        if self.type_op == 0:
            result = find_dupes_verts(context, config.dist_verts)
            if result == 0:
                self.report({'INFO'}, "nothing found")
            else:
                self.report({'INFO'}, "found " + str(result) + " vertices")
        elif self.type_op == 1:
            result = sel_radius_verts(context, config.dist_verts)
            if result == 0:
                self.report({'INFO'}, "nothing added")
            else:
                self.report({'INFO'}, "added " + str(result) + " vertices")
        else:
            result = False

        if result:
            return {'FINISHED'}
        else:
            return {'CANCELLED'}


class MatExrudeOperator(bpy.types.Operator):
    """Extude with mats"""
    bl_idname = "mesh.mat_extrude"
    bl_label = "Mat Extrude"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.active_object is not None and context.active_object.type == 'MESH'

    def execute(self, context):
        main_matExtrude(context)
        return {'FINISHED'}


class MatsSelMultiple(bpy.types.Operator):
    """select objects with multiple materials"""
    bl_idname = "paul.mats_sel_multiple"
    bl_label = "Mats select multiple"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        objs = [o for o in context.scene.objects if o.type == 'MESH']
        bpy.ops.object.select_all(action='DESELECT')
        for obj in objs:
            if len(obj.material_slots) != 1:
                obj.select = True
        return {'FINISHED'}


class MatsEqualizeOperator(bpy.types.Operator):
    bl_idname = "paul.mats_equalize"
    bl_label = "Get Mats for all"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.active_object is not None and context.active_object.type == 'MESH'

    def execute(self, context):
        getMatsAct2Pas()
        return {'FINISHED'}


class GetMatsOperator(bpy.types.Operator):
    """Get mats"""
    bl_idname = "mesh.get_mat4extrude"
    bl_label = "Get Mats for extrude"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.active_object is not None and context.active_object.type == 'MESH'

    def execute(self, context):
        getMats(context)
        return {'FINISHED'}


class SSOperator(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "mesh.simple_scale_operator"
    bl_label = "Scale operator"
    bl_options = {'REGISTER', 'UNDO'}

    type_op = bpy.props.IntProperty(name='type_op', default=0, options={'HIDDEN'})

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        if self.type_op == 1:
            getorient()
        else:
            main_ss(context)
        return {'FINISHED'}


class CompareMeshes(bpy.types.Operator):
    bl_idname = "object.compare_meshes"
    bl_label = "Compare meshes"
    bl_options = {'REGISTER', 'UNDO'}

    type_op = bpy.props.IntProperty(name='type_op', default=0, options={'HIDDEN'})

    @classmethod
    def poll(cls, context):
        return context.active_object is not None and context.active_object.type == 'MESH'

    def execute(self, context):
        config = bpy.context.window_manager.paul_manager
        if self.type_op == 0:
            if not compMeshesVerts(context, config.compmeshes_treshold):
                return {'CANCELLED'}
        elif self.type_op == 1:
            if not compMeshesToMats(context):
                return {'CANCELLED'}

        return {'FINISHED'}


class CrossPolsOperator(bpy.types.Operator):
    bl_idname = "mesh.polycross"
    bl_label = "Polycross"
    bl_options = {'REGISTER', 'UNDO'}

    type_op = bpy.props.IntProperty(name='type_op', default=0, options={'HIDDEN'})

    @classmethod
    def poll(cls, context):
        return context.active_object is not None and context.active_object.type == 'MESH'

    def execute(self, context):
        lt = bpy.context.window_manager.paul_manager
        if self.type_op == 0:
            lt.SPLIT = False
            lt.filter_edges = False
            lt.filter_verts_top = False
            lt.filter_verts_bottom = False
        elif self.type_op == 1:
            lt.SPLIT = True
            lt.filter_edges = False
            lt.filter_verts_top = False
            lt.filter_verts_bottom = False
        else:
            if lt.filter_edges or lt.filter_verts_bottom or lt.filter_verts_top:
                if lt.filter_edges:
                    lt.filter_verts_bottom = False
                    lt.filter_verts_top = False
            else:
                select_v_on_plane()
                return {'FINISHED'}

        crosspols()
        if self.type_op == 0:
            bpy.context.tool_settings.mesh_select_mode = True, True, True
        return {'FINISHED'}


class Project3DLoopOperator(bpy.types.Operator):
    """Make loop from two projections"""
    bl_idname = "mesh.projectloop"
    bl_label = "Project 3D Loop"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.active_object is not None and context.active_object.type == 'MESH'

    def execute(self, context):
        DDDLoop()
        return {'FINISHED'}


class BarcOperator(bpy.types.Operator):
    """Shapes loop to arc by sidepoints of loop anf middle active"""
    bl_idname = "mesh.barc"
    bl_label = "BARC repeat"
    bl_options = {'REGISTER', 'UNDO'}

    type_op = bpy.props.IntProperty(name='type_op', default=0, options={'HIDDEN'})

    @classmethod
    def poll(cls, context):
        return context.active_object is not None and context.active_object.type == 'MESH'

    def execute(self, context):
        if self.type_op == 0:
            barc(None)
        elif self.type_op == 1:
            barc(bpy.context.window_manager.paul_manager.barc_rad)
        elif self.type_op == 2:
            barc_cursorToCenter()
        bpy.ops.object.mode_set(mode='EDIT')
        return {'FINISHED'}


class PaBarcCreateOperator(bpy.types.Operator):
    bl_idname = "paul.barc_create"
    bl_label = "BARC - create BARC"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.active_object is not None and context.active_object.type == 'MESH'

    def execute(self, context):
        bpy.ops.mesh.barc(type_op=0)
        return {'FINISHED'}


class PaBarcSetOperator(bpy.types.Operator):
    bl_idname = "paul.barc_set"
    bl_label = "BARCS - Set radius"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.active_object is not None and context.active_object.type == 'MESH'

    def execute(self, context):
        bpy.ops.mesh.barc(type_op=1)
        return {'FINISHED'}


class PaBarcCursorOperator(bpy.types.Operator):
    bl_idname = "paul.barc_cursor"
    bl_label = "BARCC - Cursor to Center"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.active_object is not None and context.active_object.type == 'MESH'

    def execute(self, context):
        bpy.ops.mesh.barc(type_op=2)
        return {'FINISHED'}


class MiscOperator(bpy.types.Operator):
    bl_idname = "object.misc"
    bl_label = "Misc"
    bl_options = {'REGISTER', 'UNDO'}

    type_op = bpy.props.IntProperty(name='type_op', default=0, options={'HIDDEN'})
    """
    @classmethod
    def poll(cls, context):
        return context.active_object is not None"""

    def execute(self, context):
        config = bpy.context.window_manager.paul_manager
        if self.type_op == 0:
            ignore_instance()
        elif self.type_op == 1:
            select_2d_curves()
        elif self.type_op == 2:
            filter_dubles_origins(config.verts_activate)
        elif self.type_op == 3:
            swap_curve()
        elif self.type_op == 4:
            supress_materials()
        elif self.type_op == 5:
            context.scene['cheredator'] = cheredator()
        elif self.type_op == 6:
            select_modifiers_objs()
        elif self.type_op == 7:
            switch_matnodes()
        elif self.type_op == 8:
            all_mats_to_active()
        elif self.type_op == 9:
            hue_2matneme()
        elif self.type_op == 10:
            HVS_from_mathame()
        elif self.type_op == 11:
            matsUnclone()
        elif self.type_op == 12:
            matsPurgeout()
        elif self.type_op == 13:
            matchProp()
        elif self.type_op == 14:
            selected_mats_to_active()
        elif self.type_op == 15 and context.active_object.type == 'MESH':
            matsActSortSlots()
        elif self.type_op == 16:
            objSwitchOn(config.oso_vizing, config.oso_select, config.oso_render, off=False)
        elif self.type_op == 17:
            objSwitchOn(config.oso_vizing, config.oso_select, config.oso_render, off=True)
        return {'FINISHED'}


class SpreadOperator(bpy.types.Operator):
    """Distributes vertices of loop by axes"""
    bl_idname = "mesh.spread_operator"
    bl_label = "Spread operator"
    bl_options = {'REGISTER', 'UNDO'}

    def updateself(self, context):
        bpy.context.window_manager.paul_manager.shape_inf = self.influence * 5

    influence = bpy.props.IntProperty(name="Shape",
                                      description="instance -> spline -> spline 2 -> Basier_mid -> Basier -> instance",
                                      default=0,
                                      min=0,
                                      max=50,
                                      update=updateself)

    @classmethod
    def poll(cls, context):
        return context.active_object is not None and context.active_object.type == 'MESH'

    def draw(self, context):
        layout = self.layout
        row = layout.row()
        row.prop(self, 'influence')

    def execute(self, context):
        config = bpy.context.window_manager.paul_manager
        if main_spread(context, (config.spread_x, config.spread_y, config.spread_z, config.relation),
                       self.influence * 5):
            pass
            # print('spread complete')
        else:
            return {'CANCELLED'}
        return {'FINISHED'}


class AlignOperator(bpy.types.Operator):
    bl_idname = "mesh.align_operator"
    bl_label = "Align operator"
    bl_options = {'REGISTER', 'UNDO'}

    type_op = bpy.props.IntProperty(name='type_op', default=0, options={'HIDDEN'})
    dist = bpy.props.FloatProperty(name='dist', precision=4)
    dist_x = bpy.props.FloatProperty(name='X', precision=4)
    dist_y = bpy.props.FloatProperty(name='Y', precision=4)
    dist_z = bpy.props.FloatProperty(name='Z', precision=4)

    @classmethod
    def poll(cls, context):
        return context.active_object is not None and context.active_object.type == 'MESH'

    def execute(self, context):
        resfunc = False
        config = bpy.context.window_manager.paul_manager
        if self.type_op == 1:
            resfunc = store_align()
            if not resfunc:
                return {'CANCELLED'}

            config.step_len = GetStoreVecLength()
            self.dist_x = Vector(config.vec_store).x
            self.dist_y = Vector(config.vec_store).y
            self.dist_z = Vector(config.vec_store).z
            self.report({'INFO'}, \
                        'dist: ' + str(round(config.step_len, 4)))
        elif self.type_op == 0:
            resfunc = main_align()
        elif self.type_op == 2:
            scene = bpy.context.scene
            resfunc = main_align_object(scene.AxesProperty, scene.ProjectsProperty)
        elif self.type_op == 3:
            # Store Vert
            resfunc = store_align('vert')
        elif self.type_op == 4:
            # Store Coner
            resfunc = store_align('coner')
        elif self.type_op == 5:
            # 3D Match
            resfunc = match3D(False)
        elif self.type_op == 6:
            # 3d Match Flip
            resfunc = match3D(True)
        elif self.type_op == 7:
            resfunc = mirrorside()

        if not resfunc:
            return {'CANCELLED'}

        self.dist = config.step_len
        return {'FINISHED'}


class RailerOperator(bpy.types.Operator):
    bl_idname = "object.railer_operator"
    bl_label = "Railer operator"
    bl_options = {'REGISTER', 'UNDO'}

    type_op = bpy.props.IntProperty(name='type_op', default=0, options={'HIDDEN'})
    z_up = BoolProperty(name='Z up')
    follow_path = BoolProperty(name='Follow path')
    flat_dist = BoolProperty(name='Flat dist')
    instance = BoolProperty(name='Instance')
    dist = FloatProperty(name='dist')
    seed = IntProperty(name='seed', max=1, min=0)

    def draw(self, context):
        layout = self.layout
        col_top = layout.box().column(align=True)
        row = col_top.row(align=True)
        row.prop(self, 'dist')
        row = col_top.row(align=True)
        row.prop(self, 'z_up')
        if self.z_up:
            row = col_top.row(align=True)
            row.prop(self, 'flat_dist')

        row = col_top.row(align=True)
        row.prop(self, 'follow_path')
        row = col_top.row(align=True)
        row.prop(self, 'instance')
        if self.follow_path:
            row = col_top.row(align=True)
            row.prop(self, 'seed')

    def __init__(self):
        config = bpy.context.window_manager.paul_manager
        self.dist = config.railer_dist

    def execute(self, context):
        config = bpy.context.window_manager.paul_manager
        scn = context.scene
        objects = scn.objects
        config.railer_dist = self.dist
        resfunc = False

        if self.type_op == 1:
            scn.path_obj = getChoseSelection(objects)

        elif self.type_op == 2:
            scn.corner_obj = getChoseSelection(objects)

        elif self.type_op == 3:
            scn.linear_obj = getChoseSelection(objects)

        elif self.type_op == 4:
            resfunc = main_railer(dist=self.dist, z_up=self.z_up, \
                                  follow_path=self.follow_path, flat=self.flat_dist, \
                                  instance=self.instance, seed=self.seed)
            if not resfunc:
                return {'CANCELLED'}

        return {'FINISHED'}


class ChunksOperator(bpy.types.Operator):
    """select mesh part"""
    bl_idname = "mesh.sel_chunks"
    bl_label = "Select Chunks"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.active_object is not None and context.active_object.type == 'MESH'

    def execute(self, context):
        config = bpy.context.window_manager.paul_manager
        m = config.chunks_clamp
        s = config.chunks_setting
        Select_chunks(maloe=m, setting=s)
        return {'FINISHED'}


class CornerOperator(bpy.types.Operator):
    bl_idname = "mesh.corner"
    bl_label = "Corner"
    bl_options = {'REGISTER', 'UNDO'}
    type_op = bpy.props.IntProperty(name='type_op', default=0, options={'HIDDEN'})

    @classmethod
    def poll(cls, context):
        return context.active_object is not None and context.active_object.type == 'MESH'

    def execute(self, context):
        config = bpy.context.window_manager.paul_manager
        active = config.corner_active_edge
        to_active = config.to_corner_active_edge
        mode_orig = bpy.context.object.mode
        bpy.ops.object.mode_set(mode='OBJECT')
        if self.type_op == 0:
            'corner_corner', corner_corner(active, to_active)
        elif self.type_op == 1:
            'corner_extend', corner_extend(active, to_active)
        bpy.ops.object.mode_set(mode=mode_orig)
        return {'FINISHED'}


class OffsetOperator(bpy.types.Operator):
    bl_idname = "mesh.offset_operator"
    bl_label = "Offset operator"
    bl_options = {'REGISTER', 'UNDO'}

    type_op = bpy.props.IntProperty(name='type_op', default=0, options={'HIDDEN'})
    sign_op = bpy.props.IntProperty(name='sign_op', default=1, options={'HIDDEN'})

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        config = bpy.context.window_manager.paul_manager
        if self.type_op == 0:  # move left / right
            ao = bpy.context.active_object.name
            l_obj = []
            for obj_a in bpy.context.selected_objects:
                l_obj.append(obj_a.name)
            if config.shift_copy:
                if bpy.context.mode == 'OBJECT':
                    for obj_a in bpy.context.selected_objects:
                        bpy.context.scene.objects.active = obj_a
                        bpy.ops.object.select_all(action='DESELECT')
                        bpy.ops.object.select_pattern(pattern=obj_a.name)
                        bpy.ops.object.duplicate(linked=config.instance)

                    for obj_a_name in l_obj:
                        bpy.context.scene.objects[obj_a_name].select = True
                    bpy.context.scene.objects.active = bpy.data.objects[ao]

                elif bpy.context.mode == 'EDIT_MESH':
                    bpy.ops.mesh.duplicate()

            x = config.step_len * self.sign_op
            if bpy.context.mode == 'OBJECT':
                for obj_a_ in l_obj:
                    obj_a = bpy.context.scene.objects[obj_a_]
                    bpy.context.scene.objects.active = obj_a
                    bpy.ops.object.select_all(action='DESELECT')
                    bpy.ops.object.select_pattern(pattern=obj_a.name)
                    main_offset(x)

                for obj_a_name in l_obj:
                    bpy.context.scene.objects[obj_a_name].select = True
                bpy.context.scene.objects.active = bpy.data.objects[ao]
            else:
                main_offset(x)

        elif self.type_op == 1:  # get length
            config.step_len = GetStoreVecLength()

        elif self.type_op == 2:  # copy
            # copy_offset()
            pass

        elif self.type_op == 3:
            cam_lam = bpy.context.object.type in ['CAMERA', 'LAMP', 'EMPTY']
            if config.shift_copy:
                if bpy.context.mode == 'OBJECT':
                    l_obj = []
                    ao = bpy.context.active_object.name
                    for obj_a in bpy.context.selected_objects:
                        l_obj.append(obj_a.name)
                    for obj_a in bpy.context.selected_objects:
                        bpy.context.scene.objects.active = obj_a
                        bpy.ops.object.duplicate(linked=config.instance)
                        bpy.ops.object.select_all(action='DESELECT')
                        bpy.ops.object.select_pattern(pattern=obj_a.name)
                    for obj_a_name in l_obj:
                        bpy.context.scene.objects[obj_a_name].select = True
                    bpy.context.scene.objects.active = bpy.data.objects[ao]

                elif bpy.context.mode == 'EDIT_MESH':
                    bpy.ops.mesh.duplicate()

            if cam_lam:
                vec = GetDistObjToCursor(bpy.context.active_object)
            else:
                vec = GetDistToCursor()
            config.object_name_store = bpy.context.active_object.name
            config.vec_store = vec
            config.step_len = vec.length
            x = config.step_len
            if bpy.context.mode == 'OBJECT':
                ao = bpy.context.active_object.name
                for obj_a in bpy.context.selected_objects:
                    bpy.context.scene.objects.active = obj_a
                    main_offset(x)
                bpy.context.scene.objects.active = bpy.data.objects[ao]
            else:
                main_offset(x)

            config.step_len = GetStoreVecLength()

        elif self.type_op == 4:
            act_obj = bpy.context.active_object
            bpy.ops.object.duplicate(linked=config.instance)
            bpy.ops.object.select_all(action='DESELECT')
            bpy.ops.object.select_pattern(pattern=act_obj.name)
            bpy.context.scene.objects.active = bpy.data.objects[act_obj.name]

        else:
            pass

        self.type_op = 0
        self.sign_op = 1
        return {'FINISHED'}


class RotorOperator(bpy.types.Operator):
    bl_idname = "mesh.rotor_operator"
    bl_label = "Rotor operator"
    bl_options = {'REGISTER', 'UNDO'}

    type_op = bpy.props.IntProperty(name='type_op', default=0, options={'HIDDEN'})
    sign_op = bpy.props.IntProperty(name='sign_op', default=1, options={'HIDDEN'})

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        config = bpy.context.window_manager.paul_manager
        resfunc = False
        if self.type_op == 0:  # move left / right
            ao = bpy.context.active_object.name
            l_obj = []
            for obj_a in bpy.context.selected_objects:
                l_obj.append(obj_a.name)
            if config.rotor3d_copy:
                if bpy.context.mode == 'OBJECT':
                    for obj_a in bpy.context.selected_objects:
                        bpy.context.scene.objects.active = obj_a
                        bpy.ops.object.select_all(action='DESELECT')
                        bpy.ops.object.select_pattern(pattern=obj_a.name)
                        bpy.ops.object.duplicate(linked=config.rotor3d_instance)

                    for obj_a_name in l_obj:
                        bpy.context.scene.objects[obj_a_name].select = True
                    bpy.context.scene.objects.active = bpy.data.objects[ao]

            x = config.step_angle * self.sign_op
            if bpy.context.mode == 'OBJECT':
                for obj_a_ in l_obj:
                    obj_a = bpy.context.scene.objects[obj_a_]
                    bpy.context.scene.objects.active = obj_a
                    bpy.ops.object.select_all(action='DESELECT')
                    bpy.ops.object.select_pattern(pattern=obj_a.name)
                    resfunc = main_rotor(x)

                for obj_a_name in l_obj:
                    bpy.context.scene.objects[obj_a_name].select = True
                bpy.context.scene.objects.active = bpy.data.objects[ao]
            else:
                resfunc = main_rotor(x)

        elif self.type_op == 1:  # get angle
            if (GetStoreVecAngle()):
                def getLen(e_i):
                    ao = bpy.context.active_object
                    me = ao.data
                    ed = me.edges[e_i]
                    length = round((me.vertices[ed.vertices[0]].co - \
                                    me.vertices[ed.vertices[1]].co).length, 3)
                    return length

                def getVecEdge(e_i):
                    ao = bpy.context.active_object
                    me = ao.data
                    ed = me.edges[e_i]
                    return (me.vertices[ed.vertices[1]].co - \
                            me.vertices[ed.vertices[0]].co)

                if (config.active_edge1_store > 0 and config.active_edge2_store > 0):
                    edgel = []
                    edgel.append(getLen(config.active_edge1_store))
                    edgel.append(getLen(config.active_edge2_store))
                    if (edgel[1] < edgel[0]):
                        edgel.reverse()

                    ko1 = round(edgel[0] / edgel[1], 3)
                    ko2 = round(edgel[1] / edgel[0], 3)

                    vec_ed1 = getVecEdge(config.active_edge1_store)
                    vec_ed2 = getVecEdge(config.active_edge2_store)

                    ang = round(vec_ed1.angle(vec_ed2) * 180 / pi, 3)
                    '''
                    self.report({'INFO'}, \
                        str(edgel[0])+'/'+str(edgel[1])+'='+str(ko1)+'/'+str(ko2))'''
                    self.report({'INFO'}, str(str(ko1) + '/' + str(ko2) + ' ang=' + str(ang)))
                    resfunc = True
                else:
                    resfunc = False
            else:
                resfunc = False

        # elif self.type_op == 2:  # copy
        # resfunc = copy_offset()

        elif self.type_op == 3:
            if config.shift_copy:
                if bpy.context.mode == 'OBJECT':
                    l_obj = []
                    ao = bpy.context.active_object.name
                    for obj_a in bpy.context.selected_objects:
                        l_obj.append(obj_a.name)
                    for obj_a in bpy.context.selected_objects:
                        bpy.context.scene.objects.active = obj_a
                        bpy.ops.object.duplicate(linked=config.instance)
                        bpy.ops.object.select_all(action='DESELECT')
                        bpy.ops.object.select_pattern(pattern=obj_a.name)
                    for obj_a_name in l_obj:
                        bpy.context.scene.objects[obj_a_name].select = True
                    bpy.context.scene.objects.active = bpy.data.objects[ao]

                elif bpy.context.mode == 'EDIT_MESH':
                    bpy.ops.mesh.duplicate()

            vec = GetDistToCursor()
            config.object_name_store = bpy.context.active_object.name
            config.vec_store = vec
            config.step_len = vec.length
            x = config.step_len
            if bpy.context.mode == 'OBJECT':
                ao = bpy.context.active_object.name
                for obj_a in bpy.context.selected_objects:
                    bpy.context.scene.objects.active = obj_a
                    resfunc = main_offset(x)
                bpy.context.scene.objects.active = bpy.data.objects[ao]
            else:
                resfunc = main_offset(x)

            config.step_len = GetStoreVecLength()

        elif self.type_op == 4:
            act_obj = bpy.context.active_object
            bpy.ops.object.duplicate(linked=config.instance)
            bpy.ops.object.select_all(action='DESELECT')
            bpy.ops.object.select_pattern(pattern=act_obj.name)
            bpy.context.scene.objects.active = bpy.data.objects[act_obj.name]
            resfunc = True

        elif self.type_op == 5:
            resfunc = scaler_get(self.sign_op)

        else:
            pass

        if not resfunc:
            return {'CANCELLED'}

        self.type_op = 0
        self.sign_op = 1
        return {'FINISHED'}


class SelOperator(bpy.types.Operator):
    bl_idname = "mesh.setedgslen"
    bl_label = "Set Edges Length"
    bl_options = {'REGISTER', 'UNDO'}

    type_op = bpy.props.IntProperty(name='type_op', default=0, options={'HIDDEN'})

    @classmethod
    def poll(cls, context):
        return context.active_object is not None and \
               context.active_object.type == 'MESH'

    def execute(self, context):
        config = bpy.context.window_manager.paul_manager
        if self.type_op == 0:
            selFromMid(config.active_length_ratio)

        elif self.type_op == 1:
            selToCursor(config.active_length_ratio)

        elif self.type_op == 2:
            selKey(config.active_length_ratio)

        elif self.type_op == 3:
            selFromCursor(config.active_length_ratio)

        return {'FINISHED'}


class PaGroupSelectLinked(bpy.types.Operator):
    bl_idname = "paul.gsl"
    bl_label = "GSL Group select linked"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        groups_list = [o.dupli_group for o in bpy.context.selected_objects]
        groups = [i for i in set(groups_list) if i != None]

        if groups:
            bpy.ops.object.select_all(action='DESELECT')
            for group in groups:
                for obj in group.objects:
                    obj.select = True
        return {'FINISHED'}


class PaLoopResolve(bpy.types.Operator):
    """Resolve loop density by Besier in vertex mode or split edges in edges mode"""
    bl_idname = "paul.loop_resolve"
    bl_label = "Loop Resolve"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        config = bpy.context.window_manager.paul_manager
        if config.loopresolve_relative:
            loopResolve(STEP=config.loopresolve_step, dist=None)
        else:
            loopResolve(STEP=config.loopresolve_step, dist=config.loopresolve_dist)

        return {'FINISHED'}


class PaLoopReduce(bpy.types.Operator):
    """Reduce selected loop ring"""
    bl_idname = "paul.loop_reduce"
    bl_label = "Loop Reduce"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        config = bpy.context.window_manager.paul_manager
        loopReduce(config.loopreduce_step)
        return {'FINISHED'}


class PaMatsUnclone(bpy.types.Operator):
    bl_idname = "paul.mats_unclone"
    bl_label = "Mats Unclone"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        # config = bpy.context.window_manager.paul_manager
        matsUnclone()
        return {'FINISHED'}


class PaMatsPurgeout(bpy.types.Operator):
    bl_idname = "paul.mats_purgeout"
    bl_label = "Mats Purgeout"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        # config = bpy.context.window_manager.paul_manager
        matsPurgeout()
        return {'FINISHED'}


class PaObnameMats(bpy.types.Operator):
    bl_idname = "paul.obname_mat"
    bl_label = "Obname materials"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        # config = bpy.context.window_manager.paul_manager
        objs = [o for o in bpy.context.scene.objects if o.select]
        for obj in objs:
            number_mats = len(obj.material_slots)
            if number_mats == 1:
                mat_name = obj.material_slots[0].material.name
                new_name = obj.name + '__' + mat_name
                obj.name = new_name
                obj.data.name = new_name
                obj.select = False
        return {'FINISHED'}


class PaStairsMaker(bpy.types.Operator):
    """build stair from polystripe"""
    bl_idname = "paul.stairs_maker"
    bl_label = "Stairs Maker"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        StairsMaker(self)
        return {'FINISHED'}


class PsSelSameVerts(bpy.types.Operator):
    r"""Выбирает все объекты с таким же количеством вершин, как у выделенных"""
    bl_idname = "paul.sel_same_verts"
    bl_label = "Select same vertices"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        # config = bpy.context.window_manager.paul_manager
        objects = context.scene.objects
        vertsObjs = [len(o.data.vertices) for o in objects \
                     if o.select and o.type == 'MESH']
        selObjs = [o for o in objects \
                   if o.type == 'MESH' and len(o.data.vertices) in vertsObjs]
        bpy.ops.object.select_all(action='DESELECT')
        for o in selObjs:
            o.select = True

        return {'FINISHED'}


class PaSetAutoSmooth(bpy.types.Operator):
    """set Autosmooth angle 70 on selection"""
    bl_idname = "paul.set_autosmooth"
    bl_label = "Set Autosmooth"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        # config = bpy.context.window_manager.paul_manager
        if context.mode == 'EDIT_MESH':
            bpy.ops.object.mode_set(mode='OBJECT')
        bpy.ops.object.shade_smooth()
        for ob in bpy.context.selected_objects:
            if ob.type == 'MESH':
                ob.data.use_auto_smooth = True
                ob.data.auto_smooth_angle = 1.22173  # 70
                # ob.data.auto_smooth_angle = 0.785398 #45
                bpy.context.scene.objects.active = ob
                bpy.ops.mesh.customdata_custom_splitnormals_clear()

        return {'FINISHED'}


class PaInstancesMeshnameReplacePP(bpy.types.Operator):
    bl_idname = "paul.instances_meshname_replace"
    bl_label = "Instances select unique"
    bl_options = {'REGISTER', 'UNDO'}

    ch_onlypp = BoolProperty(name='Select only ++')
    bl_show = False
    selectors = []

    def execute(self, context):
        def copyObjectMesh(obj_source, obj_dist):
            bpy.ops.object.select_all(action='DESELECT')
            obj_dist.select = True
            context.scene.objects.active = obj_dist
            bpy.ops.object.select_linked(type='OBDATA')
            sel_add = [o.name for o in context.scene.objects if o.select \
                       and o.name not in self.selectors]
            if len(sel_add) > 1:
                self.selectors.extend(sel_add)
                self.selectors.append(obj_source.name)
            context.scene.objects.active = obj_source
            bpy.ops.object.make_links_data(type='OBDATA')
            obj_source.select = True

        config = bpy.context.window_manager.paul_manager
        if config.inst_repl_use_translation:
            objs_plan = []
            objs_model = []
            for obj in bpy.context.scene.objects:
                if obj.type != 'MESH' or (config.inst_repl_select and not obj.select):
                    continue

                if config.inst_repl_from in obj.name:
                    objs_plan.append(obj)
                if config.inst_repl_to in obj.name:
                    objs_model.append(obj)

            if not objs_plan or not objs_model:
                return {'FINISHED'}

            edit_mode_out()
            obj_for_select = []
            for obj_plan in objs_plan:
                bpy.ops.object.select_all(action='DESELECT')

                name = obj_plan.name[:obj_plan.name.find(config.inst_repl_from)]
                for obj_model in objs_model:
                    if name == obj_model.name[:obj_model.name.find(config.inst_repl_to)]:
                        obj_model.select = True
                        obj_plan.select = True
                        obj_for_select.append(obj_plan)
                        bpy.context.scene.objects.active = obj_model
                        bpy.ops.object.make_links_data(type='OBDATA')
                        break

            bpy.ops.object.select_all(action='DESELECT')
            for obj in obj_for_select:
                obj.select = True
            return {'FINISHED'}

        self.selectors = []
        objs = [o for o in context.scene.objects if o.select]
        if len(objs) == 2:
            act_obj = context.scene.objects.active
            if objs.index(act_obj):
                objs.reverse()
            pass_obj = objs[-1]
            copyObjectMesh(act_obj, pass_obj)
            self.bl_show = False

        elif len(objs) != 2:
            objs_pp_names = [o.name[:-2] for o in objs if o.name[-2:] == '++']
            objects = context.scene.objects
            blacklist = []
            for pass_obj_name in objs_pp_names:
                if pass_obj_name in objects:
                    pass_obj = objects[pass_obj_name]
                    act_name = pass_obj_name + '++'
                    act_obj = context.scene.objects[act_name]
                    copyObjectMesh(act_obj, pass_obj)
                else:
                    blacklist.append(pass_obj_name + '++')

            if self.ch_onlypp:
                bpy.ops.object.select_all(action='DESELECT')
                for objname in objs_pp_names:
                    if objname + '++' in blacklist: continue
                    tmp_name = objname + '++'
                    context.scene.objects[tmp_name].select = True
            else:
                bpy.ops.object.select_all(action='DESELECT')
                for objname in self.selectors:
                    if objname in blacklist: continue
                    obj = context.scene.objects[objname]
                    obj.select = True
            self.bl_show = True
        return {'FINISHED'}

    def draw(self, context):
        if self.bl_show:
            layout = self.layout
            col = layout.column()
            col.prop(self, 'ch_onlypp')


class PaInstancesUnique(bpy.types.Operator):
    bl_idname = "paul.instances_sel_unique"
    bl_label = "Instances select unique"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.active_object is not None and \
               context.active_object.type == 'MESH'

    def execute(self, context):
        # config = bpy.context.window_manager.paul_manager
        objs = bpy.context.selected_objects

        instance_group = {}
        for obj in objs:
            if obj.type != "MESH":
                continue

            o_name = obj.name
            m_name = obj.data.name
            if m_name not in instance_group:
                instance_group[m_name] = [o_name]
            else:
                instance_group[m_name].append(o_name)

        bpy.ops.object.select_all(action="DESELECT")
        for key, instances in instance_group.items():
            if len(instances) > 1:
                bpy.data.objects[instances[0]].select = True

        return {'FINISHED'}


class PaInstanceResizer(bpy.types.Operator):
    """Сбрасывет выкрученный масштаб всем инстансам, принимая как-нибудь из расставленных за scale=1"""
    bl_idname = "paul.instance_resizer"
    bl_label = "Instances resizer"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        names = []
        instances_objs = []
        sel_objs = context.selected_objects
        one_obj = []
        independent_objs = []

        bpy.ops.object.select_all(action='DESELECT')

        for i in sel_objs:
            if i.name in names:
                continue
            i.select = True
            context.scene.objects.active = i
            bpy.ops.object.select_linked(type='OBDATA')
            if len(context.selected_objects) > 1:
                sel_inst_objs = context.selected_objects
                instances_objs.append(sel_inst_objs)
                for obj in sel_inst_objs:
                    names.append(obj.name)
            else:
                independent_objs.append(i)
            bpy.ops.object.select_all(action='DESELECT')

        for ind_obj in independent_objs:
            ind_obj.select = True
        if independent_objs:
            bpy.ops.object.transform_apply(scale=True)
            bpy.ops.object.select_all(action='DESELECT')

        for ins_objs in instances_objs:
            dim = []
            o_scale = []
            for obj in ins_objs:
                obj.select = True
                dim.append(obj.dimensions[:])
                o_scale.append([1 if x > 0 else -1 for x in obj.scale[:]])

            context.scene.objects.active = None
            for obj in context.selected_objects:
                if all(map(lambda x: x > 0, obj.scale)):
                    context.scene.objects.active = obj
                    break
            else:
                context.scene.objects.active = context.selected_objects[0]

            act_scale = context.scene.objects.active.scale[:]
            scale = [1 if x > 0 else -1 for x in act_scale]
            bpy.ops.object.make_single_user(object=True, obdata=True)
            bpy.ops.object.transform_apply(scale=True)
            bpy.ops.object.mode_set(mode='EDIT')
            bpy.ops.mesh.select_all(action='SELECT')
            bpy.ops.mesh.normals_make_consistent(inside=False)
            bpy.ops.object.mode_set(mode='OBJECT')
            bpy.ops.object.make_links_data(type='OBDATA')

            for j, o in enumerate(ins_objs):
                o.dimensions = dim[j]
                o.scale = [x * ka * ko for x, ka, ko in zip(o.scale, scale, o_scale[j])]

            one_obj.append(context.active_object)
            bpy.ops.object.select_all(action='DESELECT')

        for obj in one_obj:
            obj.select = True

        return {'FINISHED'}


class PaObjNegScale(bpy.types.Operator):
    """filter objects with mirror scaling"""
    bl_idname = "paul.obj_filter_neg_scale"
    bl_label = "Obj filter negative scale"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.active_object is not None and \
               context.active_object.type == 'MESH'

    def execute(self, context):
        # config = bpy.context.window_manager.paul_manager
        objs = bpy.context.selected_objects
        sel_objs = []
        for obj in objs:
            if obj.type != "MESH":
                continue

            mulVecScales = obj.scale.x * obj.scale.y * obj.scale.z
            mulVecDeltaScales = obj.delta_scale.x * obj.delta_scale.y * obj.delta_scale.z
            mulVecScales *= mulVecDeltaScales
            if mulVecScales < 0:
                sel_objs.append(obj)

        bpy.ops.object.select_all(action="DESELECT")
        for obj in sel_objs:
            obj.select = True

        return {'FINISHED'}


class PaInstancesRecount(bpy.types.Operator):
    """text report of vertices/instances of selected objects"""
    bl_idname = "paul.instances_recount"
    bl_label = "Instances Recount"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        def getLenSymbOfDigit(dig):
            return 'ABCDEFGHIJKLMNOP'[len(str(int(dig))) - 1]

        def getMulDims(obj_name):
            obj = bpy.data.objects[obj_name]
            return reduce(mul, [max(d, 0.1) for d in obj.dimensions])

        config = bpy.context.window_manager.paul_manager
        # from operator import itemgetter

        objs = bpy.context.selected_objects

        instance_group = {}
        for obj in objs:
            if obj.type != "MESH":
                continue

            o_name = obj.name
            m_name = obj.data.name
            if m_name not in instance_group:
                instance_group[m_name] = [o_name]
            else:
                instance_group[m_name].append(o_name)

        ovr = config.ovr_options
        mess_list = []
        dic_el = {}
        for key, instances in instance_group.items():
            number = len(instances)
            verts_count = len(bpy.data.meshes[key].vertices)
            verts_total = number * verts_count
            vertscount_symb = getLenSymbOfDigit(verts_count)
            udel_wes = round(verts_count / (getMulDims(instances[0])), 1)
            verts = bpy.data.meshes[key].vertices
            edges = bpy.data.meshes[key].edges
            edges_count = len(edges)
            arr_verts_edges = [(e.index, (verts[e.vertices[0]].co - verts[e.vertices[1]].co).length) \
                               for e in edges]
            sum_length_edge = sum([e[1] for e in arr_verts_edges])
            porog_10 = sum_length_edge / edges_count * 0.1
            edge_10 = [e[0] for e in arr_verts_edges if e[1] < porog_10]
            length_edge_10 = len(edge_10)

            message_line = "%d = %d x %d = %s%.1f - %d = %s = %s" % \
                           (verts_total, number, verts_count, vertscount_symb, udel_wes, length_edge_10, \
                            key, instances[0])
            mess_list.append((verts_total, number, verts_count, udel_wes, \
                              length_edge_10, instances[0], message_line))

            dic_el[instances[0]] = edge_10

        idx = 'ABCED'.find(ovr)
        result = sorted(mess_list, key=itemgetter(idx), reverse=True)

        bpy.ops.object.select_all(action="DESELECT")

        txt_out_name = "Vertices.txt"
        texts = bpy.data.texts
        if txt_out_name not in texts:
            texts.new(txt_out_name)
        text = texts[txt_out_name]
        text.clear()
        # text.write("Statistical information at the vertices of the object\n")
        for i, message in enumerate(result):
            text.write(message[-1] + '\n')
            if i < config.ovr_count:
                obj = bpy.data.objects[message[-2]]
                obj.select = True
                if obj.name in dic_el:
                    context.scene.objects.active = obj
                    bpy.ops.object.mode_set(mode='EDIT')
                    bpy.ops.mesh.select_mode(type='EDGE')
                    bpy.ops.mesh.select_all(action='DESELECT')
                    bpy.ops.object.mode_set(mode='OBJECT')
                    # print(obj.name, dic_el[obj.name])
                    for e in dic_el[obj.name]:
                        obj.data.edges[e].select = True

        return {'FINISHED'}


class PaInstancesRename(bpy.types.Operator):
    """Renames selected objects meshname from active with insctances recount"""
    bl_idname = "paul.instances_rename"
    bl_label = "Instances Rename"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.active_object is not None and \
               context.active_object.type == 'MESH'

    def execute(self, context):
        # config = bpy.context.window_manager.paul_manager
        # from operator import itemgetter

        class Counter():
            def __init__(self):
                self.count = 0

            def __call__(self):
                self.count += 1
                post_phix = "_%(number)03d" % {"number": self.count}
                return post_phix

            def reset(self):
                self.count = 0

        objs = bpy.context.selected_objects
        act_obj = bpy.context.active_object
        cou = Counter()
        act_key = act_obj.name + cou()
        act_obj.data.name = act_key
        instance_group = {}
        for obj in objs:
            if obj.type != "MESH":
                continue

            o_name = obj.name
            m_name = obj.data.name
            if m_name not in instance_group:
                instance_group[m_name] = [o_name]
            else:
                instance_group[m_name].append(o_name)

        for key, instances in instance_group.items():
            if key == act_key: continue
            name = act_obj.name + cou()
            bpy.data.meshes[key].name = name

        for key, instances in instance_group.items():
            if key == act_key:
                for nameobj in instances:
                    name = bpy.data.objects[nameobj].data.name
                    bpy.data.objects[nameobj].name = name
                continue

        for ob in bpy.context.selected_objects:
            if ob.type == 'MESH':
                ob.name = ob.data.name

        return {'FINISHED'}


class PaMatsDatafix(bpy.types.Operator):
    """remove copies of material slots on objects and turning slot from object to data"""
    bl_idname = "paul.mats_datafix"
    bl_label = "Mats Datafix"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.active_object is not None and \
               context.active_object.type == 'MESH'

    def execute(self, context):
        # config = bpy.context.window_manager.paul_manager
        matsDatafix()

        return {'FINISHED'}


class PaHeavyNgons(bpy.types.Operator):
    r"""Поиск самых тяжелых N-полигонов"""
    bl_idname = "paul.heavy_ngons"
    bl_label = "Heavy NGons"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.active_object is not None and \
               context.active_object.type == 'MESH'

    def execute(self, context):
        # from operator import itemgetter
        # config = bpy.context.window_manager.paul_manager
        NUMBER_SELECT = 5

        obj = bpy.context.active_object

        bpy.ops.object.mode_set(mode='EDIT')
        bpy.ops.mesh.select_all(action='DESELECT')
        bpy.ops.mesh.select_mode(type='FACE')

        mesh = obj.data
        ltFaces = [(len(face.vertices), face.index) for face in mesh.polygons]
        ltFaces_sort = sorted(ltFaces, key=itemgetter(0), reverse=True)

        bpy.ops.object.mode_set(mode='OBJECT')
        for idx, tFace in enumerate(ltFaces_sort[:NUMBER_SELECT]):
            mesh.polygons[tFace[1]].select = True

        bpy.ops.object.mode_set(mode='EDIT')

        return {'FINISHED'}


class PaCleanGlass(bpy.types.Operator):
    r"""Расчитска стёкол. Упрощение выделенного до квада"""
    bl_idname = "paul.clean_glass"
    bl_label = "Clean Glass"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.active_object is not None and \
               context.active_object.type == 'MESH'

    def execute(self, context):
        # config = bpy.context.window_manager.paul_manager
        bpy.ops.object.mode_set(mode='OBJECT')
        bpy.ops.object.mode_set(mode='EDIT')

        obj = bpy.context.active_object
        mesh = obj.data

        lPolygns = [p for p in mesh.polygons if p.select]
        p_normal = lPolygns[0].normal.copy()
        p_axe = (mesh.vertices[lPolygns[0].edge_keys[0][0]].co - mesh.vertices[lPolygns[0].edge_keys[0][1]].co)
        vec = Vector((0, 0, 1))
        q_rot1 = vec.rotation_difference(p_normal).to_matrix().to_4x4()
        vec2 = q_rot1 * Vector((0, 1, 0))
        q_rot2 = vec2.rotation_difference(p_axe).to_matrix().to_4x4()
        # q_rot = q_rot1*q_rot2
        q_rot_inv = q_rot1.inverted() * q_rot2.inverted()

        x_series = [v.co.x for v in mesh.vertices if v.select]
        y_series = [v.co.y for v in mesh.vertices if v.select]
        z_series = [v.co.z for v in mesh.vertices if v.select]

        lVerts = [q_rot_inv * v.co.copy() for v in mesh.vertices if v.select]
        iCount_verts = len(lVerts)
        z_min = lVerts[0].z
        xs = [v.x for v in lVerts]
        ys = [v.y for v in lVerts]

        x_min = min(xs)
        x_max = max(xs)
        y_min = min(ys)
        y_max = max(ys)

        vEx1 = Vector((x_min, y_min, z_min)) * q_rot_inv
        vEx2 = Vector((x_min, y_max, z_min)) * q_rot_inv
        vEx3 = Vector((x_max, y_max, z_min)) * q_rot_inv
        vEx4 = Vector((x_max, y_min, z_min)) * q_rot_inv

        bpy.ops.mesh.delete(type='VERT')

        bpy.ops.mesh.primitive_plane_add()
        bpy.ops.object.editmode_toggle()
        bpy.ops.object.editmode_toggle()

        lIndexVertsPlane = [v.index for v in mesh.vertices if v.select]
        bpy.ops.object.editmode_toggle()
        mesh.vertices[lIndexVertsPlane[0]].co = vEx1
        mesh.vertices[lIndexVertsPlane[1]].co = vEx2
        mesh.vertices[lIndexVertsPlane[2]].co = vEx4
        mesh.vertices[lIndexVertsPlane[3]].co = vEx3
        bpy.ops.object.editmode_toggle()

        return {'FINISHED'}


class PaVolumeSelect(bpy.types.Operator):
    """select objects/verts in volume of given object"""
    bl_idname = "paul.valume_select"
    bl_label = "Valume select"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.active_object is not None and \
               context.active_object.type == 'MESH'

    def execute(self, context):
        def is_inside(p, obj):
            # max_dist = 1.84467e+19
            is_true, point, normal, face = obj.closest_point_on_mesh(p)
            p2 = point - p
            v = p2.dot(normal)
            return not (v < 0.0)

        config = context.window_manager.paul_manager

        edit_mode_out()
        act_obj = context.active_object
        sel_objs = context.selected_objects[:]

        if config.valsel_objectmode:
            bpy.ops.object.select_all(action='DESELECT')
            for obj in sel_objs:
                obj.select = is_inside(obj.location, act_obj)
            act_obj.select = True
        else:
            for obj in sel_objs:
                if obj == act_obj or obj.type != 'MESH':
                    continue

                context.scene.objects.active = obj
                mesh = obj.data
                edit_mode_in()
                bpy.ops.mesh.select_all(action="DESELECT")
                bm = bmesh.from_edit_mesh(mesh)
                flag = False
                for v in bm.verts:
                    p = obj.matrix_world * v.co
                    v.select = is_inside(p, act_obj)
                    if v.select:
                        flag = True
                edit_mode_out()
                obj.select = flag

            context.scene.objects.active = act_obj
        return {'FINISHED'}


class PaVertsProjectOnEdge(bpy.types.Operator):
    """split edge by perpendicular projection of other edges"""
    bl_idname = "paul.verts_project_on_edge"
    bl_label = "Vverts project"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.active_object is not None and \
               context.active_object.type == 'MESH' and \
               context.mode == 'EDIT_MESH'

    def execute(self, context):
        config = bpy.context.window_manager.paul_manager

        edit_mode_out()
        edit_mode_in()

        def bm_edge_first_get(bm):
            if not config.vproj_active:
                for elem in bm.select_history:
                    if isinstance(elem, bmesh.types.BMEdge):
                        return elem.index
                return None
            else:
                for elem in reversed(bm.select_history):
                    if isinstance(elem, bmesh.types.BMEdge):
                        return elem.index
                return None

        obj = bpy.context.active_object
        mesh = obj.data
        bm = bmesh.from_edit_mesh(mesh)
        check_lukap(bm)

        act_edge_idx = bm_edge_first_get(bm)
        if act_edge_idx == None:
            print_error2('Not found first edge', 'PaVertsProjectOnEdge 01')
            return {'CANCELED'}

        pas_edges = [e for e in bm.edges if e.select and e.index != act_edge_idx]
        act_edge = bm.edges[act_edge_idx]

        points = []
        pl1 = act_edge.verts[0].co
        pl2 = act_edge.verts[1].co
        for edge_pas in pas_edges:
            v1 = edge_pas.verts[0].co
            v2 = edge_pas.verts[1].co
            point1, dist1 = intersect_point_line(v1, pl1, pl2)
            point2, dist2 = intersect_point_line(v2, pl1, pl2)

            if 1 > dist1 > 0 and point1 not in points:
                points.append((point1, point1 - pl1))
            if 1 > dist2 > 0 and point2 not in points:
                points.append((point2, point2 - pl1))

        points_sort = sorted(points, key=itemgetter(1))
        geom_split = bmesh.ops.bisect_edges(bm, edges=[act_edge], cuts=len(points_sort))["geom_split"]
        vertices = [v for v in geom_split if isinstance(v, bmesh.types.BMVert)]
        vertices.sort(key=lambda v: (pl1 - v.co).length)
        for idx, vert in enumerate(vertices):
            point = points_sort[idx][0]
            vert.co = point

        bmesh.update_edit_mesh(mesh)
        mesh.update()

        return {'FINISHED'}


class PaInstancesSelPair(bpy.types.Operator):
    """Select Objects by number of Instances"""
    bl_idname = "paul.instances_sel_pair"
    bl_label = "Instances Select Pair"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.active_object is not None and \
               context.active_object.type == 'MESH'

    def execute(self, context):
        # config = bpy.context.window_manager.paul_manager
        LEN_INSTANCES = 2

        objs = bpy.data.objects

        instance_group = {}
        for obj in objs:
            if obj.type != "MESH":
                continue

            o_name = obj.name
            m_name = obj.data.name
            if m_name not in instance_group:
                instance_group[m_name] = [o_name]
            else:
                instance_group[m_name].append(o_name)

        bpy.ops.object.select_all(action="DESELECT")
        for key, instances in instance_group.items():
            number = len(instances)
            if number == LEN_INSTANCES:
                for instance in instances:
                    objs[instance].select = True

        return {'FINISHED'}


class PaEdgesPairFill(bpy.types.Operator):
    r"""Connect pairs of selected edges"""
    bl_idname = "paul.edges_pairfill"
    bl_label = "Edges Pair Fill"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.active_object is not None and \
               context.active_object.type == 'MESH'

    def execute(self, context):
        def getCentre(mesh, e):
            v1 = mesh.vertices[e.vertices[0]].co
            v2 = mesh.vertices[e.vertices[1]].co
            centre = (v1 + v2) / 2
            return centre

        config = bpy.context.window_manager.paul_manager

        bpy.ops.object.mode_set(mode='OBJECT')
        bpy.ops.object.editmode_toggle()

        obj = bpy.context.active_object
        mesh = obj.data

        lEdges_idx = []
        if config.pairfill_options == 'succesive':
            bm = bmesh.new()
            bm.from_mesh(mesh)
            check_lukap(bm)

            for elem in reversed(bm.select_history):
                if isinstance(elem, bmesh.types.BMEdge):
                    lEdges_idx.append(elem.index)
            bm.free()

        else:
            edges = [(e, getCentre(mesh, e)) for e in mesh.edges if e.select]
            for i, lt1 in enumerate(edges[:-1]):
                vec1 = edges[i + 1][1] - lt1[1]
                count = 0
                for lt2 in edges[i + 1:]:
                    vec2 = lt2[1] - lt1[1]
                    if vec1.angle(vec2) < math.pi / 2:
                        count += 1

                if count == (len(edges) - i - 1):
                    break

            if len(edges) > 0:
                centre0 = edges[i][1]
                edges_sort_ = [(te[0], (te[1] - centre0).length) for te in edges]
                edges_sort = sorted(edges_sort_, key=itemgetter(1))
                lEdges_idx = [te[0].index for te in edges_sort]

        pairs = list(zip(lEdges_idx[::2], lEdges_idx[1::2]))
        for pair in pairs:
            bpy.ops.mesh.select_all(action='DESELECT')
            bpy.ops.object.editmode_toggle()
            e1 = mesh.edges[pair[0]]
            e2 = mesh.edges[pair[1]]
            e1.select = True
            e2.select = True
            bpy.ops.object.editmode_toggle()
            bpy.ops.mesh.edge_face_add()

        bpy.ops.mesh.select_all(action='DESELECT')

        return {'FINISHED'}


class PaObjMultySureUV(bpy.types.Operator):
    bl_idname = "paul.multy_sureuv"
    bl_label = "Obj MMuulty SureUV"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.active_object is not None and \
               context.active_object.type == 'MESH'

    def execute(self, context):
        config = bpy.context.window_manager.paul_manager
        for ob in bpy.context.selected_objects:
            if ob.type == 'MESH':
                bpy.context.scene.objects.active = ob
                bpy.ops.object.sureuvw_operator(action="box", \
                                                size=config.omsureuv_all_scale_def, \
                                                rot=config.omsureuv_rot, \
                                                offset=config.omsureuv_offset, \
                                                zrot=0, xoffset=0, yoffset=0, \
                                                texaspect=config.omsureuv_tex_aspect)

        return {'FINISHED'}


class PaObjFilterLocalRotated(bpy.types.Operator):
    """filter objects with rotation"""
    bl_idname = "paul.obj_filter_local_rotated"
    bl_label = "Obj filter local rotated"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.active_object is not None and \
               context.active_object.type == 'MESH'

    def execute(self, context):
        # config = bpy.context.window_manager.paul_manager
        objs = bpy.context.selected_objects
        sel_objs = []
        for obj in objs:
            if obj.type != "MESH":
                continue

            mulVecRot = sum(obj.rotation_euler)
            if mulVecRot != 0:
                sel_objs.append(obj)

        bpy.ops.object.select_all(action="DESELECT")
        for obj in sel_objs:
            obj.select = True

        return {'FINISHED'}


class PaPolyedgeSelect(bpy.types.Operator):
    """Filter contacting edges of selected faces"""
    bl_idname = "paul.polyedge_select"
    bl_label = "Polyedge select"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.active_object is not None and \
               context.active_object.type == 'MESH'

    def execute(self, context):
        bpy.ops.mesh.select_mode(use_extend=False, use_expand=False, type='EDGE')
        bpy.ops.mesh.hide(unselected=True)
        bpy.ops.mesh.region_to_loop()
        bpy.ops.mesh.reveal()
        bpy.ops.mesh.select_all(action='INVERT')
        return {'FINISHED'}


class PaSsmooth(bpy.types.Operator):
    """Mode-dependent smooth"""
    bl_idname = "mesh.ssmooth"
    bl_label = "Ssmooth"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.active_object is not None and \
               context.active_object.type == 'MESH' and \
               context.object.mode == "EDIT"

    def execute(self, context):
        if bpy.context.tool_settings.mesh_select_mode[0] and check("mesh_looptools")[0]:
            bpy.ops.mesh.looptools_relax(input='selected', interpolation='cubic', iterations='1', regular=True)
        else:
            bpy.ops.mesh.vertices_smooth()

        return {'FINISHED'}


class PaMisc_MatsFilterDupes(bpy.types.Operator):
    """filter objects with origing in one place"""
    bl_idname = "paul.filter_dupes_origins"
    bl_label = "Filter dupes"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        # config = bpy.context.window_manager.paul_manager
        bpy.ops.object.misc(type_op=2)
        return {'FINISHED'}


class PaMisc_MatsAllToActive(bpy.types.Operator):
    bl_idname = "paul.mats_all_to_active"
    bl_label = "Mats all to active"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.active_object is not None and \
               context.active_object.type == 'MESH'

    def execute(self, context):
        # config = bpy.context.window_manager.paul_manager
        bpy.ops.object.misc(type_op=8)
        return {'FINISHED'}


class PaMisc_MatsSelectedToActive(bpy.types.Operator):
    bl_idname = "paul.mats_selected_to_active"
    bl_label = "Mats selected to active"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.active_object is not None and \
               context.active_object.type == 'MESH'

    def execute(self, context):
        # config = bpy.context.window_manager.paul_manager
        bpy.ops.object.misc(type_op=14)
        return {'FINISHED'}


class PaMisc_MatnodesSwitch(bpy.types.Operator):
    bl_idname = "paul.matnodes_switch"
    bl_label = "Matnodes switch"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        # config = bpy.context.window_manager.paul_manager
        bpy.ops.object.misc(type_op=7)
        return {'FINISHED'}


class paul_managerProps(bpy.types.PropertyGroup):
    """
    Fake module like class
    bpy.context.window_manager.paul_manager
    """
    display = bpy.props.BoolProperty(name='display')
    display_align = bpy.props.BoolProperty(name='display_align', description="Align selection to active edge")
    display_offset = bpy.props.BoolProperty(name='display_offset',
                                            description="store and reuse distance for modification")
    display_3dmatch = bpy.props.BoolProperty(name='display_3dmatch', description="3point alignation by key")
    display_railer = bpy.props.BoolProperty(name='display_railer',
                                            description="spread objects along curve with straight segments"
                                            )
    loopreduce_step = bpy.props.IntProperty(name='Step', default=5, min=1)
    loopresolve_step = bpy.props.IntProperty(name='Step', default=5, min=3)
    loopresolve_dist = bpy.props.FloatProperty(name='Dist', default=1.0, min=1e-4, precision=4)
    loopresolve_relative = bpy.props.BoolProperty(name='loopresolve_relative', default=True)

    spread_x = bpy.props.BoolProperty(name='spread_x', default=False)
    spread_y = bpy.props.BoolProperty(name='spread_y', default=True)
    spread_z = bpy.props.BoolProperty(name='spread_z', default=False)
    relation = bpy.props.BoolProperty(name='relation', default=False)
    edge_idx_store = bpy.props.IntProperty(name="edge_idx_store")
    object_name_store = bpy.props.StringProperty(name="object_name_store")
    object_name_store_v = bpy.props.StringProperty(name="object_name_store_v")
    object_name_store_c = bpy.props.StringProperty(name="object_name_store_c")
    align_dist_z = bpy.props.BoolProperty(name='align_dist_z')
    align_lock_z = bpy.props.BoolProperty(name='align_lock_z')
    step_len = bpy.props.FloatProperty(name="step_len")
    vec_store = bpy.props.FloatVectorProperty(name="vec_store")
    vert_store = bpy.props.IntProperty(name="vert_store")
    coner_edge1_store = bpy.props.IntProperty(name="coner_edge1_store")
    coner_edge2_store = bpy.props.IntProperty(name="coner_edge2_store")
    active_edge1_store = bpy.props.IntProperty(name="active_edge1_store", default=-1)
    active_edge2_store = bpy.props.IntProperty(name="active_edge2_store", default=-1)
    variant = bpy.props.IntProperty(name="variant")
    instance = bpy.props.BoolProperty(name="instance")
    flip_match = bpy.props.BoolProperty(name="flip_match")
    step_angle = bpy.props.FloatProperty(name="step_angle")
    railer_dist = bpy.props.FloatProperty(name="Dist", default=1.0)
    dist_verts = bpy.props.FloatProperty(name="Dist", default=0.02, precision=2, min=0)
    compmeshes_treshold = bpy.props.FloatProperty(name="compmeshes_treshold", default=0.05, \
                                                  precision=2, min=0)
    ovr_count = IntProperty(name="Number", min=1, max=100, default=30)
    si_percent = IntProperty(name="Percent", min=1, max=100, default=98)

    shift_lockX = bpy.props.BoolProperty(name='shift_lockX', default=False)
    shift_lockY = bpy.props.BoolProperty(name='shift_lockY', default=False)
    shift_lockZ = bpy.props.BoolProperty(name='shift_lockZ', default=False)
    shift_copy = bpy.props.BoolProperty(name='shift_copy', default=False)
    shift_local = bpy.props.BoolProperty(name='shift_local', default=False)

    rotor3d_copy = bpy.props.BoolProperty(name='rotor3d_copy', default=False)
    rotor3d_instance = bpy.props.BoolProperty(name="rotor3d_instance")
    rotor3d_center = bpy.props.FloatVectorProperty(name="rotor3d_center")
    rotor3d_axis = bpy.props.FloatVectorProperty(name="rotor3d_axis")

    SPLIT = bpy.props.BoolProperty(name='SPLIT', default=False)
    inner_clear = bpy.props.BoolProperty(name='inner_clear', default=False)
    outer_clear = bpy.props.BoolProperty(name='outer_clear', default=False)
    fill_cuts = bpy.props.BoolProperty(name='fill_cuts', default=False)
    filter_edges = bpy.props.BoolProperty(name='filter_edges', default=False)
    filter_verts_top = bpy.props.BoolProperty(name='filter_verts_top', default=False)
    filter_verts_bottom = bpy.props.BoolProperty(name='filter_verts_bottom', default=False)
    disp_cp = bpy.props.BoolProperty(name='disp_cp', default=False, description="slice object with custom plane")
    disp_cp_project = bpy.props.BoolProperty(name='disp_cp_project', default=False)
    disp_cp_filter = bpy.props.BoolProperty(name='disp_cp_filter', default=False)
    filter_mats = bpy.props.BoolProperty(name='filter_mats', default=False)

    shape_inf = bpy.props.IntProperty(name="shape_inf", min=0, max=200, default=0)
    shape_spline = bpy.props.BoolProperty(name="shape_spline", default=False)
    spline_Bspline2 = bpy.props.BoolProperty(name="spline_Bspline2", default=True)
    barc_rad = bpy.props.FloatProperty(name="barc_rad")

    disp_matExtrude = bpy.props.BoolProperty(name='disp_matExtrude', default=False,
                                             description="extrude vertical material colored loop"
                                             )
    disp_projectloop = bpy.props.BoolProperty(name='disp_projectloop', default=False)
    disp_barc = bpy.props.BoolProperty(name='disp_barc', default=False)
    disp_misc = bpy.props.BoolProperty(name='disp_misc', default=False)
    disp_eap = bpy.props.BoolProperty(name='disp_eap', default=False)
    disp_fedge = bpy.props.BoolProperty(name='disp_fedge', default=False)
    disp_coll = bpy.props.BoolProperty(name='disp_coll', default=False)
    disp_3drotor = bpy.props.BoolProperty(name='disp_3drotor', default=False, description="manipulate object with key")
    disp_obj = bpy.props.BoolProperty(name='disp_obj', default=False)
    disp_chunks = bpy.props.BoolProperty(name='disp_chunks', default=False)
    disp_corner = bpy.props.BoolProperty(name='disp_corner', default=False,
                                         description="lengthen or split edges by projections"
                                         )
    disp_reduce = bpy.props.BoolProperty(name='disp_reduce', default=False)
    disp_sel = bpy.props.BoolProperty(name='disp_sel', default=False,
                                      description='Set length of selected edges equal to stored in Sideshift '
                                      )
    disp_zmj100 = bpy.props.BoolProperty(name='disp_zmj100', default=False)
    disp_distverts = bpy.props.BoolProperty(name='disp_distverts', default=False,
                                            description="find verts that will be collapsed with remove doubles"
                                            )
    disp_compmeshes = bpy.props.BoolProperty(name='disp_compmeshes', default=False,
                                             description="per vertex objects comparison"
                                             )
    disp_blendupcleanup = bpy.props.BoolProperty(name='disp_blendupcleanup', default=False)
    disp_milovsky = bpy.props.BoolProperty(name='disp_milovsky', default=False)
    disp_omsureuv = bpy.props.BoolProperty(name='disp_omsureuv', default=False)
    disp_ovr = bpy.props.BoolProperty(name='disp_ovr', default=False)
    disp_si1 = bpy.props.BoolProperty(name='disp_si1', default=False)
    disp_si2 = bpy.props.BoolProperty(name='disp_si2', default=False)
    disp_pairfill = bpy.props.BoolProperty(name='disp_pairfill', default=False)
    disp_loopreduce = bpy.props.BoolProperty(name='disp_loopreduce', default=False)
    disp_test = bpy.props.BoolProperty(name='disp_test', default=False)
    disp_afas = bpy.props.BoolProperty(name='disp_afas', default=False)
    disp_naminginstances = bpy.props.BoolProperty(name='disp_naminginstances', default=False)
    disp_loopresolve = bpy.props.BoolProperty(name='disp_loopresolve', default=False)
    disp_mborder = bpy.props.BoolProperty(name='disp_mborder', default=False)
    disp_batch = bpy.props.BoolProperty(name='disp_batch', default=False)
    disp_render = bpy.props.BoolProperty(name='disp_render', default=False)
    disp_bremover = bpy.props.BoolProperty(name='disp_bremover', default=False)
    disp_inst_repl = bpy.props.BoolProperty(name='disp_inst_repl', default=False)
    display_edgloop = bpy.props.BoolProperty(name='display_edgloop', default=False,
                                             description='Tools about Edges and Loops')
    disp_cad = bpy.props.BoolProperty(name='disp_cad', default=False)
    disp_objed = bpy.props.BoolProperty(name='disp_objed', default=False)
    disp_build = bpy.props.BoolProperty(name='disp_build', default=False)
    disp_materials = bpy.props.BoolProperty(name='disp_materials', default=False)

    mborder_size = FloatProperty(name="mborder_size", default=0.1, precision=1, max=100, min=-100)

    oso_vizing = bpy.props.BoolProperty(name='oso_vizing', default=False)
    oso_select = bpy.props.BoolProperty(name='oso_select', default=False)
    oso_render = bpy.props.BoolProperty(name='oso_render', default=False)

    omsureuv_all_scale_def = FloatProperty(name="omsureuv_all_scale_def", default=omsureuv_all_scale_def_glob,
                                           precision=4)
    omsureuv_tex_aspect = FloatProperty(name="omsureuv_tex_aspect", default=1.0, precision=4)
    omsureuv_rot = FloatVectorProperty(name="omsureuv_rot", precision=2)
    omsureuv_offset = FloatVectorProperty(name="omsureuv_offset", precision=4)

    afas_angle = FloatProperty(name='angle', max=pi, min=0, default=0.2)
    vproj_active = BoolProperty(name='active edge', default=False, description='Use active edge')
    fedge_angle = BoolProperty(name='angle', default=False)
    fedge_verts = BoolProperty(name='verts', default=True)
    fedge_edges = BoolProperty(name='edges', default=True)
    fedge_zerop = BoolProperty(name='zerop', default=True)
    fedge_empty = BoolProperty(name='empty', default=True)
    fedge_three = BoolProperty(name='three', default=True)
    fedge_tris = BoolProperty(name='tris', default=True)
    fedge_snm = BoolProperty(name='fedge_snm', default=True)
    fedge_nonquads = BoolProperty(name='nonquads', default=True)
    fedge_WRONG_AREA = bpy.props.FloatProperty(name="WRONG_AREA", default=0.02, precision=2)
    corner_active_edge = BoolProperty(name='coner_active_edge', default=False)
    to_corner_active_edge = BoolProperty(name='to_coner_active_edge', default=True)
    corner_overlap = BoolProperty(name='corner_overlap', default=False)
    active_length_ratio = BoolProperty(name='active_length_ratio', default=False)
    verts_activate = BoolProperty(name='verts_activate', default=False)
    valsel_objectmode = BoolProperty(name='valsel_objectmode', default=False)
    inst_repl_use_translation = BoolProperty(name='inst_repl_use_translation', default=False)
    inst_repl_from = StringProperty(name="inst_repl_from")
    inst_repl_to = StringProperty(name="inst_repl_to")
    inst_repl_select = BoolProperty(name='inst_repl_select', default=False)
    batch_opengl = BoolProperty(name='batch_opengl', default=False)

    chunks_clamp = bpy.props.IntProperty(name="chunks_clamp", default=1, \
                                         min=1, max=100, step=1, subtype='FACTOR')
    chunks_setting = EnumProperty(
        name="Chunks settings",
        items=(('V', "vertices", ""),
               ('F', "faces", ""),
               ('SF', "semantic faces", ""),
               ('FC', "filter chunks", "")
               ),
        default='SF',
    )

    # List of operator properties, the attributes will be assigned
    # to the class instance from the operator settings before calling.
    by_layers_setting = BoolProperty(
        name="By layers",
        description="Import sorted by name objects to layers: 1,2,3, ... , 20",
        default=False,
    )
    ngons_setting = BoolProperty(
        name="NGons",
        description="Import faces with more than 4 verts as ngons",
        default=True,
    )
    edges_setting = BoolProperty(
        name="Lines",
        description="Import lines and faces with 2 verts as edge",
        default=True,
    )
    smooth_groups_setting = BoolProperty(
        name="Smooth Groups",
        description="Surround smooth groups by sharp edges",
        default=True,
    )

    split_objects_setting = BoolProperty(
        name="Object",
        description="Import OBJ Objects into Blender Objects",
        default=True,
    )
    split_groups_setting = BoolProperty(
        name="Group",
        description="Import OBJ Groups into Blender Objects",
        default=True,
    )

    groups_as_vgroups_setting = BoolProperty(
        name="Poly Groups",
        description="Import OBJ groups as vertex groups",
        default=False,
    )

    image_search_setting = BoolProperty(
        name="Image Search",
        description="Search subdirs for any associated images "
                    "(Warning, may be slow)",
        default=True,
    )

    split_mode_setting = EnumProperty(
        name="Split",
        items=(('ON', "Split", "Split geometry, omits unused verts"),
               ('OFF', "Keep Vert Order", "Keep vertex order from file"),
               ),
    )

    clamp_size_setting = FloatProperty(
        name="Clamp Size",
        description="Clamp bounds under this value (zero to disable)",
        min=0.0, max=1000.0,
        soft_min=0.0, soft_max=1000.0,
        default=0.0,
    )
    axis_forward_setting = EnumProperty(
        name="Forward",
        items=(('X', "X Forward", ""),
               ('Y', "Y Forward", ""),
               ('Z', "Z Forward", ""),
               ('-X', "-X Forward", ""),
               ('-Y', "-Y Forward", ""),
               ('-Z', "-Z Forward", ""),
               ),
        default='-Z',
    )

    axis_up_setting = EnumProperty(
        name="Up",
        items=(('X', "X Up", ""),
               ('Y', "Y Up", ""),
               ('Z', "Z Up", ""),
               ('-X', "-X Up", ""),
               ('-Y', "-Y Up", ""),
               ('-Z', "-Z Up", ""),
               ),
        default='Y',
    )

    ovr_options = EnumProperty(
        name="Sorting option",
        items=(
            ('E', "E - verts density", ""),
            ('D', "D - edges density", ""),
            ('C', "C - verts local", ""),
            ('B', "B - instances count", ""),
            ('A', "A - verts summ", ""),
        ),
        default='A',
    )

    pairfill_options = EnumProperty(
        name="Pairfill options",
        items=(
            ('succesive', "Succesive", ""),
            ('linear', "Linear", ""),
        ),
        default='succesive',
    )


class PaSearchInstanses1(bpy.types.Operator):
    r"""Поиск потенциальных инстансов по активному объекту"""
    bl_idname = "paul.search_instanses_1"
    bl_label = "Search Instanses by Active Object"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.active_object is not None and \
               context.active_object.type == 'MESH'

    def execute(self, context):
        config = bpy.context.window_manager.paul_manager
        self.TRESHOLD = 0.002
        self.PERCENT = config.si_percent

        sel_objs = [obj for obj in bpy.context.selected_objects if obj.type == "MESH"]
        act_obj = bpy.context.active_object
        instances = PaSearchInstanses2.findFragments(self, act_obj, sel_objs, config.filter_mats)
        bpy.ops.object.select_all(action='DESELECT')
        for obj in instances:
            obj.select = True
        return {'FINISHED'}


class PaSearchInstanses2(bpy.types.Operator):
    r"""Поиск потенциальных инстансов в выделении, игнорируя целые цепи"""
    bl_idname = "paul.search_instanses_2"
    bl_label = "Search Instanses"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.active_object is not None and \
               context.active_object.type == 'MESH'

    def findFragments(self, act_obj, sel_objs, filter_mats):
        def compMeshesVerts2(obj1, obj2, treshold, percent):
            mesh1 = obj1.data
            size = len(mesh1.vertices)
            kd = mathutils.kdtree.KDTree(size)

            for i, v in enumerate(mesh1.vertices):
                kd.insert(v.co, i)

            kd.balance()
            sel_v = 0
            mesh2 = obj2.data
            size2 = len(mesh2.vertices)
            kd2 = mathutils.kdtree.KDTree(size2)
            for i, v in enumerate(mesh2.vertices):
                kd2.insert(v.co, i)
                co, index, dist = kd.find(v.co)
                if dist > treshold:
                    sel_v += 1

            kd2.balance()
            for i, v in enumerate(mesh1.vertices):
                co, index, dist = kd2.find(v.co)
                if dist > treshold:
                    sel_v += 1

            percent_ = 100 - sel_v / len(mesh2.vertices) * 100
            return percent_ >= percent

        act_mesh = act_obj.data
        len_act_verts = len(act_mesh.vertices)
        meshes = {act_mesh.name: True}
        to_sel_objs = []
        mats_act_obj = [slot.material for slot in act_obj.material_slots]

        for obj in sel_objs:
            mesh = obj.data

            if len(mesh.vertices) != len_act_verts:
                meshes[mesh.name] = False
                continue

            if filter_mats:
                mats_obj = [slot.material for slot in obj.material_slots]
                # if mats_obj != mats_act_obj:
                if not compare_notstrict_list_order(mats_obj, mats_act_obj):
                    meshes[mesh.name] = False
                    continue

            if mesh.name in meshes:
                # obj.select = meshes[mesh.name]
                if meshes[mesh.name]:
                    to_sel_objs.append(obj)
                continue

            result = compMeshesVerts2(act_obj, obj, self.TRESHOLD, self.PERCENT)
            meshes[mesh.name] = result
            # obj.select = result
            if result:
                to_sel_objs.append(obj)

        return to_sel_objs

    def execute(self, context):
        config = bpy.context.window_manager.paul_manager
        self.TRESHOLD = 0.002
        self.PERCENT = config.si_percent

        sel_objs = [o for o in bpy.context.selected_objects if o.type == 'MESH']
        blacklist_objs = []
        result_list = []

        for act_obj in sel_objs:
            if act_obj in blacklist_objs: continue
            act_len_vts = len(act_obj.data.vertices)
            to_select_objs = [act_obj]
            mats_act_obj = [slot.material for slot in act_obj.material_slots]
            for obj in sel_objs:
                if obj == act_obj: continue
                len_vts = len(obj.data.vertices)
                if act_len_vts == len_vts:
                    if config.filter_mats:
                        mats_obj = [slot.material for slot in obj.material_slots]
                        if not compare_notstrict_list_order(mats_obj, mats_act_obj):
                            continue

                    to_select_objs.append(obj)

            result_list.append(to_select_objs)
            blacklist_objs.extend(to_select_objs)

        sort_list = sorted(result_list, key=len, reverse=True)
        chain_instances = []

        for prev_chain in sort_list:
            black_chain_instances = []
            for idx, act_obj in enumerate(prev_chain):
                if act_obj in black_chain_instances:
                    continue
                sel_objs = prev_chain[idx + 1:]
                if sel_objs:
                    local_chain = self.findFragments(act_obj, sel_objs, config.filter_mats)
                    if local_chain:
                        chain_instances.append([act_obj] + local_chain)
                        black_chain_instances.extend(chain_instances[-1])
                        if len(chain_instances[-1]) == len(prev_chain):
                            break

            if len(chain_instances[-1]) == len(prev_chain):
                break

        sort_list = sorted(chain_instances, key=len, reverse=True)
        if sort_list:
            bpy.ops.object.select_all(action='DESELECT')
            for obj in sort_list[0]:
                obj.select = True

        return {'FINISHED'}


class MessageOperator(bpy.types.Operator):
    from bpy.props import StringProperty

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
                          type="Message",
                          message=message)


def print_error2(message, code_error='None'):
    print('Error:' + code_error)
    bpy.ops.error.message('INVOKE_DEFAULT',
                          type="Message",
                          message=message)


def print_error3(message, code_error='None', self=None):
    print('Error: ' + code_error)
    print_info(message, self)


def print_info(message, self=None):
    print_error(message)
    print(message)
    if self:
        self.report({'INFO'}, message)


class CheredatorModalOperator(bpy.types.Operator):
    """Remove checker deselected vertices from loop"""
    bl_idname = "mesh.modal_cheredator"
    bl_label = "Cheredator"
    bl_options = {'REGISTER', 'UNDO'}
    steps = bpy.props.IntProperty(options={'HIDDEN'})
    type_op = bpy.props.IntProperty(name='type_op', default=0, options={'HIDDEN'})

    def execute(self, context):
        context.scene['cheredator'] = cheredator_fantom(self)
        return

    def modal(self, context, event):
        # context.area.tag_redraw()
        if self.type_op == 0:
            cheredator(2)

        if event.type == 'WHEELDOWNMOUSE':
            self.steps += 1
            self.execute(context)
            if not context.scene['cheredator']:
                self.steps -= 1

        elif event.type == 'WHEELUPMOUSE':
            self.steps = max(self.steps - 1, 0)
            self.execute(context)
        elif event.type == 'LEFTMOUSE':  # Confirm
            bpy.types.SpaceView3D.draw_handler_remove(self._handle, 'WINDOW')
            cheredator(self.steps)
            return {'FINISHED'}
        elif self.type_op == 0 or event.type in ('RIGHTMOUSE', 'ESC') or not context.scene['cheredator']:  # Cancel
            bpy.types.SpaceView3D.draw_handler_remove(self._handle, 'WINDOW')
            return {'CANCELLED'}

        return {'RUNNING_MODAL'}

    def invoke(self, context, event):
        self.steps = 2

        ars = (self,)
        self._handle = bpy.types.SpaceView3D.draw_handler_add(cheredator_fantom, ars, 'WINDOW', 'POST_VIEW')
        self.execute(context)
        context.window_manager.modal_handler_add(self)
        return {'RUNNING_MODAL'}


# *********** Import Objs *************
'''
"name": "Import multiple OBJ files",
"author": "poor",
"description": "Import multiple OBJ files, UV's, materials",
'''


class ImportMultipleObjs(bpy.types.Operator, ImportHelper):
    """This appears in the tooltip of the operator and in the generated docs"""
    bl_idname = "import_scene.multiple_objs"
    bl_label = "Import multiple OBJ's"
    bl_options = {'PRESET', 'UNDO'}

    # ImportHelper mixin class uses this
    filename_ext = ".obj"

    filter_glob = StringProperty(
        default="*.obj",
        options={'HIDDEN'},
    )

    # Selected files
    files = CollectionProperty(type=bpy.types.PropertyGroup)

    def execute(self, context):
        def get_filename(file):
            return file.name

        config = bpy.context.window_manager.paul_manager

        # get the folder
        folder = (os.path.dirname(self.filepath))

        first_layer_idx = 0
        if config.by_layers_setting:
            sort_files = sorted(self.files, key=get_filename)
            layers_context = list(bpy.context.scene.layers[:])
            first_layer_idx = layers_context.index(True)
        else:
            sort_files = self.files

        # iterate through the selected files
        for idx, i in enumerate(sort_files):
            if config.by_layers_setting:
                layers = [False] * 20
                idx_layer = min(19, idx + first_layer_idx)
                layers[idx_layer] = True
                layers_context[idx_layer] = True
                bpy.context.scene.layers = layers

            # generate full path to file
            path_to_file = (os.path.join(folder, i.name))

            # call obj operator and assign ui values
            bpy.ops.import_scene.obj(filepath=path_to_file,
                                     axis_forward=config.axis_forward_setting,
                                     axis_up=config.axis_up_setting,
                                     use_edges=config.edges_setting,
                                     use_smooth_groups=config.smooth_groups_setting,
                                     use_split_objects=config.split_objects_setting,
                                     use_split_groups=config.split_groups_setting,
                                     use_groups_as_vgroups=config.groups_as_vgroups_setting,
                                     use_image_search=config.image_search_setting,
                                     split_mode=config.split_mode_setting,
                                     global_clamp_size=config.clamp_size_setting)
        if config.by_layers_setting:
            bpy.context.scene.layers = layers_context
        return {'FINISHED'}


# ***********  Autoupdate  ***************
class ThisScriptUpdateAddon(bpy.types.Operator):
    """ Update this addon without any browsing and so on. After - press F8 to reload addons """
    bl_idname = "script.paul_update_addon"
    bl_label = "Update 1D_script addon"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        script_paths = os.path.normpath(os.path.dirname(__file__))
        os.curdir = os.path.dirname(os.path.join(script_paths, 'addons'))
        os.chdir(os.curdir)

        try:
            url = 'https://www.dropbox.com/s/xf4lbn5l87bmdzb/1D_Scripts.py'
            file = urllib.request.urlretrieve(url, os.path.normpath(os.path.join(os.curdir, '1D_Scripts.py')))
            self.report({'INFO'}, "Reload addons with F8 button")
        except:
            self.report({'ERROR'}, "Cannot retrieve file from Internet")
        return {'FINISHED'}


classes = [eap_op0, eap_op1, eap_op2, eap_op3, ChunksOperator, f_op0,
           RenderMe, ExportSomeData, RotorOperator, DisableDubleSideOperator, ImportMultipleObjs,
           MatExrudeOperator, GetMatsOperator, CrossPolsOperator, SSOperator, SpreadOperator,
           AlignOperator, Project3DLoopOperator, BarcOperator, LayoutSSPanel, MessageOperator,
           OffsetOperator, MiscOperator, paul_managerProps, ThisScriptUpdateAddon,
           CheredatorModalOperator, D1_fedge, CornerOperator, SelOperator, RailerOperator,
           DistVerticesOperator, CompareMeshes, PaInstancesRecount, PaInstancesRename,
           PaMatsDatafix, PaInstancesSelPair, SureUVWOperator, PaObjMultySureUV,
           PaInstancesUnique, PaObjNegScale, PaObjFilterLocalRotated, MatsSelMultiple,
           PaInstancesMeshnameReplacePP, PaSetAutoSmooth, PsSelSameVerts,
           PaMatsUnclone, PaMatsPurgeout, PaSearchInstanses1, PaSearchInstanses2,
           PaHeavyNgons, PaCleanGlass, PaVertsProjectOnEdge, PaEdgesPairFill, PaObnameMats,
           PaLoopReduce, AFASOperator, MatsEqualizeOperator, PaMisc_MatsAllToActive,
           PaMisc_MatsSelectedToActive, PaMisc_MatnodesSwitch, PaStairsMaker, EExtrudeAlongPath,
           PaGroupSelectLinked, BTSelectInstancesOperator, PaImageTPanel,
           BTFilterInstancesOperator, BTObjDistributeByXOperator, BTObnameToMeshnameOperator,
           BTMeshnameToObnameOperator, BTIsolateLayersOperator, PaMisc_MatsFilterDupes,
           BTDropInstancesOperator, PaLoopResolve, PaBarcCreateOperator, PaBarcSetOperator,
           PaBarcCursorOperator, PaSideShiftStoreDist, PaSideShiftActiveCursor,
           PaSideShiftBackward, PaSideShiftForward, PaPropagateObname, SUV_OT_spreads,
           PaMakeBorder, UvScalerOperator, PaRCS, NATimeLineRenderStart, NGD1_camswitch, PaInstanceResizer,
           PaNJoin, AMCornerCross, AMExtendCross, PaVolumeSelect,
           BTBatchUVMapsEraserOperator, BTBatchVertexGroupEraserOperator,
           BTBatchShapeKeysEraserOperator, BTBatchVertexColorsEraserOperator, BTBatchMaterialEraserOperator,
           BTBatchGPencilEraserOperator, BTAllModifiersEraserOperator, BTAllSubsurfsEraserOperator,
           BTZeroSubsurfsEraserOperator, BTEdgeSplitRemoverOperator, BTMirrorMDFRemoverOperator,
           BTMultipleUVMapsRemoverOperator, BTBevelModifierRemoverOperator, BTEmptySlotsRemoverOperator,
           BatchOperatorSettings, PaObjSwitchOnOff, PaObjSelectModified, PaCurvesSelect2D, PaCurveSwap2D3D,
           PaMatsSort, PaPolyedgeSelect, PaSsmooth
           ]

addon_keymaps = []


def register():
    for c in classes:
        bpy.utils.register_class(c)

    bpy.types.WindowManager.paul_manager = \
        bpy.props.PointerProperty(type=paul_managerProps)
    bpy.context.window_manager.paul_manager.display = False
    bpy.context.window_manager.paul_manager.display_align = False
    bpy.context.window_manager.paul_manager.spread_x = False
    bpy.context.window_manager.paul_manager.spread_y = True
    bpy.context.window_manager.paul_manager.spread_z = False
    bpy.context.window_manager.paul_manager.relation = False
    bpy.context.window_manager.paul_manager.edge_idx_store = -1
    bpy.context.window_manager.paul_manager.object_name_store = ''
    bpy.context.window_manager.paul_manager.object_name_store_c = ''
    bpy.context.window_manager.paul_manager.object_name_store_v = ''
    bpy.context.window_manager.paul_manager.active_edge1_store = -1
    bpy.context.window_manager.paul_manager.active_edge2_store = -1
    bpy.context.window_manager.paul_manager.coner_edge1_store = -1
    bpy.context.window_manager.paul_manager.coner_edge2_store = -1
    bpy.context.window_manager.paul_manager.align_dist_z = False
    bpy.context.window_manager.paul_manager.align_lock_z = False
    bpy.context.window_manager.paul_manager.step_len = 1.0
    bpy.context.window_manager.paul_manager.instance = False
    bpy.context.window_manager.paul_manager.display_3dmatch = False
    bpy.context.window_manager.paul_manager.flip_match = False
    bpy.context.window_manager.paul_manager.variant = 0
    bpy.context.window_manager.paul_manager.SPLIT = False
    bpy.context.window_manager.paul_manager.inner_clear = False
    bpy.context.window_manager.paul_manager.outer_clear = False
    bpy.context.window_manager.paul_manager.fill_cuts = False
    bpy.context.window_manager.paul_manager.filter_edges = False
    bpy.context.window_manager.paul_manager.filter_verts_top = False
    bpy.context.window_manager.paul_manager.filter_verts_bottom = False
    bpy.context.window_manager.paul_manager.shape_inf = 0
    bpy.context.window_manager.paul_manager.ovr_count = 10
    bpy.context.window_manager.paul_manager.afas_angle = 0.2
    bpy.context.window_manager.paul_manager.disp_cp = False
    bpy.context.window_manager.paul_manager.disp_3drotor = False
    bpy.context.window_manager.paul_manager.disp_corner = False
    bpy.context.window_manager.paul_manager.disp_cad = False
    bpy.context.window_manager.paul_manager.display_offset = False
    bpy.context.window_manager.paul_manager.disp_objed = False
    bpy.context.window_manager.paul_manager.disp_build = False
    bpy.context.window_manager.paul_manager.disp_compmeshes = False
    bpy.context.window_manager.paul_manager.disp_chunks = False
    bpy.context.window_manager.paul_manager.disp_materials = False
    bpy.context.window_manager.paul_manager.display_railer = False
    bpy.context.window_manager.paul_manager.disp_matExtrude = False
    bpy.context.window_manager.paul_manager.disp_distverts = False

    bpy.types.Scene.batch_operator_settings = \
        bpy.props.PointerProperty(type=BatchOperatorSettings)

    wm = bpy.context.window_manager
    km = wm.keyconfigs.addon.keymaps.new(name='offset', space_type='VIEW_3D')
    kmi = km.keymap_items.new(OffsetOperator.bl_idname, 'R', 'PRESS', ctrl=False, shift=True)
    addon_keymaps.append((km, kmi))


def unregister():
    for km, kmi in addon_keymaps:
        km.keymap_items.remove(kmi)
    addon_keymaps.clear()

    if hasattr(bpy.types.Scene, 'batch_operator_settings'):
        del bpy.types.Scene.batch_operator_settings

    del bpy.types.WindowManager.paul_manager
    classes.reverse()
    for c in classes:
        bpy.utils.unregister_class(c)


if __name__ == "__main__":
    register()
