from solid2 import *
from stl.slot import generate_slots
from stl.base import generate_base
from stl.wall import generate_walls
from stl.lid import generate_lid, generate_lip
from stl.utils import generate_starting_model


def generate_box_with_slots(
    length_x,
    length_y,
    length_z,
    slot_size_z,
    number_of_slots_x,
    number_of_slots_y,
    wall_thickness,
    outer_wall_thickness,
):

    base_height = 1

    base = generate_base(length_x, length_y, wall_thickness, base_height)

    walls = generate_walls(
        length_x, length_y, length_z, wall_thickness, outer_wall_thickness, base_height
    )

    slots = generate_slots(
        length_x,
        length_y,
        slot_size_z,
        number_of_slots_x,
        number_of_slots_y,
        wall_thickness,
        base_height,
    )

    lip = generate_lip(
        length_x, length_y, length_z, wall_thickness, outer_wall_thickness
    )

    model = base + walls + slots + lip

    return model


def generate_stl_model(
    slot_size_x,
    slot_size_y,
    slot_size_z,
    number_of_slots_x,
    number_of_slots_y,
    wall_thickness,
    wall_inset,
    with_lid_inset,
    with_pull_tab,
):

    set_global_fn(72)

    # PARAMS
    length_x = slot_size_x * number_of_slots_x + (wall_thickness * number_of_slots_x)
    length_y = slot_size_y * number_of_slots_y + (wall_thickness * number_of_slots_y)
    length_z = slot_size_z
    slot_size_z = length_z - wall_inset
    outer_wall_thickness = 1

    box_with_slots = generate_box_with_slots(
        length_x,
        length_y,
        length_z,
        slot_size_z,
        number_of_slots_x,
        number_of_slots_y,
        wall_thickness,
        outer_wall_thickness,
    )

    lid = generate_lid(
        length_x,
        length_y,
        length_z,
        wall_thickness,
        outer_wall_thickness,
        with_lid_inset,
        with_pull_tab,
    )

    return box_with_slots.color("red") + lid.color("blue")


def generate_fallback_cube():
    return generate_starting_model()
