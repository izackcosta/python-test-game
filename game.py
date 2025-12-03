from player import Player

WIDTH = 640
HEIGHT = 480

player = Player()

def draw():
    screen.fill((0, 255, 255))
    player.draw()

def update():
    player.update()