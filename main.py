import pygame, sys
from pygame.locals import *
from data.globals import *

## Basic Stuff ##
win = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption(f"Mapper ({WINDOW_SIZE[0]}x{WINDOW_SIZE[1]})")

running = True
while running:
    win.fill((0,0,0))
    cursor = pygame.mouse.get_pos()
    s = pygame.Surface((50,50))
    s.set_alpha(75)
    s.fill((255,255,0))
    win.blit(s, (cursor[0], cursor[1]))

    if pygame.mouse.get_pressed()[0]:
        pygame.draw.rect(win, (255,255,0), (cursor[0], cursor[1], 50, 50))

    for ev in pygame.event.get():
        if ev.type == QUIT:
            running = False;
            pygame.quit()
            sys.exit()

    pygame.display.update()
    clock.tick(FPS)