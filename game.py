from player import Player
from coin import Coin
from platform_2 import Platform
from grid import Grid
from scenario import Scenario

WIDTH = 640
HEIGHT = 480

score = 0

grid = Grid(WIDTH, HEIGHT, 32)

main_scenario = Scenario([Platform('grass_platform.png', 1, 14, grid),
                Platform('grass_platform.png', 2, 14, grid), 
                Platform('grass_platform.png', 3, 14, grid), 
                Coin(2, 9, grid), 
                Platform('grass_platform.png', 3, 7, grid),
                Platform('grass_platform.png', 4, 14, grid),
                Platform('grass_platform.png', 5, 14, grid),])

player = Player(grid, main_scenario)

def draw():
    screen.fill((0, 255, 255))
    main_scenario.draw()
    player.draw()
    screen.draw.text(f'Score: {player.score}', (10, 10), color='yellow')

def update():
    player.update()