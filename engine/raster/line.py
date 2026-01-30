# ═══════════════════════════════════════════════════════
# RASTERIZAÇÃO DE RETAS
# ═══════════════════════════════════════════════════════
# Implementação de algoritmos de rasterização de linhas
# (Requisito b - Primitivas de Rasterização: Linha)
#
# Algoritmos implementados:
# - DDA (Digital Differential Analyzer)
# - Bresenham (mais eficiente, usado no projeto)
# ═══════════════════════════════════════════════════════

from engine.framebuffer import set_pixel

# ─── Algoritmo DDA ───
def dda(superficie, x0, y0, x1, y1, cor):
    """
    Algoritmo DDA para rasterização de linhas.
    Usa aritmética de ponto flutuante.
    """
    dx = x1 - x0
    dy = y1 - y0

    passos = max(abs(dx), abs(dy))

    if passos == 0:
        set_pixel(superficie, x0, y0, cor)
        return

    x_inc = dx / passos
    y_inc = dy / passos

    x = x0
    y = y0

    for _ in range(passos + 1):
        set_pixel(superficie, round(x), round(y), cor)
        x += x_inc
        y += y_inc

# ─── Algoritmo de Bresenham ───
def bresenham(superficie, x0, y0, x1, y1, cor):
    """
    Algoritmo de Bresenham para rasterização de linhas.
    
    REQUISITO: (b) Primitivas de Rasterização - Linha
    
    Mais eficiente que DDA por usar apenas aritmética inteira.
    Usado em todo o projeto para desenho de linhas e polígonos.
    
    Características:
    - Apenas operações inteiras (sem ponto flutuante)
    - Suporta linhas em todas as direções
    - Trata casos especiais (linhas verticais/horizontais)
    """
    steep = abs(y1 - y0) > abs(x1 - x0)
    if steep:
        x0, y0 = y0, x0
        x1, y1 = y1, x1

    if x0 > x1:
        x0, x1 = x1, x0
        y0, y1 = y1, y0

    dx = x1 - x0
    dy = y1 - y0

    ystep = 1
    if dy < 0:
        ystep = -1
        dy = -dy

    # Bresenham clássico
    d = 2 * dy - dx
    incE = 2 * dy
    incNE = 2 * (dy - dx)

    x = x0
    y = y0

    while x <= x1:
        if steep:
            set_pixel(superficie, y, x, cor)
        else:
            set_pixel(superficie, x, y, cor)

        if d <= 0:
            d += incE
        else:
            d += incNE
            y += ystep

        x += 1

# ─── Desenho de Polígonos ───
def desenhar_poligono(tela, pontos, cor):
    """
    Desenha o contorno de um polígono conectando seus vértices.
    
    Usado para criar formas complexas no jogo (jangada, obstáculos, etc).
    Utiliza o algoritmo de Bresenham para cada aresta.
    """
    n = len(pontos)
    if n < 3:
        return

    for i in range(n):
        x0, y0 = pontos[i]
        x1, y1 = pontos[(i + 1) % n]
        bresenham(tela, x0, y0, x1, y1, cor)