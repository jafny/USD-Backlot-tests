import bpy

def clear_scene():
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete(use_global=False)

def create_bench():
    """Build a simple park bench with seat, backrest, and four legs."""
    clear_scene()

    # Seat
    bpy.ops.mesh.primitive_cube_add(size=2, location=(0, 0, 0.5))
    seat = bpy.context.active_object
    seat.scale = (1.5, 0.3, 0.1)
    seat.name = "Seat"

    # Backrest
    bpy.ops.mesh.primitive_cube_add(size=2, location=(0, -0.4, 1.0))
    back = bpy.context.active_object
    back.scale = (1.5, 0.1, 0.5)
    back.name = "Backrest"

    # Legs
    for x in (-1.4, 1.4):
        for y in (-0.25, 0.25):
            bpy.ops.mesh.primitive_cube_add(size=1, location=(x, y, 0.25))
            leg = bpy.context.active_object
            leg.scale = (0.1, 0.1, 0.5)
            leg.name = f"Leg_{x}_{y}"

if __name__ == "__main__":
    create_bench()
