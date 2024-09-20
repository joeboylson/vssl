from solid2 import cube
from stl.utils import generate_steps, generate_starting_model


def generate_slots(
    length_x,
    length_y,
    length_z,
    number_of_slots_x,
    number_of_slots_y,
    wall_thickness,
    base_height,
):
    model = generate_starting_model()

    x_slots = generate_steps(0, length_x, number_of_slots_x + 1)
    y_slots = generate_steps(0, length_y, number_of_slots_y + 1)

    for x in x_slots:
        _y = length_y + wall_thickness
        slot = cube(wall_thickness, _y, length_z)
        slot = slot.translateX(x)
        slot = slot.translateZ(base_height)
        model = model + slot

    for y in y_slots:
        _x = length_x + wall_thickness
        slot = cube(_x, wall_thickness, length_z)
        slot = slot.translateY(y)
        slot = slot.translateZ(base_height)
        model = model + slot

    return model
