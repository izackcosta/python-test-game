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
                Coin(3, 13, grid), 
                Platform('grass_platform.png', 3, 7, grid),
                Platform('grass_platform.png', 4, 14, grid),
                Platform('grass_platform.png', 5, 14, grid),
                Platform('grass_platform.png', 0, 14, grid),
                Platform('grass_platform.png', 6, 14, grid),
                Platform('grass_platform.png', 7, 14, grid),
                Platform('grass_platform.png', 8, 14, grid),
                Platform('grass_platform.png', 9, 14, grid),
                Coin(5, 13, grid),
                Coin(7, 13, grid), ])

player = Player(grid, main_scenario)

def draw():
    screen.fill((0, 255, 255))
    main_scenario.draw()
    player.draw()
    screen.draw.text(f'Score: {player.score}', (10, 10), color='yellow', fontname = 'pixel_font')

def update():
    player.update()