import bpy
import bmesh
import random

pos_x = random.randint(0,5)
pos_y = random.randint(0,5)
pos_z = random.randint(0,5)
bpy.ops.mesh.primitive_uv_sphere_add(radius=1, enter_editmode=False, location=(pos_x, pos_y, pos_z))
bpy.ops.object.modifier_add(type='COLLISION')

bpy.ops.mesh.primitive_plane_add(size=4, enter_editmode=False, location=(pos_y, pos_x, pos_z+1.05))
bpy.context.active_object.name = 'plane'

cloth = bpy.context.scene.objects["plane"]
bpy.ops.object.select_all(action='DESELECT')
bpy.context.view_layer.objects.active = cloth
cloth.select_set(True)    
bpy.ops.object.mode_set(mode='EDIT')
#cloth.select_set(True)    
#bpy.context.view_layer.objects.active = cloth
bpy.ops.mesh.subdivide(number_cuts=18, quadcorner='INNERVERT')
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

sphere = bpy.data.objects['Sphere']

outfile = open("simulation_data_x.csv","w")
outfile_y = open("simulation_data_y.csv","w")
print(obj.matrix_world)
print(obj.matrix_world[0][3])
print(obj.matrix_world[1][3])
print(obj.matrix_world[2][3])
random_frame = random.randint(1,40)
bpy.context.scene.frame_set(random_frame)
for i in range(random_frame,random_frame+20):
    bm = bmesh.new()
    
    #obj = bpy.data.objects['plane']
    bm.from_object( obj, depsgraph )
    for j,v in enumerate(bm.verts):
        #world_mat = obj.matrix_world
        #v = obj.matrix_world[0] * v.co  
        outfile.write( "vert:"+str(j)+","+str(obj.matrix_world[0][3]*v.co.x) + "," + str(obj.matrix_world[1][3]*v.co.y) + "," + str(obj.matrix_world[2][3]*v.co.z)+ "," )
        outfile.write("\n")
    outfile.write("\n")
    bm.free()
    bpy.context.view_layer.update()
    #print(obj.matrix_world[2][3])
print(sphere.dimensions)
outfile_y.write(str(sphere.matrix_world[0][3])+","+str(sphere.matrix_world[1][3])+","+str(sphere.matrix_world[2][3])+",")
outfile_y.write(sphere.dimensions)