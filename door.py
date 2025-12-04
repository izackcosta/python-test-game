from pickable import Pickable

class Door(Pickable):

    def __init__(self, x, y, grid):
        super().__init__('door.png', x, y, grid, 1000)

    def pick(self, player, scenario):
        super().pick(player, scenario)