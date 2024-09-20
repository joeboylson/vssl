from solid2 import *


def generate_steps(start, end, num_steps):
    if num_steps < 2:
        raise ValueError("Number of steps must be at least 2.")

    step_size = (end - start) / (num_steps - 1)
    return [start + i * step_size for i in range(num_steps)]


def generate_slots(
    length_x,
    length_y,
    length_z,
    number_of_slots_x,
    number_of_slots_y,
    wall_thickness,
    base_height,
):
    _model = cube(0)
    x_slots = generate_steps(0, length_x, number_of_slots_x + 1)
    y_slots = generate_steps(0, length_y, number_of_slots_y + 1)

    for x in x_slots:
        _model = _model + cube(
            wall_thickness, length_y + wall_thickness, length_z
        ).translateX(x).translateZ(base_height)

    for y in y_slots:
        _model = _model + cube(
            length_x + wall_thickness, wall_thickness, length_z
        ).translateY(y).translateZ(base_height)

    return _model


def generate_base(length_x, length_y, wall_thickness, base_height):
    _model = cube(length_x + wall_thickness, length_y + wall_thickness, base_height)
    return _model


def generate_walls(
    length_x, length_y, length_z, wall_thickness, outer_wall_thickness, base_height
):

    ox = length_x + wall_thickness + outer_wall_thickness * 2
    oy = length_y + wall_thickness + outer_wall_thickness * 2
    oz = base_height + length_z
    otx = outer_wall_thickness * -1
    oty = outer_wall_thickness * -1

    _wall_outer = cube(ox, oy, oz).translate(otx, oty, 0)

    ix = ox - 4
    iy = oy - 4
    iz = oz + 10
    itx = (outer_wall_thickness * -1) + 2
    ity = (outer_wall_thickness * -1) + 2
    itz = -5

    _wall_inner = cube(ix, iy, iz).translate(itx, ity, itz)

    return _wall_outer - _wall_inner


def generate_lid_lip(with_clearance=False):

    clearance = 0.18
    coordinates_no_clearance = [[0, 0], [0, 4], [2, 4]]
    coordinates_with_clearance = [[0, 0], [0, 4], [2 + clearance, 4], [clearance, 0]]
    coords = coordinates_with_clearance if with_clearance else coordinates_no_clearance
    _model = polygon(coords).linear_extrude(1).rotateX(90).translateY(1)

    return _model


def generate_lip(
    length_x,
    length_y,
    length_z,
    wall_thickness,
    outer_wall_thickness,
    with_clearance=False,
):

    left = (cube(0) + generate_lid_lip(with_clearance)).render()
    left = left.translateZ(length_z)
    left = left.scaleY(length_y + (outer_wall_thickness * 2) + wall_thickness)
    left = left.translateY(outer_wall_thickness * -1)
    left = left.translateX(outer_wall_thickness * -1)

    top = (cube(0) + generate_lid_lip()).render()
    top = (cube(0) + top.rotateZ(-90)).render()
    top = top.translateZ(length_z)
    top = top.scaleX(length_x + (outer_wall_thickness * 2) + wall_thickness)
    top = top.translateX(outer_wall_thickness * -1)
    top = top.translateY(length_y + (outer_wall_thickness * 2) + wall_thickness - 1)

    right = (cube(0) + left).render()
    right = right.rotateZ(180)
    right = right.translateX(length_x + wall_thickness)
    right = right.translateY(length_y + wall_thickness)

    bottom = (cube(0) + generate_lid_lip()).render()
    bottom = (cube(0) + bottom.rotateZ(90)).render()
    bottom = bottom.translateZ(length_z)
    bottom = bottom.scaleX(length_x + (outer_wall_thickness * 2) + wall_thickness)
    bottom = bottom.translateX(length_x + outer_wall_thickness + wall_thickness)
    bottom = bottom.translateY(outer_wall_thickness * -1)

    assembly = left + top + right - bottom
    assembly = assembly.translateZ(-1)
    return assembly


def generate_lid(
    length_x,
    length_y,
    length_z,
    wall_thickness,
    outer_wall_thickness,
    base_height,
    with_lid_cutout=True,
    with_pull_tab=True,
):

    x = length_x + (outer_wall_thickness * 2) + wall_thickness
    y = length_y + (outer_wall_thickness * 2) + wall_thickness
    z = 2

    ltx = outer_wall_thickness * -1
    lty = ltx
    ltz = length_z + 2

    _lid = cube(x, y, z)
    _lid = _lid.translate(ltx, lty, ltz)

    _lid_cutout = cube(0)
    if with_lid_cutout:
        _lid_cutout_factor = 10
        _lid_cutout = cube(x - _lid_cutout_factor, y - _lid_cutout_factor, z)
        _lid_cutout = _lid_cutout.translate(
            ltx + (_lid_cutout_factor / 2), lty + (_lid_cutout_factor / 2), ltz + 1
        )

    _lip = generate_lip(
        length_x,
        length_y,
        length_z,
        wall_thickness,
        outer_wall_thickness,
        with_clearance=True,
    )

    _lip = _lip.translateZ(1)

    # pull tab
    _pull_tab = cylinder(0, r=0)
    if with_pull_tab:
        _pull_tab = cylinder(100, r=8).translateX((length_x / 2) + 0.25).translateY(16)

    _model = (_lid - _lip - _pull_tab - _lid_cutout).render()

    _model = _model.translateX((length_x * -1) - (8 + wall_thickness))
    _model = _model.translateZ((length_z * -1) - base_height - 1)

    return _model


def generate_stl_model(
    slot_size_x,
    slot_size_y,
    slot_size_z,
    number_of_slots_x,
    number_of_slots_y,
    wall_thickness,
    wall_inset,
):

    set_global_fn(72)

    # PARAMS
    length_x = slot_size_x * number_of_slots_x + (wall_thickness * number_of_slots_x)
    length_y = slot_size_y * number_of_slots_y + (wall_thickness * number_of_slots_y)

    length_z = slot_size_z
    slot_size_z = length_z - wall_inset

    outer_wall_thickness = 1
    base_height = 1

    with_lid_cutout = True
    with_pull_tab = True

    model = cube(0)

    slots = generate_slots(
        length_x,
        length_y,
        slot_size_z,
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
        with_lid_cutout,
        with_pull_tab,
    )

    slots_assembly = slots + base + walls + lip
    model = slots_assembly.color("red") + lid_assembly.color("blue")

    return model


def generate_fallback_cube():
    return cube(0)
