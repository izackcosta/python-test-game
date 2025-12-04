from game_actor import GameActor

class Enemy(GameActor):

    def __init__(self, image, x, y, grid, speed, initial_direction, game):
        super().__init__(image, x, y, grid, speed)
        self.initial_direction = initial_direction
        self.direction = self.initial_direction
        self.game = game

    def restart(self):
        self.direction = self.initial_direction
        self.grid.position_in_cell(self, self.initial_position[0], self.initial_position[1])