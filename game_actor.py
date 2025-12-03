from pgzero.actor import Actor

class GameActor(Actor):
    
    Framerate = 6

    Direction ={
        'RIGHT': 1,
        'LEFT': -1
    }

    def __init__(self, image, x, y, grid, speed):

        super().__init__(image, (0, 0))

        self.grid = grid

        self.grid.position_in_cell(self, x, y)

        self.speed = speed

        self.direction = GameActor.Direction['RIGHT']

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

    def update(self):
        pass

    def move(self, dx):
        self.x += dx * self.speed