import pygame, sys, math
from pygame.locals import *
from data.globals import *

## Basic Stuff ##
win = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption(f"Mapper ({WINDOW_SIZE[0]}x{WINDOW_SIZE[1]})")

## variables ##
tile_map = []

def drawGrid(surface, width, height, spacing):
    for x in range(0, width, spacing):
        pygame.draw.line(surface, (255,255,255), (x,0), (x, height))
    for y in range(0, height, spacing):
        pygame.draw.line(surface, (255,255,255), (0,y), (width, y))

running = True
while running:
    win.fill((0,0,0))
    drawGrid(win, WINDOW_SIZE[0], WINDOW_SIZE[1], 16)

    cursor = pygame.mouse.get_pos()
    pygame.draw.rect(win, (255,255,0), (cursor[0], cursor[1], 16, 16))

    if pygame.mouse.get_pressed()[0]:
        tile_map.append((cursor[0], cursor[1]))

    for tile in tile_map:
        pygame.draw.rect(win, (255,255,255), (tile[0], tile[1], 16, 16))

    for ev in pygame.event.get():
        if ev.type == QUIT:
            running = False;
            pygame.quit()
            sys.exit()

    pygame.display.update()
    clock.tick(FPS)