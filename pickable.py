from prop import Prop

class Pickable(Prop):

    def __init__(self, image, x, y, grid):
        super().__init__(image, x, y, grid)

    def pick(self, player, scenario):
        scenario.remove_prop(self)