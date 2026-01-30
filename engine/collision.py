# -*- coding: utf-8 -*-
# ═══════════════════════════════════════════════════════
# DETECÇÃO DE COLISÕES
# ═══════════════════════════════════════════════════════
# Sistema de detecção de colisões para o gameplay.
#
# Utiliza AABB (Axis-Aligned Bounding Box) para verificar
# sobreposição entre retângulos e círculos.
#
# Usado para:
# - Colisão jangada × obstáculos (perde vida)
# - Colisão jangada × peixe (ganha ponto)
# ═══════════════════════════════════════════════════════


def check_collision_raft_obstacle(raft_x, raft_y, raft_w, raft_h, obs_x, obs_y, obs_radius):
    """
    Verifica colisão entre jangada (retângulo) e obstáculo (círculo).
    
    Algoritmo AABB (Axis-Aligned Bounding Box):
    - Aproxima o círculo como um retângulo
    - Verifica sobreposição de retângulos
    
    Usado quando: jangada colide com pedra/alga/coral
    Efeito: perde 1 vida e rotaciona 360°
    
    Args:
        raft_x, raft_y: canto superior esquerdo da jangada
        raft_w, raft_h: dimensões da jangada
        obs_x, obs_y: centro do obstáculo
        obs_radius: raio do obstáculo
    
    Returns:
        True se há colisão, False caso contrário
    """
    # Define limites do retângulo da jangada
    raft_left = raft_x
    raft_right = raft_x + raft_w
    raft_top = raft_y
    raft_bottom = raft_y + raft_h

    # Aproxima círculo como retângulo para AABB
    obs_left = obs_x - obs_radius
    obs_right = obs_x + obs_radius
    obs_top = obs_y - obs_radius
    obs_bottom = obs_y + obs_radius

    # Teste de sobreposição: se NÃO há separação, há colisão
    return not (
        raft_right < obs_left
        or raft_left > obs_right
        or raft_bottom < obs_top
        or raft_top > obs_bottom
    )


def check_collision_raft_fish(raft_x, raft_y, fish_x, fish_y):
    """
    Verifica colisão entre jangada e peixe (ambos retângulos).
    
    Algoritmo AABB para retângulos:
    - Calcula limites de cada objeto
    - Verifica se há sobreposição nos dois eixos
    
    Usado quando: jangada captura peixe
    Efeito: +1 ponto, peixe reaparece em nova posição
    
    Args:
        raft_x, raft_y: canto superior esquerdo da jangada
        fish_x, fish_y: centro do peixe
    
    Returns:
        True se há colisão, False caso contrário
    """
    # Dimensões fixas da jangada
    raft_w = 50
    raft_h = 85  # proa (15) + corpo (70)
    raft_left = raft_x
    raft_top = raft_y
    raft_right = raft_x + raft_w
    raft_bottom = raft_top + raft_h
    
    # Dimensões fixas do peixe
    fish_w = 28  # corpo + cauda + barbatanas
    fish_h = 12
    fish_left = fish_x - fish_w // 2
    fish_right = fish_x + fish_w // 2
    fish_top = fish_y - fish_h // 2
    fish_bottom = fish_y + fish_h // 2
    
    # Teste AABB: se não há separação, há colisão
    return not (raft_right < fish_left or 
                raft_left > fish_right or 
                raft_bottom < fish_top or 
                raft_top > fish_bottom)

