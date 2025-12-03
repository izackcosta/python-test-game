from player import Player
from coin import Coin
from platform_2 import Platform
from grid import Grid

WIDTH = 640
HEIGHT = 480

grid = Grid(WIDTH, HEIGHT, 32)

scenario = {Platform('grass_platform', 1, 10, grid),}

def draw_scenario():
    for prop in scenario:
        prop.draw()

player = Player()

def draw():
    screen.fill((0, 255, 255))
    draw_scenario()
    player.draw()

def update():
    player.update()