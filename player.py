from game_actor import GameActor
from pgzero.keyboard import keyboard

class Player(GameActor):

    def __init__(self, grid):

        super().__init__('hero_idle_right_0', 1, 9, grid, 2)

        self.animations['idle_right'] = [
            'hero_idle_right_0.png',
            'hero_idle_right_1.png',
            'hero_idle_right_2.png',
            'hero_idle_right_3.png'
        ]

        self.animations['walk_right'] = [
            'hero_run_right_0.png',
            'hero_run_right_1.png',
            'hero_run_right_2.png',
            'hero_run_right_3.png',
            'hero_run_right_4.png',
            'hero_run_right_5.png',
        ]

        self.animations['idle_left'] = [
            'hero_idle_left_0.png',
            'hero_idle_left_1.png',
            'hero_idle_left_2.png',
            'hero_idle_left_3.png'
        ]

        self.animations['walk_left'] = [
            'hero_run_left_0.png',
            'hero_run_left_1.png',
            'hero_run_left_2.png',
            'hero_run_left_3.png',
            'hero_run_left_4.png',
            'hero_run_left_5.png',
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
