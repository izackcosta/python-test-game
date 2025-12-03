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

        self.animations['walk_right'] = [
            'knight_walk_right_0.png',
            'knight_walk_right_1.png',
            'knight_walk_right_2.png',
            'knight_walk_right_3.png',
            'knight_walk_right_4.png',
            'knight_walk_right_3.png',
            'knight_walk_right_2.png',
            'knight_walk_right_1.png'
        ]

        self.animations['idle_left'] = [
            'knight_idle_left_0.png',
            'knight_idle_left_1.png',
            'knight_idle_left_2.png',
            'knight_idle_left_3.png'
        ]

        self.animations['walk_left'] = [
            'knight_walk_left_0.png',
            'knight_walk_left_1.png',
            'knight_walk_left_2.png',
            'knight_walk_left_3.png',
            'knight_walk_left_4.png',
            'knight_walk_left_3.png',
            'knight_walk_left_2.png',
            'knight_walk_left_1.png'
        ]

        self.current_animation = self.animations['idle_right']

        self.direction = 0

    def update(self):
        if keyboard.right:
            if self.current_animation != self.animations['walk_right']:
                self.current_animation = self.animations['walk_right']
                self.direction = 0
            self.move(1)
        elif keyboard.left:
            if self.current_animation != self.animations['walk_left']:
                self.current_animation = self.animations['walk_left']
                self.direction = 1
            self.move(-1)
        elif self.direction == 0:
            self.current_animation = self.animations['idle_right']
        else:
            self.current_animation = self.animations['idle_left']
