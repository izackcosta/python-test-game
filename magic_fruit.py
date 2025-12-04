from pickable import Pickable

class MagicFruit(Pickable):

    def __init__(self, x, y, grid):

        super().__init__('fruit_0', x, y, grid, 500)

        self.animations['glow'] = [
            'fruit_0.png',
            'fruit_1.png',
            'fruit_2.png',
            'fruit_3.png',
        ]

        self.current_animation = self.animations['glow']