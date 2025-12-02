from game_actor import GameActor

WIDTH = 800
HEIGHT = 600

player = GameActor('knight_idle_right_0.png', 400, 300)

def draw():
    screen.fill((0, 255, 255))
    player.draw()

def update():
    pass