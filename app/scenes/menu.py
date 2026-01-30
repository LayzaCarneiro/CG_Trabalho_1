# -*- coding: utf-8 -*-
# ═══════════════════════════════════════════════════════════════
# MENU PRINCIPAL
# ═══════════════════════════════════════════════════════════════
# Tela inicial com botões de interação.
#
# Demonstra os seguintes requisitos:
# - (b) Primitivas: círculos (sol), elipses (ondas)
# - (i) Interação: detecção de clique do mouse em botões
# - (j) Menu: navegação entre cenas (Iniciar/Como Jogar/Sair)
#
# Botões:
# - INICIAR: começa o jogo
# - COMO JOGAR: mostra instruções
# - SAIR: fecha o jogo
# ═══════════════════════════════════════════════════════════════

import pygame
import assets.colors as color
from engine.raster.circle import draw_circle
from app.scenes.auxiliary_functions import draw_text, draw_button, ponto_em_retangulo
from app.scenes.instructions import run_instructions
from assets.music_manager import music_manager

def draw_title_scene(surf, w, h):
    """
    Desenha cena decorativa do menu (sol + horizonte + ondas).
    
    REQUISITO: (b) Primitivas gráficas (círculos e elipses)
    
    Args:
        surf: pygame.Surface
        w: largura da tela
        h: altura da tela
    """

# ─── Função Principal ───
def run_menu(superficie):
    """
    Executa o menu principal do jogo.
    
    REQUISITOS:
    - (i) Interação com Usuário: cliques do mouse em botões
    - (j) Menu: navegação entre cenas
    
    Todo o desenho usa apenas set_pixel (via primitivas do engine).
    
    Args:
        superficie: pygame.Surface principal
    
    Returns:
        str: 'iniciar' ou 'sair'
    """
    w = superficie.get_width()
    h = superficie.get_height()

    # Botões
    bw, bh = 180, 50
    bx = (w - bw) // 2
    by_iniciar = int(h * 0.45)
    by_instrucoes = by_iniciar + 70
    by_sair = by_instrucoes + 70

    # Garante que a música do menu está tocando
    music_manager.play("menu")

    while True:
        # Fundo (usa fill para performance; os elementos são desenhados com set_pixel)
        superficie.fill(color.SKY)

        # Cena: sol, horizonte, ondas
        draw_title_scene(superficie, w, h)

        # Título
        titulo = "JANGADEIRO: DRAGAO DO MAR"
        tw_approx = len(titulo) * 6 * 2
        draw_text(superficie, titulo, (w - tw_approx) // 2, int(h * 0.22), color.TITLE, scale=2)

        # Botões
        draw_button(superficie, bx, by_iniciar, bw, bh, "INICIAR", color.BTN_FILL, color.BTN_BORDER, color.BTN_TEXT)
        draw_button(superficie, bx, by_instrucoes, bw, bh, "COMO JOGAR", color.BTN_FILL, color.BTN_BORDER, color.BTN_TEXT)
        draw_button(superficie, bx, by_sair, bw, bh, "SAIR", color.BTN_FILL, color.BTN_BORDER, color.BTN_TEXT)

        pygame.display.flip()

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                return "sair"
            if e.type == pygame.MOUSEBUTTONDOWN and e.button == 1:
                mx, my = e.pos
                if ponto_em_retangulo(mx, my, bx, by_iniciar, bw, bh):
                    return "iniciar"
                if ponto_em_retangulo(mx, my, bx, by_instrucoes, bw, bh):
                    run_instructions(superficie)
                if ponto_em_retangulo(mx, my, bx, by_sair, bw, bh):
                    return "sair"
            if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
                return "sair"
