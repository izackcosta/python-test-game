from player import Player
from coin import Coin
from platform_2 import Platform
from grid import Grid
from scenario import Scenario

WIDTH = 640
HEIGHT = 480

grid = Grid(WIDTH, HEIGHT, 32)

main_scenario = Scenario({Platform('grass_platform.png', 1, 10, grid), Platform('grass_platform.png', 2, 10, grid), Platform('grass_platform.png', 3, 10, grid), Coin(2, 9, grid)})

player = Player(grid)

def draw():
    screen.fill((0, 255, 255))
    main_scenario.draw()
    player.draw()

def update():
    player.update()