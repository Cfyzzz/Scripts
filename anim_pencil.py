# Nedovizin Alexander

import bpy
import math
from mathutils import Vector    


def MakePolyLine(objname, curvename, cList):    
    w = 1 # weight   
    curvedata = bpy.data.curves.new(name=curvename, type='CURVE')    
    curvedata.dimensions = '3D'    
    
    objectdata = bpy.data.objects.new(objname, curvedata)    
    objectdata.location = (0,0,0) #object origin    
    bpy.context.scene.objects.link(objectdata)    
    
    polyline = curvedata.splines.new('NURBS')    
    polyline.points.add(len(cList)-1)    
    for num in range(len(cList)):    
        x, y, z = cList[num]    
        polyline.points[num].co = (x, y, z, w)    
    
    polyline.order_u = len(polyline.points)-1  
    polyline.use_endpoint_u = True  
    return curvedata
      
    
points=[]
start_frame=1
word_frames = 30

for gp in bpy.data.grease_pencil:
    for gpl in gp.layers:
        for idx, stroke in enumerate(gpl.active_frame.strokes):
            for p in stroke.points:
                points.append(Vector(p.co))
            
            word_frames = len(stroke.points)    
            polyline = MakePolyLine("NameOfMyCurveObject", "NameOfMyCurve", points) 
            points=[]
            
            print(type(polyline))
            polyline.bevel_depth = 0.02

            polyline.bevel_factor_end = 0
            polyline.keyframe_insert(data_path='bevel_factor_end', frame = start_frame)           
            start_frame += word_frames
            polyline.bevel_factor_end = 1
            polyline.keyframe_insert(data_path='bevel_factor_end', frame = start_frame)           
            
bpy.context.scene.frame_end = start_frame + 100         
            
            