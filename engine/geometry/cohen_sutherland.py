# ═══════════════════════════════════════════════════════
# RECORTE DE LINHAS - COHEN-SUTHERLAND
# ═══════════════════════════════════════════════════════
# Implementação do algoritmo de clipping Cohen-Sutherland
# (Requisito g - Recorte de Cohen-Sutherland)
#
# Recorta linhas para exibir apenas a parte visível
# dentro de uma janela/viewport retangular.
#
# Utiliza códigos de região (4 bits) para determinar
# rapidamente se uma linha está dentro, fora ou atravessando.
# ═══════════════════════════════════════════════════════

from engine.raster.line import bresenham

# ─── Códigos de Região (4 bits) ───
INSIDE = 0   # 0000: Dentro da área de recorte
LEFT   = 1   # 0001: Fora à esquerda
RIGHT  = 2   # 0010: Fora à direita
BOTTOM = 4   # 0100: Fora abaixo
TOP    = 8   # 1000: Fora acima

def codigo_regiao(x, y, xmin, ymin, xmax, ymax):
    """
    Calcula o código de região de um ponto (4 bits).
    
    REQUISITO: (g) Recorte de Cohen-Sutherland
    
    O código indica em qual região o ponto está:
    - INSIDE (0000): dentro do retângulo
    - LEFT, RIGHT, TOP, BOTTOM: fora em cada direção
    - Combinações (ex: TOP|LEFT): fora em diagonal
    
    Args:
        x, y: coordenadas do ponto
        xmin, ymin, xmax, ymax: limites da janela
    
    Returns:
        código de região (bitmask de 4 bits)
    """
    code = INSIDE
    if x < xmin: code |= LEFT
    elif x > xmax: code |= RIGHT
    if y < ymin: code |= TOP      # y cresce para baixo
    elif y > ymax: code |= BOTTOM
    return code

def cohen_sutherland(x0, y0, x1, y1, xmin, ymin, xmax, ymax):
    """
    Algoritmo de recorte Cohen-Sutherland para linhas.
    
    REQUISITO: (g) Recorte de Cohen-Sutherland (Clipping)
    
    Recorta uma linha contra uma janela retangular.
    
    Casos:
    1. Ambos pontos dentro → aceita totalmente
    2. Ambos pontos na mesma região fora → rejeita totalmente
    3. Linha atravessa janela → recorta recursivamente
    
    Algoritmo iterativo:
    - Calcula códigos de região dos dois pontos
    - Se ambos INSIDE → aceita linha completa
    - Se têm bits em comum fora → rejeita (não cruza janela)
    - Senão, recorta o ponto externo na borda e recalcula
    
    Args:
        x0, y0, x1, y1: coordenadas da linha
        xmin, ymin, xmax, ymax: retângulo de recorte

    Returns:
        tuple:
            - bool: True se a linha (ou parte dela) é visível
            - x0, y0, x1, y1: coordenadas da linha recortada (ou None se fora)
    """
    c0 = codigo_regiao(x0, y0, xmin, ymin, xmax, ymax)
    c1 = codigo_regiao(x1, y1, xmin, ymin, xmax, ymax)

    while True:
        # Caso 1: Ambos dentro (c0 | c1 == 0)
        if not (c0 | c1):
            return True, x0, y0, x1, y1

        # Caso 2: Ambos fora na mesma direção (c0 & c1 != 0)
        if c0 & c1:
            return False, None, None, None, None

        # Caso 3: Recortar ponto externo
        c_out = c0 if c0 else c1

        # Calcula intersecção com a borda
        if c_out & TOP:
            x = x0 + (x1 - x0) * (ymin - y0) / (y1 - y0)
            y = ymin
        elif c_out & BOTTOM:
            x = x0 + (x1 - x0) * (ymax - y0) / (y1 - y0)
            y = ymax
        elif c_out & RIGHT:
            y = y0 + (y1 - y0) * (xmax - x0) / (x1 - x0)
            x = xmax
        elif c_out & LEFT:
            y = y0 + (y1 - y0) * (xmin - x0) / (x1 - x0)
            x = xmin

        # Atualiza o ponto e recalcula código
        if c_out == c0:
            x0, y0 = x, y
            c0 = codigo_regiao(x0, y0, xmin, ymin, xmax, ymax)
        else:
            x1, y1 = x, y
            c1 = codigo_regiao(x1, y1, xmin, ymin, xmax, ymax)


# ─── Funções de Desenho com Clipping ───
def draw_line(superficie, x0, y0, x1, y1, color, viewport=None):
    """
    Desenha uma linha com recorte opcional.
    
    Se viewport é fornecido, aplica Cohen-Sutherland antes de desenhar.
    Caso contrário, desenha a linha completa sem recorte.
    
    Usado no jogo para: viewport do minimapa, linhas da jangada.
    
    Args:
        superficie: pygame.Surface onde desenhar
        x0, y0, x1, y1: coordenadas da linha
        color: cor da linha (R, G, B)
        viewport: tupla (xmin, ymin, largura, altura) ou None
    """
    if viewport:
        xmin, ymin, w, h = viewport
        xmax = xmin + w
        ymax = ymin + h

        visible, cx0, cy0, cx1, cy1 = cohen_sutherland(
            x0, y0, x1, y1,
            xmin, ymin,
            xmax, ymax
        )

        if not visible:
            return  # linha totalmente fora

        x0, y0, x1, y1 = cx0, cy0, cx1, cy1

    bresenham(superficie, x0, y0, x1, y1, color)


def draw_line_clipped(tela, x0, y0, x1, y1, cor, viewport):
    """
    Wrapper para desenhar linha com clipping (sempre aplica recorte).
    
    REQUISITO: (g) Recorte de Cohen-Sutherland
    
    Usado quando: garantir que linhas não saiam da viewport (minimapa).
    
    Args:
        tela: pygame.Surface onde desenhar
        x0, y0, x1, y1: coordenadas da linha
        cor: cor da linha
        viewport: tupla (xmin, ymin, xmax, ymax) definindo o retângulo de recorte
    """
    xmin, ymin, xmax, ymax = viewport
    visivel, cx0, cy0, cx1, cy1 = cohen_sutherland(x0, y0, x1, y1, xmin, ymin, xmax, ymax)
    if not visivel:
        return
    bresenham(tela, cx0, cy0, cx1, cy1, cor)