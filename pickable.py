from prop import Prop

class Pickable(Prop):

    def __init__(self, image, x, y, grid, points, game):
        super().__init__(image, x, y, grid)
        self.points = points
        self.game = game

    def pick(self, scenario):
        self.game['score'] += self.points
        self.game['play_pickable_sound']()
        scenario.remove_prop(self)