"""Optimize SK2 (Seoul Streets): keep all originals, deduplicate backup copies, resize textures."""
import bpy
import sys
import os

bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete(use_global=False)
bpy.ops.outliner.orphans_purge(do_local_ids=True, do_linked_ids=True, do_recursive=True)

fbx_path = sys.argv[-2]
output_glb = sys.argv[-1]

print(f"\n=== Importing FBX ===")
bpy.ops.import_scene.fbx(filepath=fbx_path)

# Remove backup copies and exact duplicates (.001, .002, _backup_01)
to_delete = []
for obj in bpy.data.objects:
    if obj.type == 'MESH':
        name = obj.name
        if '_backup_' in name or name.endswith(('.001', '.002', '.003', '.004', '.005', '.006', '.007', '.008', '.009', '.010')):
            to_delete.append(obj)

print(f"Removing {len(to_delete)} duplicates/backups")
for obj in to_delete:
    bpy.data.objects.remove(obj, do_unlink=True)

print(f"Remaining: {len([o for o in bpy.data.objects if o.type == 'MESH'])} objects")

# Resize textures to 1024 max
print(f"\n=== Resizing textures (max 1024) ===")
count = 0
for img in bpy.data.images:
    if img.size[0] > 1024 or img.size[1] > 1024:
        scale = 1024 / max(img.size[0], img.size[1])
        img.scale(int(img.size[0] * scale), int(img.size[1] * scale))
        count += 1
print(f"Resized {count} textures")

bpy.ops.outliner.orphans_purge(do_local_ids=True, do_linked_ids=True, do_recursive=True)

print("\n=== Post-optimization ===")
print(f"Objects: {len([o for o in bpy.data.objects if o.type == 'MESH'])}")
print(f"Materials: {len(bpy.data.materials)}")
print(f"Images: {len(bpy.data.images)}")
print(f"Polygons: {sum(len(m.polygons) for m in bpy.data.meshes):,}")

bpy.ops.object.select_all(action='SELECT')

print(f"\n=== Exporting ===")
bpy.ops.export_scene.gltf(
    filepath=output_glb,
    export_format='GLB',
    export_yup=True,
    export_apply=True,
    export_animations=False,
    export_draco_mesh_compression_enable=True,
    export_draco_mesh_compression_level=6,
    export_draco_position_quantization=12,
    export_draco_normal_quantization=8,
    export_draco_texcoord_quantization=10,
    export_image_format='JPEG',
    export_jpeg_quality=75
)

size_mb = os.path.getsize(output_glb) / (1024 * 1024)
print(f"\n=== DONE ===")
print(f"Output: {output_glb}")
print(f"Size: {size_mb:.1f} MB")
