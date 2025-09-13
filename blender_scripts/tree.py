import bpy

def clear_scene():
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete(use_global=False)

def create_tree():
    """Build a stylized tree using a cylinder trunk and cone foliage."""
    clear_scene()

    # Trunk
    bpy.ops.mesh.primitive_cylinder_add(radius=0.1, depth=2, location=(0, 0, 1))
    trunk = bpy.context.active_object
    trunk.name = "Trunk"

    # Foliage
    bpy.ops.mesh.primitive_cone_add(radius1=1, depth=2, location=(0, 0, 2.5))
    foliage = bpy.context.active_object
    foliage.name = "Foliage"

if __name__ == "__main__":
    create_tree()
