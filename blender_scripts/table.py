import bpy

def clear_scene():
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete(use_global=False)

def create_table():
    """Build a simple table with a rectangular top and four cylindrical legs."""
    clear_scene()

    # Table top
    bpy.ops.mesh.primitive_cube_add(size=2, location=(0, 0, 1))
    top = bpy.context.active_object
    top.scale = (1.5, 1, 0.1)
    top.name = "TableTop"

    # Legs
    for x in (-1.3, 1.3):
        for y in (-0.8, 0.8):
            bpy.ops.mesh.primitive_cylinder_add(radius=0.05, depth=0.9, location=(x, y, 0.45))
            leg = bpy.context.active_object
            leg.name = f"Leg_{x}_{y}"

if __name__ == "__main__":
    create_table()
