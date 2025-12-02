from pgzero.actor import Actor

class GameActor(Actor):
    
    def __init__(self, image, x, y):
        super().__init__(image, (x, y))