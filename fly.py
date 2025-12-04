from patrol_enemy import PatrolEnemy

class Fly(PatrolEnemy):
    def __init__(self, x, y, grid, patrol_points):
        super().__init__('fly_right_0', x, y, grid, 4, patrol_points)

        self.animations['walk_right'] = [
            'fly_right_0.png',
            'fly_right_1.png',
            'fly_right_2.png',
        ]

        self.animations['walk_left'] = [
            'fly_left_0.png',
            'fly_left_1.png',
            'fly_left_2.png',
        ]