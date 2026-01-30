# ═══════════════════════════════════════════════════════
# RASTERIZAÇÃO DE ELIPSES
# ═══════════════════════════════════════════════════════
# Implementação do algoritmo de rasterização de elipses
# (Requisito b - Primitivas de Rasterização: Elipse)
#
# Utiliza o algoritmo do ponto médio para elipses,
# dividido em duas regiões para maior precisão.
# ═══════════════════════════════════════════════════════

from engine.framebuffer import set_pixel

# ─── Plotagem de 4 Pontos Simétricos ───
def get_elipse_points(superficie, xc, yc, x, y, cor):
    """
    Aproveita a simetria da elipse para plotar 4 pontos de uma vez.
    
    A elipse possui simetria em relação aos eixos horizontal e vertical,
    permitindo plotar 4 pontos para cada cálculo.
    """
    set_pixel(superficie, xc + x, yc + y, cor)
    set_pixel(superficie, xc - x, yc + y, cor)
    set_pixel(superficie, xc + x, yc - y, cor)
    set_pixel(superficie, xc - x, yc - y, cor)

# ─── Algoritmo do Ponto Médio para Elipse ───
def draw_elipse(superficie, xc, yc, rx, ry, cor):
    """
    Desenha uma elipse usando o algoritmo do ponto médio.
    
    REQUISITO: (b) Primitivas de Rasterização - Elipse
    
    Características:
    - Divide o desenho em 2 regiões para precisão
    - Usa apenas aritmética inteira
    - Suporta elipses de qualquer proporção
    
    Args:
        xc, yc: Centro da elipse
        rx: Raio no eixo X
        ry: Raio no eixo Y
        cor: Cor da elipse
    
    Usado no jogo para: peixes, ondas, elementos decorativos.
    """
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
