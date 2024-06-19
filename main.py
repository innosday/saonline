import pygame,sys
from datafile import *
from pygame.locals import *


clock = pygame.time.Clock()
pygame.init()

screen = [640,480]
bg = pygame.display.set_mode(screen,0,32)

spr_character = SpriteSheet('IDLE.png',24,40,5,34,5)
# spr_character = SpriteSheet('SpriteSheet1.png',16,16,8,8,11)

while True:
    bg.blit(spr_character.spr[1],(320,240))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    clock.tick(60)