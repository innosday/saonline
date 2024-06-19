import pygame,sys
from datafile import *
from pygame.locals import *


clock = pygame.time.Clock()
pygame.init()

screen = [800,600]
pygame.display.set_mode(screen)

spr_character = SpriteSheet('')
