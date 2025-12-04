from player import Player
from coin import Coin
from platform_2 import Platform
from grid import Grid
from scenario import Scenario
from mushroom import Mushroom
from goblin import Goblin
from fly import Fly
from magic_fruit import MagicFruit
from door import Door
from pgzero.rect import Rect

WIDTH = 800
HEIGHT = 640

GameState ={
    'MENU'      : 1,
    'PLAYING'   : 2,
    'GAME_OVER' : 3,
    'WIN'       : 4
}

game = {
    'score' : 0,
    'state' : GameState['MENU'],
    'muted' : False,
}

start_game_rect = Rect((289,203), (225,34))
mute_rect = Rect((305,303), (189,34))
exit_rect = Rect((359,403), (83,34))

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
                Mushroom(5, 18, grid, -1),
                Mushroom(8, 18, grid, -1),
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
                Platform('grass_platform.png', 7, 13, grid),
                Platform('grass_platform.png', 4, 12, grid),
                Platform('grass_platform.png', 3, 12, grid),
                Platform('grass_platform.png', 2, 12, grid),
                Platform('grass_platform.png', 1, 12, grid),
                Platform('grass_platform.png', 0, 12, grid),
                Platform('grass_platform.png', 7, 10, grid),
                Platform('sand_platform.png', 9, 9, grid),
                Goblin(0, 11, grid, (4, 0)),
                MagicFruit(0, 11, grid),
                Fly(0, 8, grid, (24, 0)),
                Fly(24, 8, grid, (0, 24)),
                #Fly(13, 8, grid, (0, 24)),
                Platform('sand_platform.png', 12, 9, grid),
                Coin(12, 8, grid),
                Platform('sand_platform.png', 15, 9, grid),
                Platform('sand_platform.png', 18, 9, grid),
                Coin(18, 8, grid),
                Platform('sand_platform.png', 21, 7, grid),
                Fly(0, 4, grid, (24, 0)),
                Fly(24, 4, grid, (0, 24)),
                Fly(13, 4, grid, (0, 24)),
                Platform('sand_platform.png', 12, 5, grid),
                Coin(12, 4, grid),
                Platform('sand_platform.png', 15, 5, grid),
                Platform('sand_platform.png', 18, 5, grid),
                Coin(18, 4, grid),
                Platform('stone_platform.png', 10, 3, grid),
                Platform('stone_platform.png', 9, 3, grid),
                Platform('stone_platform.png', 8, 3, grid),
                Platform('stone_platform.png', 7, 3, grid),
                Platform('stone_platform.png', 6, 3, grid),
                Platform('stone_platform.png', 5, 3, grid),
                Platform('stone_platform.png', 4, 3, grid),
                Platform('stone_platform.png', 3, 3, grid),
                Platform('stone_platform.png', 2, 3, grid),
                Goblin(10, 2, grid, (2, 10)),
                Goblin(2, 2, grid, (10, 2)),
                MagicFruit(2, 2, grid),
                Platform('stone_platform.png', 5, 1, grid),
                Door(5, 0, grid)
                ])

player = Player(grid, main_scenario, game)

def draw():

    screen.fill((0, 255, 255))

    if game['state'] == GameState['MENU']:
        screen.draw.text('START GAME', center=(WIDTH//2, (HEIGHT//2) - 100), color='yellow', fontsize=50, background='red')
        muted = 'ON' if game['muted'] else 'OFF'
        screen.draw.text(f'MUTE: {muted}', center=(WIDTH//2, (HEIGHT//2)), color='yellow', fontsize=50, background='red')
        screen.draw.text('EXIT', center=(WIDTH//2, (HEIGHT//2 + 100)), color='yellow', fontsize=50, background='red')

    if game['state'] == GameState['PLAYING']:
        main_scenario.draw()
        player.draw()
        screen.draw.text(f'Score: {game["score"]}', (500, 10), color='yellow', fontname = 'pixel_font')

    if game['state'] == GameState['GAME_OVER']:
        screen.draw.text('GAME OVER!', center=(WIDTH//2, (HEIGHT//2)), color='yellow', fontsize=50)

    if game['state'] == GameState['WIN']:
        screen.draw.text(f'YOU WON!', center=(WIDTH//2, (HEIGHT//2)), color='yellow', fontsize=50)
        screen.draw.text(f'final score: {game["score"]}', center=(WIDTH//2, (HEIGHT//2) + 60), color='yellow', fontsize=25)

def update():

    if game['state'] == GameState['MENU']:
        pass

    if game['state'] == GameState['PLAYING']:
        player.update()
        main_scenario.update()

def on_mouse_down(pos):

    if game['state'] == GameState['MENU']:
        
        if start_game_rect.collidepoint(pos):
            game['state'] = GameState['PLAYING']

        if mute_rect.collidepoint(pos):
            game['muted'] = not game['muted']

        if exit_rect.collidepoint(pos):
            exit()

def call_win_screen():
    game['state'] = GameState['WIN']

game['call_win'] = call_win_screen

def call_game_over_screen():
    game['state'] = GameState['GAME_OVER']

game['call_game_over'] = call_game_over_screen
