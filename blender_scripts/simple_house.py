import bpy

def clear_scene():
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete(use_global=False)

def create_house():
    """Build a simple house with a cube base and pyramid roof."""
    clear_scene()

    # Base of the house
    bpy.ops.mesh.primitive_cube_add(size=2, location=(0, 0, 1))
    base = bpy.context.active_object
    base.scale = (2, 2, 1)
    base.name = "HouseBase"

    # Roof
    bpy.ops.mesh.primitive_cone_add(vertices=4, radius1=2.2, depth=1.5, location=(0, 0, 2.75))
    roof = bpy.context.active_object
    roof.name = "Roof"

if __name__ == "__main__":
    create_house()
