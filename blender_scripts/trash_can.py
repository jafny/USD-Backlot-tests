import bpy

def clear_scene():
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete(use_global=False)

def create_trash_can():
    """Create a basic cylindrical trash can with lid and handles."""
    clear_scene()

    # Body
    bpy.ops.mesh.primitive_cylinder_add(radius=0.5, depth=1, location=(0, 0, 0.5))
    body = bpy.context.active_object
    body.name = "CanBody"

    # Lid
    bpy.ops.mesh.primitive_cylinder_add(radius=0.55, depth=0.1, location=(0, 0, 1.05))
    lid = bpy.context.active_object
    lid.name = "Lid"

    # Handles
    for x in (-0.6, 0.6):
        bpy.ops.mesh.primitive_cube_add(size=0.2, location=(x, 0, 0.9))
        handle = bpy.context.active_object
        handle.scale = (0.1, 0.05, 0.05)
        handle.name = f"Handle_{x}"

if __name__ == "__main__":
    create_trash_can()
