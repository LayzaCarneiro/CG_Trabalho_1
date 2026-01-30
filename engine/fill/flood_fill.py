# -*- coding: utf-8 -*-
# ═══════════════════════════════════════════════════════
# PREENCHIMENTO - FLOOD FILL
# ═══════════════════════════════════════════════════════
# Implementação do algoritmo Flood Fill iterativo
# (Requisito c - Preenchimento de Regiões: Flood Fill)
#
# Algoritmo baseado em pilha (DFS) que preenche áreas
# delimitadas por uma cor de borda específica.
# Utiliza conectividade 4-direcional (cima, baixo, esq, dir).
# ═══════════════════════════════════════════════════════

from engine.framebuffer import set_pixel

# ─── Flood Fill (4-conectado) ───
def flood_fill_iterativo(superficie, x, y, cor_preenchimento, cor_borda):
    """
    Preenche uma área delimitada por bordas com uma cor específica.
    
    REQUISITO: (c) Preenchimento de Regiões - Flood Fill
    
    Algoritmo:
    1. Inicia em um ponto (x, y)
    2. Preenche o pixel se não for borda ou já preenchido
    3. Adiciona vizinhos na pilha (4-direções)
    4. Repete até pilha vazia
    
    Características:
    - Iterativo (evita estouro de pilha)
    - 4-conectado (não preenche diagonais)
    - Respeita limites da superfície
    
    Usado na tela de abertura para preencher figuras desenhadas.    
    """
    
    """
    Preenche recursivamente uma área com cor, evitando ultrapassar bordas.

    Args:
        superficie (pygame.Surface): Superfície onde o preenchimento será feito.
        x (int): Coordenada x inicial do ponto de partida.
        y (int): Coordenada y inicial do ponto de partida.
        cor_preenchimento (tuple): Cor RGB usada para preencher a área.
        cor_borda (tuple): Cor RGB que delimita a área (não deve ser preenchida).

    Exemplo:
        flood_fill_iterativo(tela, 100, 50, (255, 0, 0), (0, 0, 0))
    """
    largura = superficie.get_width()
    altura = superficie.get_height()

    pilha = [(x, y)]

    while pilha:
        x, y = pilha.pop()

        if not (0 <= x < largura and 0 <= y < altura):
            continue

        cor_atual = superficie.get_at((x, y))[:3]

        if cor_atual == cor_borda or cor_atual == cor_preenchimento:
            continue

        set_pixel(superficie, x, y, cor_preenchimento)

        pilha.append((x + 1, y))
        pilha.append((x - 1, y))
        pilha.append((x, y + 1))
        pilha.append((x, y - 1))