from patrol_enemy import PatrolEnemy

class Goblin(PatrolEnemy):
    def __init__(self, x, y, grid, patrol_points, game):
        super().__init__('goblin_right_0', x, y, grid, 2, patrol_points, game)

        self.animations['walk_right'] = [
            'goblin_right_0.png',
            'goblin_right_1.png',
            'goblin_right_2.png',
            'goblin_right_3.png',
            'goblin_right_4.png',
            'goblin_right_5.png',
        ]

        self.animations['walk_left'] = [
            'goblin_left_0.png',
            'goblin_left_1.png',
            'goblin_left_2.png',
            'goblin_left_3.png',
            'goblin_left_4.png',
            'goblin_left_5.png',
        ]