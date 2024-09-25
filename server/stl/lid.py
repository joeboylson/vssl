from solid2 import cube, polygon, cylinder, sphere


clearance = 0.12
n_clearance = clearance * -1


def generate_lip_polygon(length=0, with_clearance=False):

    coordinates_no_clearance = [[0, 0], [0, 4], [2, 4]]
    coordinates_with_clearance = [
        [n_clearance, n_clearance],
        [n_clearance, 4 + clearance],
        [2 + clearance + 0.1, 4 + clearance],
        [clearance - 0.06, n_clearance],
    ]
    coords = coordinates_with_clearance if with_clearance else coordinates_no_clearance

    model = polygon(coords)
    model = model.linear_extrude(length)
    model = model.rotateX(90)
    model = model.translateY(length)

    return model


def generate_lip(
    length_x,
    length_y,
    length_z,
    wall_thickness,
    with_clearance=False,
    with_snaps=True,
):

    model = cube(0)

    left_right_length = length_y + wall_thickness + 1
    top_bottom_length = length_x + wall_thickness + 2

    left = generate_lip_polygon(left_right_length, with_clearance)

    right = generate_lip_polygon(left_right_length, with_clearance)
    right = right.rotateZ(180)

    top = generate_lip_polygon(top_bottom_length, with_clearance)
    top = top.rotateZ(-90)

    bottom = generate_lip_polygon(top_bottom_length, False)
    bottom = bottom.rotateZ(90)

    # translations
    left = left.translateX(-1)
    top = top.translateY(left_right_length)
    top = top.translateX(-1)
    right = right.translateX(top_bottom_length - 1)
    right = right.translateY(left_right_length)
    bottom = bottom.translateX(top_bottom_length - 1)

    if with_clearance:
        bottom = bottom.translateY(n_clearance)

    model = left + right + top - bottom
    model = model.translateZ(length_z - 1)

    if with_snaps:

        cylinder_size = 0.5 if with_clearance else 0.5 + clearance
        _snap_cube = cylinder(r=cylinder_size, h=2).scaleY(3)

        ty = 5
        tz = length_z + 1

        snap_left = _snap_cube
        snap_left = snap_left.translate(1, ty, tz)

        snap_right = _snap_cube
        snap_right = snap_right.translate(top_bottom_length - 3, ty, tz)

        model = model - snap_left - snap_right

    return model


def generate_lid(
    lid_length_x,
    lid_length_y,
    outer_wall_thickness,
    with_lid_inset=True,
    with_pull_tab=True,
):

    # dimensions
    x = lid_length_x
    y = lid_length_y
    z = 2

    # generate lid box
    lid = cube(x, y + outer_wall_thickness, z - clearance)
    lid = lid.translateY(outer_wall_thickness * -1)

    # generate lip cutout (for slanted corners)
    lip_cutout = generate_lip(
        x,
        y,
        0,
        wall_thickness=0,  # wall thickness is already accounted for in x, y calc
        with_clearance=True,
    )

    lip_cutout = lip_cutout.translateZ(-1)

    lid_inset = cube(0)
    if with_lid_inset:
        inset_amount = 10
        ix = x - inset_amount
        iy = y - inset_amount
        txy = inset_amount / 2
        tz = z - 1
        lid_inset = cube(ix, iy, z - clearance)
        lid_inset = lid_inset.translate(txy, txy, tz)

    pull_tab = cube(0)
    if with_pull_tab:
        h = 100
        r = 8
        tx = (lid_length_x / 2) + 0.25
        ty = 16
        tz = h / -2
        pull_tab = cylinder(h, r=r)
        pull_tab = pull_tab.translate(tx, ty, tz)

    model = lid - lip_cutout - lid_inset - pull_tab

    lid_position_x = (lid_length_x * -1) - 2 - outer_wall_thickness
    model = model.translateX(lid_position_x)

    # model = model.translate(0, 0, 2 + clearance)

    return model
