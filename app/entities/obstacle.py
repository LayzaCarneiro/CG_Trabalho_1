# ═══════════════════════════════════════════════════════════════
# OBSTÁCULOS DO JOGO
# ═══════════════════════════════════════════════════════════════
# Obstáculos que o jogador deve desviar.
#
# Demonstra o seguinte requisito:
# - (a) set_pixel: todo o desenho usa apenas set_pixel
#
# Tipos de obstáculos:
# 1. Rocha (cinza com gradiente radial)
# 2. Alga marinha (verde ondulante)
# 3. Coral (laranja ramificado)
# ═══════════════════════════════════════════════════════════════

from engine.framebuffer import set_pixel

def draw_obstacle(superficie, x, y, tamanho=14, tipo=None):
    """
    Desenha um obstáculo (dispatcher para os 3 tipos).
    
    REQUISITO: (a) Acesso direto à memória de vídeo (set_pixel)
    
    Todos os pixels são desenhados diretamente usando set_pixel,
    sem uso de primitivas de alto nível do pygame.
    
    Args:
        superficie: pygame.Surface
        x, y: posição central do obstáculo
        tamanho: raio aproximado do obstáculo
        tipo: tipo de obstáculo (0=rocha, 1=alga, 2=coral)
    """
    # Se tipo não for especificado, usa rocha (padrão)
    if tipo is None:
        tipo = 0
    
    if tipo == 0:
        # Rocha (cinza)
        draw_rock(superficie, x, y, tamanho)
    elif tipo == 1:
        # Alga (verde)
        draw_seaweed(superficie, x, y, tamanho)
    else:
        # Coral (laranja)
        draw_coral(superficie, x, y, tamanho)


def draw_rock(superficie, x, y, tamanho=14):
    """
    Desenha uma rocha com gradiente radial para volume.
    
    REQUISITO: (a) set_pixel direto
    
    Técnica: gradiente radial baseado em distância euclidiana.
    Efeito visual: rocha com volume (claro no centro, escuro nas bordas).
    """
    for dy in range(-tamanho, tamanho + 1):
        for dx in range(-tamanho, tamanho + 1):
            dist = dx*dx + dy*dy
            if dist <= tamanho*tamanho:
                # Gradiente radial para volume
                intensidade = 1.0 - (dist / (tamanho*tamanho))
                # Cinza claro no centro, cinza escuro nas bordas
                base_cor = int(100 + intensidade * 30)
                cor = (base_cor, base_cor, base_cor + 10)
                set_pixel(superficie, x + dx, y + dy, cor)
            elif dist <= (tamanho+2)*(tamanho+2):
                # Contorno mais escuro
                set_pixel(superficie, x + dx, y + dy, (40, 40, 50))


def draw_seaweed(superficie, x, y, tamanho=14):
    """
    Desenha alga marinha ondulante com padrão de listras.
    
    REQUISITO: (a) set_pixel direto
    
    Técnica: forma elíptica com largura variável usando sin().
    Efeito visual: alga com movimento/ondulação estática.
    """
    import math
    for dy in range(-tamanho, tamanho + 1):
        for dx in range(-tamanho, tamanho + 1):
            # Forma ondulante (elipse horizontal com variação)
            largura = tamanho + int(3 * math.sin(dy * 0.3))
            altura = int(tamanho * 0.8)
            
            if abs(dy) <= altura and abs(dx) <= largura//2:
                # Verde variado com padrão
                verde_base = 150 - abs(dx) * 5
                cor = (40, verde_base, 80)
                
                # Padrão de listras verticais
                if dx % 3 == 0:
                    cor = (60, verde_base + 30, 100)
                
                set_pixel(superficie, x + dx, y + dy, cor)
            elif abs(dx) <= largura//2 and abs(dy) <= altura + 2:
                # Contorno verde mais escuro
                set_pixel(superficie, x + dx, y + dy, (20, 80, 50))


def draw_coral(superficie, x, y, tamanho=14):
    """
    Desenha coral ramificado em forma de árvore.
    
    REQUISITO: (a) set_pixel direto
    
    Técnica: tronco central + ramificações diagonais.
    Efeito visual: estrutura orgânica ramificada.
    """
    import math
    for dy in range(-tamanho, tamanho + 1):
        for dx in range(-tamanho, tamanho + 1):
            # Tronco principal (centro)
            if abs(dx) <= 2 and dy >= -tamanho:
                cor = (200, 100, 40)
                set_pixel(superficie, x + dx, y + dy, cor)
            
            # Ramificações diagonais (padrão coral)
            elif abs(dy) < tamanho:
                # Lado esquerdo
                if dx <= -3 and dx >= -(tamanho//2) and dy >= (dx // 2) - 2:
                    dist_ramo = abs(dx) + abs(dy)
                    if dist_ramo < tamanho:
                        intensidade = 1.0 - (dist_ramo / tamanho)
                        cor_val = int(200 - intensidade * 50)
                        cor = (cor_val, int(100 + intensidade * 30), int(40 + intensidade * 20))
                        set_pixel(superficie, x + dx, y + dy, cor)
                
                # Lado direito
                elif dx >= 3 and dx <= (tamanho//2) and dy >= (-dx // 2) - 2:
                    dist_ramo = abs(dx) + abs(dy)
                    if dist_ramo < tamanho:
                        intensidade = 1.0 - (dist_ramo / tamanho)
                        cor_val = int(200 - intensidade * 50)
                        cor = (cor_val, int(100 + intensidade * 30), int(40 + intensidade * 20))
                        set_pixel(superficie, x + dx, y + dy, cor)
