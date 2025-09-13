import bpy

def clear_scene():
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete(use_global=False)

def create_street_lamp():
    """Build a basic street lamp with a pole, arm, and lamp head."""
    clear_scene()

    # Vertical pole
    bpy.ops.mesh.primitive_cylinder_add(radius=0.05, depth=3, location=(0, 0, 1.5))
    pole = bpy.context.active_object
    pole.name = "Pole"

    # Horizontal arm
    bpy.ops.mesh.primitive_cylinder_add(radius=0.03, depth=0.8, location=(0.4, 0, 3), rotation=(0, 0, 1.5708))
    arm = bpy.context.active_object
    arm.name = "Arm"

    # Lamp head
    bpy.ops.mesh.primitive_uv_sphere_add(radius=0.12, location=(0.8, 0, 3))
    head = bpy.context.active_object
    head.name = "LampHead"

if __name__ == "__main__":
    create_street_lamp()
