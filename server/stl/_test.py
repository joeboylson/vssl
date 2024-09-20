from solid2 import *
from generate_model import *


def main():

    slot_size_x = 11.5
    slot_size_y = 11.5
    slot_size_z = 30
    number_of_slots_x = 7
    number_of_slots_y = 9
    wall_thickness = 0.5
    slot_inset = 15
    include_pull_tab = False

    # PARAMS
    length_x = slot_size_x * number_of_slots_x + (wall_thickness * number_of_slots_x)
    length_y = slot_size_y * number_of_slots_y + (wall_thickness * number_of_slots_y)

    length_z = slot_size_z
    ### wall
    outer_wall_thickness = 1
    # base
    base_height = 1

    model = cube(0)

    slots = generate_slots(
        length_x,
        length_y,
        length_z - slot_inset,
        number_of_slots_x,
        number_of_slots_y,
        wall_thickness,
        base_height,
    )

    base = generate_base(length_x, length_y, wall_thickness, base_height)

    walls = generate_walls(
        length_x, length_y, length_z, wall_thickness, outer_wall_thickness, base_height
    )

    lip = generate_lip(
        length_x, length_y, length_z, wall_thickness, outer_wall_thickness
    )

    lid_assembly = generate_lid(
        length_x,
        length_y,
        length_z,
        wall_thickness,
        outer_wall_thickness,
        base_height,
        with_lid_cutout=False,
        with_pull_tab=False,
    ).render()

    slots_assembly = slots + base + walls + lip
    model = slots_assembly.color("red") + lid_assembly.color("blue")

    total_x = length_x + (outer_wall_thickness * 2) + 1
    total_y = length_y + (outer_wall_thickness * 2) + 1
    total_z = length_z + 4

    # model = model + square(180, center=True).translateY(80)

    model.save_as_scad()

    print(f"TOTAL_X: {total_x}mm")
    print(f"TOTAL_Y: {total_y}mm")
    print(f"TOTAL_Z: {total_z}mm")


main()
