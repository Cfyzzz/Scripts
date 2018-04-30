# -*- coding: utf-8 -*-  

# Alexander Nedovizin, 2013
# version 0.1

import bpy
import bmesh

scene = bpy.context.scene
objects = scene.objects 
for o in objects: 
    if o.type != 'MESH':
        continue
    
    me=o.data
    sym_split = '.P.'
    name_split = o.name.split(sym_split)
    if len(name_split)==2:
        o.name = name_split[0]+sym_split+str(len(me.polygons))
    else:
        o.name = o.name+sym_split+str(len(me.polygons))
    
    bm = bmesh.new()
    bm.from_mesh(me)   
    
    true_edges=[]
    for face in bm.faces:
        true_edges.extend([e.index for e in face.edges])
    
    flag=False
    for edge in bm.edges:
        if edge.index not in true_edges:
            flag=True
            if len(o.name)>1 and o.name[:2]=="$_":
                pass
            else:
                o.name = "$_"+o.name
            break
    
    if not flag and len(o.name)>2 and o.name[:2]=="$_":
        o.name = o.name[2:]
    
    bm.free() 

