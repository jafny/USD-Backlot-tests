import bpy

def clear_scene():
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete(use_global=False)

def create_fire_hydrant():
    """Create a basic fire hydrant with body, cap, and nozzles."""
    clear_scene()

    # Base
    bpy.ops.mesh.primitive_cylinder_add(radius=0.35, depth=0.1, location=(0, 0, 0.05))
    base = bpy.context.active_object
    base.name = "Base"

    # Body
    bpy.ops.mesh.primitive_cylinder_add(radius=0.3, depth=1, location=(0, 0, 0.6))
    body = bpy.context.active_object
    body.name = "Body"

    # Cap
    bpy.ops.mesh.primitive_cylinder_add(radius=0.35, depth=0.2, location=(0, 0, 1.15))
    cap = bpy.context.active_object
    cap.name = "Cap"

    # Top nut
    bpy.ops.mesh.primitive_uv_sphere_add(radius=0.1, location=(0, 0, 1.3))
    top = bpy.context.active_object
    top.name = "TopNut"

    # Side nozzles
    for x in (-0.5, 0.5):
        bpy.ops.mesh.primitive_cylinder_add(radius=0.1, depth=0.4, location=(x, 0, 0.8))
        nozzle = bpy.context.active_object
        nozzle.rotation_euler[1] = 1.5708
        nozzle.name = f"Nozzle_{x}"

if __name__ == "__main__":
    create_fire_hydrant()
