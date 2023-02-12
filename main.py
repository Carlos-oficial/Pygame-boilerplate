from jogo import jogo
from jogo import input
import pygame

jogador = [5, 5]

estado = [None, jogador]


def atualizar(estado, **kwargs):
    setas = input.setas()
    jogador = estado[1]
    x, y = jogador
    x += setas["direita"] - setas["esquerda"]
    y += setas["baixo"] - setas["cima"]
    jogador = [x,y]
    estado[1] = jogador
    return True


def desenhar(estado, screen):
    jogador = estado[1]
    x, y =  jogador[0],jogador[1]
    pygame.draw.polygon(
        screen,
        (255, 200, 120),
        [
            (x * 10, y * 10),
            (x * 10 + 10, y * 10),
            (x * 10 + 10, y * 10 + 10),
            (x * 10, y * 10 + 10),
        ],
    )


j = jogo.Jogo(estado, desenhar, atualizar)
j.comeca_ciclo_de_jogo()
