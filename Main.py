import pygame as pg
from random import randint
import Bloc

pg.init()
pg.display.set_caption('2048')
window = pg.display.set_mode((500, 500))
window.fill((0, 0, 0))

grid_color = (255, 255, 255)
CELL_SIZE = 125
positions = [(x, y) for x in range(0, 375+1, 125) for y in range(0, 375+1, 125)]
blocs = [Bloc.Bloc(375, 375, CELL_SIZE, CELL_SIZE), Bloc.Bloc(0, 0, CELL_SIZE, CELL_SIZE)]

import random


def addBloc(blocs):
    occupied_positions = [(bloc.getX(), bloc.getY()) for bloc in blocs]

    free_positions = [pos for pos in positions if pos not in occupied_positions]

    if free_positions:
        x, y = random.choice(free_positions)
        blocs.append(Bloc.Bloc(x, y, CELL_SIZE, CELL_SIZE))


def drawGrid():
    for row in range(4):
        for col in range(4):
            rect = pg.Rect(col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pg.draw.rect(window, grid_color, rect, 2)

launched = True
while launched:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            launched = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_UP:
                for bloc in blocs:
                    bloc.moveUp(blocs)
                addBloc(blocs)
            elif event.key == pg.K_DOWN:
                for bloc in blocs:
                    bloc.moveDown(blocs)
                addBloc(blocs)
            elif event.key == pg.K_RIGHT:
                for bloc in blocs:
                    bloc.moveRight(blocs)
                addBloc(blocs)
            elif event.key == pg.K_LEFT:
                for bloc in blocs:
                    bloc.moveLeft(blocs)
                addBloc(blocs)
    for bloc in blocs:
        if not bloc.isLiving():
            blocs.remove(bloc)


    window.fill((0, 0, 0))
    drawGrid()

    for bloc in blocs:
        bloc.initSquare(window)

    pg.display.update()


