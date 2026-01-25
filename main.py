import pygame
import sys
from engine.framebuffer import set_pixel
from engine.fill.flood_fill import flood_fill_iterativo
from engine.raster.line import bresenham
from engine.raster.line import desenhar_poligono
from engine.raster.circle import draw_circle
from engine.raster.elipse import draw_elipse

pygame.init()
largura, altura = 400, 300
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Main")

rodando = True

while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    tela.fill((0, 0, 0))

    # testes
    tela.fill((255, 255, 255))

    draw_elipse(tela, 300, 200, 150, 80, (0, 0, 0))
    flood_fill_iterativo(tela, 300, 200, (0, 150, 255), (0, 0, 0))


    pygame.display.flip()

pygame.quit()
sys.exit()