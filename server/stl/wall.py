from solid2 import cube


def generate_walls(
    length_x, length_y, length_z, wall_thickness, outer_wall_thickness, base_height
):

    # generate a cube which is the size of the entire box
    ox = length_x + wall_thickness + outer_wall_thickness * 2
    oy = length_y + wall_thickness + outer_wall_thickness * 2
    oz = base_height + length_z
    otx = outer_wall_thickness * -1
    oty = outer_wall_thickness * -1
    wall_outer_bounds = cube(ox, oy, oz).translate(otx, oty, 0)

    # generate a cube which is the size of the box minus the intended wall thickness
    ix = ox - 4
    iy = oy - 4
    iz = oz + 10
    itx = (outer_wall_thickness * -1) + 2
    ity = (outer_wall_thickness * -1) + 2
    itz = -5
    wall_inner_bounds = cube(ix, iy, iz).translate(itx, ity, itz)

    # cut out the inner cube from the outer cube which will result in a box with
    # no bottom or top (bottom and top will be created later)
    return wall_outer_bounds - wall_inner_bounds
