from game_actor import GameActor

class Prop(GameActor):

    def __init__(self, image, x, y, grid):
        super().__init__(image, x, y, grid, 0)