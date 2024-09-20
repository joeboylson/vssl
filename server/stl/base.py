from solid2 import cube


def generate_base(length_x, length_y, wall_thickness, base_height):
    _x = length_x + wall_thickness
    _y = length_y + wall_thickness
    return cube(_x, _y, base_height)
