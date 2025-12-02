from game_actor import GameActor

class Player(GameActor):

    def __init__(self):

        super().__init__('knight_idle_right_0', 100, 100)

        self.animations['idle_right'] = [
            'knight_idle_right_0.png',
            'knight_idle_right_1.png',
            'knight_idle_right_2.png',
            'knight_idle_right_3.png'
        ]

        self.current_animation = self.animations['idle_right']
