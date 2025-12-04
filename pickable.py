from prop import Prop

class Pickable(Prop):

    def __init__(self, image, x, y, grid, points, game):
        super().__init__(image, x, y, grid)
        self.points = points
        self.game = game
        self.picked = False

    def draw(self):
        if self.picked:
            return
        super().draw()

    def pick(self):
        if self.picked:
            return
        self.game['score'] += self.points
        self.game['play_pickable_sound']()
        self.picked = True

    def restart(self):
        self.picked = False