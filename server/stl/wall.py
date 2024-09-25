from solid2 import cube


def generate_walls(length_x, length_y, length_z, outer_wall_thickness):

    owt = outer_wall_thickness
    lid_height = 2
    inner_bounds_height = length_z + 50

    wall_inner_bounds = cube(length_x, length_y, inner_bounds_height)
    wall_inner_bounds = wall_inner_bounds.translateZ(-10)

    wall_outer_bounds = cube(
        length_x + (owt * 2), length_y + (owt * 2), length_z + lid_height
    )

    wall_outer_bounds = wall_outer_bounds.translate((owt * -1), (owt * -1), 0)

    wall_lid_notch = cube(length_x, owt, lid_height)
    wall_lid_notch = wall_lid_notch.translate(0, (owt * -1), length_z)

    model = wall_outer_bounds - wall_inner_bounds - wall_lid_notch

    return model
