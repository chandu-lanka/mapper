import pygame, sys
from pygame.locals import *
from data.globals import *

## Basic Stuff ##
win = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption(f"Mapper ({WINDOW_SIZE[0]}x{WINDOW_SIZE[1]})")

running = True
while running:
    for ev in pygame.event.get():
        if ev.type == QUIT:
            running = False;
            pygame.quit()
            sys.exit()