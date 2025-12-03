from pgzero.actor import Actor

class GameActor(Actor):
    
    Framerate = 6

    def __init__(self, image, x, y, speed):

        super().__init__(image, (x, y))

        self.speed = speed

        self.animations = {}

        self.animation_timer = 0

        self.current_frame = 0

        self.current_animation = None
    
    def draw(self):
        self.animation_timer += 1
        if self.animation_timer % GameActor.Framerate == 0 and self.current_animation:
            self.current_frame = (self.current_frame + 1) % len(self.current_animation)
            self.image = self.current_animation[self.current_frame]
        super().draw()

    def move(self, dx):
        self.x += dx * self.speed