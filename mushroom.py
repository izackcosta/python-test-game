from enemy import Enemy

class Mushroom(Enemy):

    def __init__(self, x, y, grid, initial_direction):
        
        super().__init__('mushroom_right_0', x, y, grid, 1, initial_direction)

        self.animations['walk_right'] = [
            'mushroom_right_0.png',
            'mushroom_right_1.png',
            'mushroom_right_2.png',
            'mushroom_right_3.png',
            'mushroom_right_4.png',
            'mushroom_right_5.png',
            'mushroom_right_6.png',
            'mushroom_right_7.png'
        ]

        self.animations['walk_left'] = [
            'mushroom_left_0.png',
            'mushroom_left_1.png',
            'mushroom_left_2.png',
            'mushroom_left_3.png',
            'mushroom_left_4.png',
            'mushroom_left_5.png',
            'mushroom_left_6.png',
            'mushroom_left_7.png'
        ]

        self.current_animation = self.animations['walk_right'] if self.direction == 1 else self.animations['walk_left']

    def update(self):
        self.move(self.direction)

