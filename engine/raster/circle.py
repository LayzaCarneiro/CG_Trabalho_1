from engine.framebuffer import set_pixel

def get_circle_points(superficie, xc, yc, x, y, cor):
    set_pixel(superficie, xc + x, yc + y, cor)
    set_pixel(superficie, xc - x, yc + y, cor)
    set_pixel(superficie, xc + x, yc - y, cor)
    set_pixel(superficie, xc - x, yc - y, cor)
    set_pixel(superficie, xc + y, yc + x, cor)
    set_pixel(superficie, xc - y, yc + x, cor)
    set_pixel(superficie, xc + y, yc - x, cor)
    set_pixel(superficie, xc - y, yc - x, cor)

def draw_circle(superficie, xc, yc, raio, cor):
    x = 0
    y = raio
    d = 1 - raio

    get_circle_points(superficie, xc, yc, x, y, cor)

    while x < y:
        x += 1

        if d < 0:
            d += 2 * x + 1
        else:
            y -= 1
            d += 2 * (x - y) + 1

        get_circle_points(superficie, xc, yc, x, y, cor)
