from solid2 import *
from stl.slot import generate_slots
from stl.base import generate_base
from stl.wall import generate_walls
from stl.lid import generate_lid, generate_lip, generate_lip_polygon
from stl.utils import generate_starting_model


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

    base_height = 1
    outer_wall_thickness = 1

    # PARAMS
    length_x = slot_size_x * number_of_slots_x + (wall_thickness * number_of_slots_x)
    length_y = slot_size_y * number_of_slots_y + (wall_thickness * number_of_slots_y)
    length_z = slot_size_z
    slot_size_z = length_z

    total_length_x = length_x + wall_thickness
    total_length_y = length_y + wall_thickness
    total_length_z = length_z + base_height

    lip = generate_lip(
        length_x=length_x,
        length_y=length_y,
        length_z=length_z,
        wall_thickness=wall_thickness,
        with_clearance=False,
    )

    slots = generate_slots(
        base_height=base_height,
        length_x=length_x,
        length_y=length_y,
        length_z=slot_size_z,
        wall_inset=wall_inset,
        number_of_slots_x=number_of_slots_x,
        number_of_slots_y=number_of_slots_y,
        wall_thickness=wall_thickness,
    )

    lid = generate_lid(
        lid_length_x=total_length_x,
        lid_length_y=total_length_y,
        outer_wall_thickness=outer_wall_thickness,
        with_lid_inset=with_lid_inset,
        with_pull_tab=with_pull_tab,
    )

    walls = generate_walls(
        total_length_x, total_length_y, total_length_z, outer_wall_thickness
    )

    slots = slots.color("red")
    lip = lip.color("orange")
    lid = lid.render().color("yellow")
    walls = walls.color("green")
    base = generate_base(total_length_x, total_length_y, base_height).color("blue")

    model = slots + lip + lid + walls + base

    model = model.translateY((length_y / -2) - 1)
    model = model.translateX(2)

    return model


def generate_fallback_cube():
    return generate_starting_model()
