import pygame

pygame.init()

size = [800,600]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("saonline")

player_posX = 400
player_posY = 300

is_right = False
is_left = False

walkCount = 0

