from game_actor import GameActor
from pgzero.keyboard import keyboard

class Player(GameActor):

    def __init__(self):

        super().__init__('knight_idle_right_0', 100, 100, 2)

        self.animations['idle_right'] = [
            'knight_idle_right_0.png',
            'knight_idle_right_1.png',
            'knight_idle_right_2.png',
            'knight_idle_right_3.png'
        ]

        self.current_animation = self.animations['idle_right']

    def update(self):
        if keyboard.right:
            self.move(1)
