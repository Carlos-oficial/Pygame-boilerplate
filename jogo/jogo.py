from jogo.constantes import *
from jogo.input import *
import pygame
import sys


class Jogo:
    """
    Classe que respresenta o estado do Jogo
    """

    def __init__(self, estado_inicial, desenha_estado, atualiza_estado, **kwargs):
        for key, arg in kwargs:
            self.__setattr__(key, arg)
        if not hasattr(self, "tamanho_do_ecra"):
            self.tamanho_do_ecra = TAMANHO_DO_ECRA
        if not hasattr(self, "nome_do_jogo"):
            self.nome_do_jogo = NOME_DO_JOGO
        self.estado = estado_inicial
        self.desenha_estado = desenha_estado
        self.atualiza_estado = atualiza_estado

    def comeca_ciclo_de_jogo(self):
        """
        Cria uma 'Screen' e usa as funções desenha_estado e atualiza_estado para correr o jogo
        """
        clock = pygame.time.Clock()
        pygame.init()
        pygame.font.init()
        screen = pygame.display.set_mode(self.tamanho_do_ecra)
        pygame.display.set_caption(self.nome_do_jogo)
        tick = 0
        continuar = True
        while continuar:
            screen.fill((0, 0, 0))
            self.desenha_estado(self.estado, screen)
            pygame.display.update()
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    playing = False
            clock.tick(60)
            continuar = self.atualiza_estado(self.estado, time=clock.get_time())
            tick += 1
