import bpy
import bmesh
import random

pos = random.randint(0,5)
bpy.ops.mesh.primitive_uv_sphere_add(radius=1, enter_editmode=False, location=(pos, pos, pos))
bpy.ops.object.modifier_add(type='COLLISION')

bpy.ops.mesh.primitive_plane_add(size=4, enter_editmode=False, location=(pos, pos, pos+1.05))
bpy.context.active_object.name = 'plane'

cloth = bpy.context.scene.objects["plane"]
bpy.ops.object.select_all(action='DESELECT')
bpy.context.view_layer.objects.active = cloth
cloth.select_set(True)    
bpy.ops.object.mode_set(mode='EDIT')
#cloth.select_set(True)    
#bpy.context.view_layer.objects.active = cloth
bpy.ops.mesh.subdivide(number_cuts=40, quadcorner='INNERVERT')
bpy.ops.object.modifier_add(type='CLOTH')
 
#bpy.context.object.modifiers["CLOTH"].frame_end = 120
#bpy.context.space_data.context = 'PHYSICS'
#bpy.ops.ptcache.bake(bake=True)
#bpy.context.space_data.context = 'MODIFIER'
#bpy.context.space_data.context = 'PHYSICS'
bpy.ops.object.mode_set(mode='OBJECT')
bpy.ops.ptcache.bake_all(bake=True)

depsgraph = bpy.context.evaluated_depsgraph_get()
obj = bpy.data.objects['plane']

bm = bmesh.new()

outfile = open("simulation_data.csv","w")
for i in range(1,45):
    bpy.context.scene.frame_set(i)
    bm.from_object( obj, depsgraph )
    for v in bm.verts:
        outfile.write( str(v.co.x) + "," + str(v.co.y) + "," + str(v.co.z)+ "," )
        outfile.write("\n")
    outfile.write("\n")
bm.free()
       