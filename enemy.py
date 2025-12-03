from game_actor import GameActor

class Enemy(GameActor):

    def __init__(self, image, x, y, grid, speed, initial_direction):
        super().__init__(image, x, y, grid, speed)
        self.direction = initial_direction