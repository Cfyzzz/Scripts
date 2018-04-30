# -*- coding: utf-8 -*- 
# Author: Alexander Nedovizin
# A simple check on the entry point (Empty) into the object (Suzanne)

import bpy
import mathutils


print('\n\n***** start *****')

obj = bpy.context.scene.objects['Suzanne']
point = bpy.context.scene.objects['Empty'].location
mesh = obj.data

size = len(mesh.vertices)
kd = mathutils.kdtree.KDTree(size)

for i, p in enumerate(mesh.polygons):
    kd.insert(obj.matrix_local * p.center, i)

kd.balance()

flag = True
# Далее находим ближайшие 10 точек в модели и проверим их на нормали
for (co, index, dist) in kd.find_n(point, 10):
    p_no = mesh.polygons[index].normal
    pt_a = p_no + co
    cross_pt = mathutils.geometry.intersect_line_plane(pt_a, point, co, p_no)
    if cross_pt:
        pose_pt = mathutils.geometry.intersect_point_line(cross_pt, pt_a, point)
        if pose_pt[1]>1 or pose_pt[1]<0:
            flag = False
            break
    


if flag: 
    print('is_boundary')
else:
    print('not is_boundary')

