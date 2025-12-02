from player import Player

WIDTH = 800
HEIGHT = 600

player = Player()

def draw():
    screen.fill((0, 255, 255))
    player.draw()

def update():
    player.update()