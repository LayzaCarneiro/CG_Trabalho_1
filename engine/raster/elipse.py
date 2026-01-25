from engine.framebuffer import set_pixel

def get_elipse_points(superficie, xc, yc, x, y, cor):
    set_pixel(superficie, xc + x, yc + y, cor)
    set_pixel(superficie, xc - x, yc + y, cor)
    set_pixel(superficie, xc + x, yc - y, cor)
    set_pixel(superficie, xc - x, yc - y, cor)

def draw_elipse(superficie, xc, yc, rx, ry, cor):
    x = 0
    y = ry

    rx2 = rx * rx
    ry2 = ry * ry

    dx = 2 * ry2 * x
    dy = 2 * rx2 * y

    # Região 1
    p1 = ry2 - (rx2 * ry) + (0.25 * rx2)

    while dx < dy:
        get_elipse_points(superficie, xc, yc, x, y, cor)

        x += 1
        dx += 2 * ry2

        if p1 < 0:
            p1 += ry2 + dx
        else:
            y -= 1
            dy -= 2 * rx2
            p1 += ry2 + dx - dy

    # Região 2
    p2 = (ry2 * (x + 0.5) * (x + 0.5)) + (rx2 * (y - 1) * (y - 1)) - (rx2 * ry2)

    while y >= 0:
        get_elipse_points(superficie, xc, yc, x, y, cor)

        y -= 1
        dy -= 2 * rx2

        if p2 > 0:
            p2 += rx2 - dy
        else:
            x += 1
            dx += 2 * ry2
            p2 += rx2 - dy + dx
