from game_actor import GameActor

class Prop(GameActor):

    def __init__(self, image, x, y, grid):
        super().__init__(image, 0, 0, 0)
        grid.position_to_cell(self, x, y)