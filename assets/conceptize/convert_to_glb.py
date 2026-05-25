"""Blender Python: Convert FBX to GLB with Draco compression."""
import bpy
import sys
import os

# Clear default scene
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete(use_global=False)
bpy.ops.outliner.orphans_purge(do_local_ids=True, do_linked_ids=True, do_recursive=True)

fbx_path = sys.argv[-2]
output_glb = sys.argv[-1]

print(f"\n=== Importing FBX: {fbx_path} ===\n")
bpy.ops.import_scene.fbx(filepath=fbx_path)

print("\n=== Pre-export stats ===")
print(f"Objects: {len([o for o in bpy.data.objects if o.type == 'MESH'])}")
total_polys = sum(len(m.polygons) for m in bpy.data.meshes)
print(f"Total polygons: {total_polys:,}")

# Select all objects for export
bpy.ops.object.select_all(action='SELECT')

print(f"\n=== Exporting GLB with Draco: {output_glb} ===\n")

# Export with Draco compression for geometry + texture optimization
bpy.ops.export_scene.gltf(
    filepath=output_glb,
    export_format='GLB',
    export_yup=True,
    export_apply=True,           # Apply modifiers
    export_animations=False,     # No animations in city pack
    export_draco_mesh_compression_enable=True,
    export_draco_mesh_compression_level=6,  # 0-10, 6 = good balance
    export_draco_position_quantization=14,
    export_draco_normal_quantization=10,
    export_draco_texcoord_quantization=12,
    export_image_format='AUTO',  # JPEG for opaque, PNG for transparent
    export_texture_dir='',       # Embed textures in GLB
    export_jpeg_quality=85
)

size_mb = os.path.getsize(output_glb) / (1024 * 1024)
print(f"\n=== DONE ===")
print(f"Output: {output_glb}")
print(f"Size: {size_mb:.1f} MB")
