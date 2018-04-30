# -*- coding: utf-8 -*-     

# Author:           Alexander Nedovizin
# name script:      Cross_pols.py
# version:          0.6

import bpy
import mathutils
from mathutils import Vector
import bmesh

SPLIT = False                    # SPLIT/CROSS режим включается когда остальные выключены
inner_clear = False                 # опция режима SPLIT/CROSS
outer_clear = False                 # опция режима SPLIT/CROSS
fill_cuts = False                   # опция режима SPLIT/CROSS

filter_edges = False             # Режим пересеченных ребер. включается, когда остальные режимы выключены

filter_verts_top = False         # Режим выделения вершин и его Опция верхняя половина (по нормали секатора)
filter_verts_bottom = False      # Режим выделения вершин и его Опция нижняя половина (по нормали секатора)

# http://dl.dropboxusercontent.com/u/59609328/Blender-Rus/Cross_pols.py


def main():
    obj = bpy.context.active_object
    if obj.type != 'MESH':
        return
    
    bpy.ops.object.mode_set(mode='OBJECT')  
    bpy.ops.object.mode_set(mode='EDIT')  
    bpy.ops.mesh.select_mode(type='FACE') 
    
    me = obj.data
    
    
    bm = bmesh.new()
    bm.from_mesh(me)
    
    P1 = me.polygons[bm.faces.active.index]
    pols = [p.index for p in me.polygons if p.select and p.index!= P1.index]
    sel_edges = []
    sel_verts = []
    vts_all = [v for v in bm.verts if v.select and v.index not in P1.vertices]
    eds_all = [e for e in bm.edges if e.select and e.verts[0].index not in P1.vertices \
                                               and e.verts[1].index not in P1.vertices]
    
    if not filter_verts_top and not filter_verts_bottom and not filter_edges:
        p1_co = me.vertices[P1.vertices[0]].co
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
                    if pose_pt[1]<=1 and pose_pt[1]>=0:
                        points.append(pose_pt[0])
                        split_ed.append(idx)
                        
                
            if len(points)==2:
                bpy.ops.mesh.select_mode(type='VERT') 
                if not SPLIT:
                    v1=bm.verts.new(points[0])
                    v2=bm.verts.new(points[1])
                    bm.verts.index_update() 
                    edge = (v1,v2)
                    edg_i = bm.edges.new(edge)
                    sel_edges.append(edg_i)
                else:
                    """ Функция позаимствована из адона Сверчок нод Bisect """
                    verts4cut = vts_all
                    edges4cut = eds_all
                    faces4cut = [fa for fa in bm.faces if fa.index in pols]
                    edges4cut_idx = [ed.index for ed in eds_all]
                    
                    geom_in = verts4cut + edges4cut + faces4cut
                    res = bmesh.ops.bisect_plane(bm, geom=geom_in, dist=0.00001,
                                                 plane_co=p1_co, plane_no=p1_no, use_snap_center=False,
                                                 clear_outer=outer_clear, clear_inner=inner_clear)
                    
                    fres = bmesh.ops.edgenet_prepare(bm, edges=[e for e in res['geom_cut']
                                                                if isinstance(e, bmesh.types.BMEdge)])
                    
                    sel_edges = [e for e in fres['edges'] if e.index not in edges4cut_idx]
                    
                    # this needs work function with solid gemometry
                    if fill_cuts:
                        fres = bmesh.ops.edgenet_prepare(bm, edges=[e for e in res['geom_cut']
                                                                    if isinstance(e, bmesh.types.BMEdge)])
                        bmesh.ops.edgeloop_fill(bm, edges=fres['edges'])

                    bm.verts.index_update()
                    bm.edges.index_update()
                    bm.faces.index_update()
                    break
           
    if filter_verts_top or filter_verts_bottom:
        bpy.ops.mesh.select_mode(type='VERT') 
        p1_co = me.vertices[P1.vertices[0]].co
        p1_no = P1.normal
        for v in vts_all:
            res = mathutils.geometry.distance_point_to_plane(v.co, p1_co, p1_no)
            if res>=0:
                if filter_verts_top:
                    sel_verts.append(v)
            else:
                if filter_verts_bottom:
                    sel_verts.append(v)
            
    if filter_edges and not filter_verts_top and not filter_verts_bottom:
        bpy.ops.mesh.select_mode(type='EDGE') 
        p1_co = me.vertices[P1.vertices[0]].co
        p1_no = P1.normal
        print(eds_all)
        for idx, edg in enumerate(eds_all):
            pt_a = edg.verts[0].co
            pt_b = edg.verts[1].co
            cross_pt = mathutils.geometry.intersect_line_plane(pt_a, pt_b, p1_co, p1_no)
            if cross_pt:
                pose_pt = mathutils.geometry.intersect_point_line(cross_pt, pt_a, pt_b)
                if pose_pt[1]<=1 and pose_pt[1]>=0:
                    sel_edges.append(edg)
            
    bm.edges.index_update()
    for v in bm.verts:
        v.select_set(False)
        bm.select_flush(False)
    for ed in sel_edges:
        ed.select=True
    for ed in sel_verts:
        ed.select=True
        
    bpy.ops.object.mode_set(mode='OBJECT') 
    bm.to_mesh(me)       
    me.update()   
    bm.free()
    bpy.ops.object.mode_set(mode='EDIT')  
            
    
main()