# ═══════════════════════════════════════════════════════════════
# ÍCONES DO HUD
# ═══════════════════════════════════════════════════════════════
# Ícones do HUD (pontuação e vidas).
#
# Demonstra os seguintes requisitos:
# - (a) set_pixel: ícones desenhados pixel a pixel
# - (b) Primitivas: polígonos (cauda do peixe)
# - (c) Preenchimento: scanline_fill na cauda
#
# Ícones:
# - Peixe: representa pontuação
# - X vermelho: representa vidas
# ═══════════════════════════════════════════════════════════════

import assets.colors as color
from engine.math.auxiliary import interpolar_cor
from engine.fill.scanline import scanline_fill
from engine.raster.line import desenhar_poligono
from app.scenes.auxiliary_functions import _set_pixel_scaled

def draw_fish_icon(superficie, x, y, tamanho=8, scale=1):
    """
    Desenha ícone de peixe para o HUD.
    
    REQUISITOS:
    - (a) set_pixel: corpo desenhado pixel a pixel
    - (b) Primitivas: desenhar_poligono na cauda
    - (c) Preenchimento: scanline_fill na cauda
    
    Args:
        superficie: pygame.Surface
        x, y: posição central
        tamanho: tamanho do ícone
        scale: fator de escala (2 = cada pixel vira bloco 2x2)
    """
    # Corpo pequeno (elipse)
    a = tamanho // 2
    b = tamanho // 3
    for dy in range(-b, b + 1):
        for dx in range(-a, a + 1):
            if a > 0 and b > 0:
                if (dx * dx) / (a * a) + (dy * dy) / (b * b) <= 1:
                    t = (dy + b) / (2 * b) if b > 0 else 0.5
                    if t < 0.5:
                        t_grad = t * 2
                    else:
                        t_grad = (1 - t) * 2
                    cor = interpolar_cor(color.FISH_BLUE, color.FISH_WHITE, t_grad)
                    _set_pixel_scaled(superficie, x, y, dx, dy, cor, scale)
    
    # Cauda
    cauda_pontos = [
        (x - a - 1, y),
        (x - a - 3, y - 2),
        (x - a - 3, y + 2)
    ]
    if scale == 1:
        scanline_fill(superficie, cauda_pontos, color.FISH_BLUE)
        desenhar_poligono(superficie, cauda_pontos, color.FISH_OUTLINE)
    else:
        cauda_esc = [(x + (px - x) * scale, y + (py - y) * scale) for px, py in cauda_pontos]
        scanline_fill(superficie, cauda_esc, color.FISH_BLUE)
        desenhar_poligono(superficie, cauda_esc, color.FISH_OUTLINE)


def draw_heart_icon(superficie, x, y, tamanho=6, scale=1):
    """
    Ícone de vida - desenha um X.
    scale=2 desenha cada pixel como bloco 2×2 (só set_pixel).
    """
    size = tamanho * 2
    thickness = 2  # Espessura das linhas do X
    
    for dy in range(size):
        for dx in range(size):
            # Diagonal principal (\)
            if abs(dx - dy) <= thickness:
                cor = (255, 100, 100)  # Vermelho
                _set_pixel_scaled(superficie, x, y, dx, dy, cor, scale)
            
            # Diagonal secundária (/)
            if abs(dx - (size - 1 - dy)) <= thickness:
                cor = (255, 100, 100)  # Vermelho
                _set_pixel_scaled(superficie, x, y, dx, dy, cor, scale)



