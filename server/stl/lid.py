from solid2 import cube, polygon, cylinder


def generate_lip_polygon(with_clearance=False):

    clearance = 0.15
    coordinates_no_clearance = [[0, 0], [0, 4], [2, 4]]
    coordinates_with_clearance = [[0, 0], [0, 4], [2 + clearance, 4], [clearance, 0]]
    coords = coordinates_with_clearance if with_clearance else coordinates_no_clearance

    model = polygon(coords)
    model = model.linear_extrude(1)
    model = model.rotateX(90)
    model = model.translateY(1)

    return model


def generate_lip(
    length_x,
    length_y,
    length_z,
    wall_thickness,
    outer_wall_thickness,
    with_clearance=False,
):

    left = generate_lip_polygon(with_clearance)
    left = left.translateZ(length_z)
    left = left.scaleY(length_y + (outer_wall_thickness * 2) + wall_thickness)
    left = left.translateY(outer_wall_thickness * -1)
    left = left.translateX(outer_wall_thickness * -1)

    top = generate_lip_polygon()
    top = top.rotateZ(-90)
    top = top.translateZ(length_z)
    top = top.scaleX(length_x + (outer_wall_thickness * 2) + wall_thickness)
    top = top.translateX(outer_wall_thickness * -1)
    top = top.translateY(length_y + (outer_wall_thickness * 2) + wall_thickness - 1)

    right = left
    right = right.rotateZ(180)
    right = right.translateX(length_x + wall_thickness)
    right = right.translateY(length_y + wall_thickness)

    bottom = generate_lip_polygon()
    bottom = bottom.rotateZ(90)
    bottom = bottom.translateZ(length_z)
    bottom = bottom.scaleX(length_x + (outer_wall_thickness * 2) + wall_thickness)
    bottom = bottom.translateX(length_x + outer_wall_thickness + wall_thickness)
    bottom = bottom.translateY(outer_wall_thickness * -1)

    # attach all sides
    model = left + top + right - bottom
    model = model.translateZ(-1)

    return model


def generate_lid_inset(x, y, z, tx, ty, tz, with_lid_inset):

    if not with_lid_inset:
        return cube(0)

    inset_height = 1
    distance_from_edge = 10
    half_distance_from_edge = distance_from_edge / 2
    _x = x - distance_from_edge
    _y = y - distance_from_edge
    _tx = tx + half_distance_from_edge
    _ty = ty + half_distance_from_edge
    _tz = tz + inset_height

    model = cube(_x, _y, z)
    model = model.translate(_tx, _ty, _tz)
    return model


def generate_pull_tab(length_x, with_pull_tab):

    if not with_pull_tab:
        return cube(0)

    h = 100
    r = 8
    tx = (length_x / 2) + 0.25
    ty = 16
    tz = h / -2

    model = cylinder(h, r=r)
    model = model.translate(tx, ty, tz)

    return model


def generate_lid(
    length_x,
    length_y,
    length_z,
    wall_thickness,
    outer_wall_thickness,
    with_lid_inset=True,
    with_pull_tab=True,
):

    # dimensions
    x = length_x + (outer_wall_thickness * 2) + wall_thickness
    y = length_y + (outer_wall_thickness * 2) + wall_thickness
    z = 2

    # translation
    tx = outer_wall_thickness * -1
    ty = tx
    tz = 0

    # generate lid box
    lid = cube(x, y, z)
    lid = lid.translate(tx, ty, tz)

    # generate lip cutout (for slanted corners)
    lip_cutout = generate_lip(
        length_x,
        length_y,
        length_z,
        wall_thickness,
        outer_wall_thickness,
        with_clearance=True,
    )
    cutout_tx = length_z * -1
    lip_cutout = lip_cutout.translateZ(cutout_tx)

    lid_inset = generate_lid_inset(x, y, z, tx, ty, tz, with_lid_inset)
    pull_tab = generate_pull_tab(length_x, with_pull_tab)

    model = lid - lip_cutout - lid_inset - pull_tab

    # move the model over a bit from the box
    final_tx = (length_x * -1) - (5 + wall_thickness)
    model = model.translateX(final_tx)

    return model
