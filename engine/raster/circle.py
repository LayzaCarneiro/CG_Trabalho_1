# ═══════════════════════════════════════════════════════
# RASTERIZAÇÃO DE CIRCUNFERÊNCIAS
# ═══════════════════════════════════════════════════════
# Implementação do algoritmo de rasterização de círculos
# (Requisito b - Primitivas de Rasterização: Circunferência)
#
# Utiliza o algoritmo do ponto médio (Midpoint Circle Algorithm)
# baseado na simetria de 8 octantes do círculo.
# ═══════════════════════════════════════════════════════

from engine.framebuffer import set_pixel

# ─── Plotagem de 8 Pontos Simétricos ───
def get_circle_points(superficie, xc, yc, x, y, cor):
    """
    Aproveita a simetria do círculo para plotar 8 pontos de uma vez.
    
    Para cada ponto (x,y) calculado, plota os 8 pontos simétricos
    nos diferentes octantes do círculo.
    """
    set_pixel(superficie, xc + x, yc + y, cor)
    set_pixel(superficie, xc - x, yc + y, cor)
    set_pixel(superficie, xc + x, yc - y, cor)
    set_pixel(superficie, xc - x, yc - y, cor)
    set_pixel(superficie, xc + y, yc + x, cor)
    set_pixel(superficie, xc - y, yc + x, cor)
    set_pixel(superficie, xc + y, yc - x, cor)
    set_pixel(superficie, xc - y, yc - x, cor)

# ─── Algoritmo do Ponto Médio ───
def draw_circle(superficie, xc, yc, raio, cor):
    """
    Desenha uma circunferência usando o algoritmo do ponto médio.
    
    REQUISITO: (b) Primitivas de Rasterização - Circunferência
    
    Características:
    - Usa apenas aritmética inteira
    - Calcula apenas 1/8 do círculo e usa simetria
    - Eficiente para círculos de qualquer tamanho
    
    Usado no jogo para: sol, olhos de personagens, ícones, etc.
    """
    x = 0
    y = raio
    d = 1 - raio  # Variável de decisão

    get_circle_points(superficie, xc, yc, x, y, cor)

    while x < y:
        x += 1

        # Atualiza variável de decisão
        if d < 0:
            d += 2 * x + 1
        else:
            y -= 1
            d += 2 * (x - y) + 1

        get_circle_points(superficie, xc, yc, x, y, cor)
