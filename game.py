from player import Player
from coin import Coin
from platform_2 import Platform
from grid import Grid
from scenario import Scenario
from mushroom import Mushroom

WIDTH = 800
HEIGHT = 640

score = 0

grid = Grid(WIDTH, HEIGHT, 32)

main_scenario = Scenario([Platform('grass_platform.png', 1, 19, grid),
                Platform('grass_platform.png', 2, 19, grid), 
                Platform('grass_platform.png', 3, 19, grid), 
                Coin(3, 18, grid), 
                Platform('grass_platform.png', 3, 7, grid),
                Platform('grass_platform.png', 4, 19, grid),
                Platform('grass_platform.png', 5, 19, grid),
                Platform('grass_platform.png', 0, 19, grid),
                Platform('grass_platform.png', 6, 19, grid),
                Platform('grass_platform.png', 7, 19, grid),
                Platform('grass_platform.png', 8, 19, grid),
                Platform('grass_platform.png', 11, 19, grid),
                Platform('grass_platform.png', 12, 19, grid),
                Coin(5, 18, grid),
                Coin(7, 18, grid),
                Mushroom(6, 18, grid, -1)])

player = Player(grid, main_scenario)

def draw():
    screen.fill((0, 255, 255))
    main_scenario.draw()
    player.draw()
    if player:
        screen.draw.text(f'Score: {player.score}', (10, 10), color='yellow', fontname = 'pixel_font')

def update():
    player.update()
    main_scenario.update()