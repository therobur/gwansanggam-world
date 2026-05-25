"""Blender Python: Inspect FBX contents."""
import bpy
import sys
import os

# Clear default scene
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete(use_global=False)
bpy.ops.outliner.orphans_purge(do_local_ids=True, do_linked_ids=True, do_recursive=True)

fbx_path = sys.argv[-1]
print(f"\n=== Importing FBX: {fbx_path} ===\n")

bpy.ops.import_scene.fbx(filepath=fbx_path)

print("\n=== SCENE STATISTICS ===")
objects = bpy.data.objects
meshes = bpy.data.meshes
materials = bpy.data.materials
images = bpy.data.images

print(f"Total objects: {len(objects)}")
print(f"Mesh objects: {len([o for o in objects if o.type == 'MESH'])}")
print(f"Empty/group objects: {len([o for o in objects if o.type == 'EMPTY'])}")
print(f"Total meshes: {len(meshes)}")
print(f"Total materials: {len(materials)}")
print(f"Total images/textures: {len(images)}")

# Total polygon count
total_polys = sum(len(m.polygons) for m in meshes)
print(f"Total polygons: {total_polys:,}")

# Bounding box of entire scene
import mathutils
min_co = mathutils.Vector((float('inf'),)*3)
max_co = mathutils.Vector((float('-inf'),)*3)
for obj in objects:
    if obj.type == 'MESH':
        for v in obj.bound_box:
            world_v = obj.matrix_world @ mathutils.Vector(v)
            for i in range(3):
                min_co[i] = min(min_co[i], world_v[i])
                max_co[i] = max(max_co[i], world_v[i])

size = max_co - min_co
print(f"Scene bounds X: {min_co[0]:.2f} to {max_co[0]:.2f} (size {size[0]:.2f})")
print(f"Scene bounds Y: {min_co[1]:.2f} to {max_co[1]:.2f} (size {size[1]:.2f})")
print(f"Scene bounds Z: {min_co[2]:.2f} to {max_co[2]:.2f} (size {size[2]:.2f})")

# Top 30 largest meshes
mesh_sizes = []
for obj in objects:
    if obj.type == 'MESH' and obj.data:
        polys = len(obj.data.polygons)
        mesh_sizes.append((obj.name, polys))
mesh_sizes.sort(key=lambda x: -x[1])

print("\n=== TOP 30 LARGEST OBJECTS ===")
for name, polys in mesh_sizes[:30]:
    print(f"  {polys:>8,} polys · {name}")

print(f"\n=== TOTAL UNIQUE OBJECTS: {len([o for o in objects if o.type == 'MESH'])} ===")
