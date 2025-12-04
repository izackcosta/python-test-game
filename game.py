from player import Player
from coin import Coin
from platform_2 import Platform
from grid import Grid
from scenario import Scenario
from mushroom import Mushroom
from goblin import Goblin
from fly import Fly

WIDTH = 800
HEIGHT = 640

score = 0

grid = Grid(WIDTH, HEIGHT, 32)

main_scenario = Scenario([Platform('grass_platform.png', 1, 19, grid),
                Platform('grass_platform.png', 2, 19, grid), 
                Platform('grass_platform.png', 3, 19, grid), 
                Coin(3, 18, grid), 
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
                #Mushroom(5, 18, grid, -1),
                #Mushroom(8, 18, grid, -1),
                Platform('grass_platform.png', 15, 19, grid),
                Platform('grass_platform.png', 18, 19, grid),
                Platform('grass_platform.png', 19, 19, grid),
                Platform('grass_platform.png', 20, 19, grid),
                Platform('grass_platform.png', 21, 19, grid),
                Coin(21, 18, grid),
                Platform('grass_platform.png', 22, 19, grid),
                Platform('grass_platform.png', 23, 19, grid),
                Platform('grass_platform.png', 24, 19, grid),
                Goblin(21, 18, grid, (18, 24)),
                Platform('grass_platform.png', 24, 17, grid),
                Platform('grass_platform.png', 21, 15, grid),
                Fly(12, 14, grid, (0, 24)),
                Platform('grass_platform.png', 18, 15, grid),
                Coin(18, 14, grid),
                Platform('grass_platform.png', 15, 15, grid),
                Platform('grass_platform.png', 12, 15, grid),
                Platform('grass_platform.png', 11, 15, grid),
                Platform('grass_platform.png', 10, 15, grid),
                Coin(10, 14, grid),
                Platform('grass_platform.png', 9, 15, grid),
                Platform('grass_platform.png', 8, 15, grid),
                Goblin(10, 14, grid, (12, 8)),
                Platform('grass_platform.png', 6, 13, grid),
                Platform('grass_platform.png', 4, 12, grid),
                Platform('grass_platform.png', 3, 12, grid),
                Platform('grass_platform.png', 2, 12, grid),
                Platform('grass_platform.png', 1, 12, grid),
                Platform('grass_platform.png', 0, 12, grid),
                Platform('grass_platform.png', 6, 10, grid),
                Goblin(0, 11, grid, (4, 0)),
                Coin(0, 11, grid),
                ])

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