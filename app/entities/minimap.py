# ═══════════════════════════════════════════════════════════════
# MINIMAPA
# ═══════════════════════════════════════════════════════════════
# Sistema de minimapa no canto superior direito.
#
# Demonstra os seguintes requisitos:
# - (a) set_pixel: todo o desenho usa apenas set_pixel
# - (f) Viewport: mostra área visível da câmera no mundo
# - Visualização top-down do mundo inteiro em escala reduzida
#
# Elementos exibidos:
# - Retângulo branco: viewport (área da câmera)
# - Quadrado verde: jangada (jogador)
# - Ponto azul: peixe
# - Pontos cinza: obstáculos
# ═══════════════════════════════════════════════════════════════

from engine.framebuffer import set_pixel
import assets.colors as color

def draw_minimap(
    superficie,
    raft_x, raft_y,
    fish_x, fish_y,
    obstaculos,
    camera_x, camera_y,
    WORLD_WIDTH, WORLD_HEIGHT,
    WIDTH, HEIGHT
):
    """
    Desenha o minimapa com viewport, jogador, peixe e obstáculos.
    
    REQUISITOS:
    - (a) set_pixel: todo o desenho pixel a pixel
    - (f) Viewport: retângulo branco mostra área visível da câmera
    
    O minimapa exibe o mundo inteiro em escala reduzida (180x180px)
    e marca a posição da viewport atual com um retângulo branco.
    
    Args:
        superficie: pygame.Surface
        raft_x, raft_y: posição da jangada no mundo
        fish_x, fish_y: posição do peixe no mundo
        obstaculos: lista de tuplas (x, y, raio, tipo)
        camera_x, camera_y: posição da câmera no mundo
        WORLD_WIDTH, WORLD_HEIGHT: dimensões do mundo
        WIDTH, HEIGHT: dimensões da viewport (tela)
    """
    # Tamanho do minimapa
    MAP_W = 180
    MAP_H = 180
    MAP_X = WIDTH - MAP_W - 15
    MAP_Y = 15

    # Fundo
    for y in range(MAP_H):
        for x in range(MAP_W):
            set_pixel(superficie, MAP_X + x, MAP_Y + y, (20, 40, 60))

    # Escala mundo → minimapa
    sx = MAP_W / WORLD_WIDTH
    sy = MAP_H / WORLD_HEIGHT

    # ===== VIEWPORT (retângulo da câmera) =====
    vx = int(camera_x * sx)
    vy = int(camera_y * sy)
    vw = int(WIDTH * sx)
    vh = int(HEIGHT * sy)

    # Contorno do viewport
    for i in range(vw):
        set_pixel(superficie, MAP_X + vx + i, MAP_Y + vy, (255, 255, 255))
        set_pixel(superficie, MAP_X + vx + i, MAP_Y + vy + vh, (255, 255, 255))

    for i in range(vh):
        set_pixel(superficie, MAP_X + vx, MAP_Y + vy + i, (255, 255, 255))
        set_pixel(superficie, MAP_X + vx + vw, MAP_Y + vy + i, (255, 255, 255))

    # ===== PEIXE =====
    px = int(fish_x * sx)
    py = int(fish_y * sy)
    set_pixel(superficie, MAP_X + px, MAP_Y + py, color.FISH_BLUE)

    # ===== OBSTÁCULOS =====
    for obs in obstaculos:
        ox = int(obs[0] * sx)
        oy = int(obs[1] * sy)
        set_pixel(superficie, MAP_X + ox, MAP_Y + oy, (120, 120, 120))

    # ===== JANGADA (PLAYER) =====
    rx = int(raft_x * sx)
    ry = int(raft_y * sy)

    for dy in range(-2, 3):
        for dx in range(-2, 3):
            set_pixel(
                superficie,
                MAP_X + rx + dx,
                MAP_Y + ry + dy,
                (255, 255, 255)
            )

