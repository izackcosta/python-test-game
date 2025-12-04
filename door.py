from pickable import Pickable
import pgzero.clock as clock

class Door(Pickable):

    def __init__(self, x, y, grid, game):
        super().__init__('door.png', x, y, grid, 1000, game)

    def pick(self):
        if self.picked:
            return
        clock.schedule(self.game['call_win'], 2)
        super().pick()