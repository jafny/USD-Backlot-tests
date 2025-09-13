import bpy

def clear_scene():
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete(use_global=False)

def create_mailbox():
    """Create a simple mailbox on a post."""
    clear_scene()

    # Post
    bpy.ops.mesh.primitive_cylinder_add(radius=0.1, depth=2, location=(0, 0, 1))
    post = bpy.context.active_object
    post.name = "Post"

    # Box body
    bpy.ops.mesh.primitive_cube_add(size=1, location=(0, 0.4, 1.8))
    body = bpy.context.active_object
    body.scale = (0.5, 0.4, 0.3)
    body.name = "Box"

    # Rounded top
    bpy.ops.mesh.primitive_cylinder_add(radius=0.5, depth=0.8, location=(0, 0.4, 2.1))
    top = bpy.context.active_object
    top.rotation_euler[0] = 1.5708
    top.scale = (1, 1, 0.6)
    top.name = "Top"

if __name__ == "__main__":
    create_mailbox()
