from prop import Prop

class Pickable(Prop):

    def __init__(self, image, x, y, grid, points):
        super().__init__(image, x, y, grid)
        self.points = points

    def pick(self, player, scenario):
        player.game['score'] += self.points
        scenario.remove_prop(self)