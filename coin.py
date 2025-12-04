from pickable import Pickable

class Coin(Pickable):

    def __init__(self, x, y, grid, game):

        super().__init__('coin_0', x, y, grid, 100, game)

        self.animations['spin'] = [
            'coin_0.png',
            'coin_1.png',
            'coin_2.png',
            'coin_3.png',
            'coin_4.png',
            'coin_5.png',
            'coin_6.png',
            'coin_5.png',
            'coin_4.png',
            'coin_7.png',
            'coin_2.png',
            'coin_1.png'
        ]

        self.current_animation = self.animations['spin']