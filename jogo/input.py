import pygame


def setas():
    left = pygame.key.get_pressed()[pygame.K_LEFT]
    up = pygame.key.get_pressed()[pygame.K_UP]
    down = pygame.key.get_pressed()[pygame.K_DOWN]
    right = pygame.key.get_pressed()[pygame.K_RIGHT]
    return {"esquerda": left, "cima": up, "baixo": down, "direita": right}
