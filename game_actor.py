from pgzero.actor import Actor

class GameActor(Actor):
    
    Framerate = 12

    def __init__(self, image, x, y):

        super().__init__(image, (x, y))

        self.animations = {
            'idle_right': [
            'knight_idle_right_0.png',
            'knight_idle_right_1.png',
            'knight_idle_right_2.png',
            'knight_idle_right_3.png'
        ],

        }

        self.animation_timer = 0

        self.current_frame = 0

        self.current_animation = self.animations['idle_right']
    
    def draw(self):
        self.animation_timer += 1
        if self.animation_timer % GameActor.Framerate == 0:
            self.current_frame = (self.current_frame + 1) % len(self.current_animation)
            self.image = self.current_animation[self.current_frame]
        super().draw()