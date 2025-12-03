from game_actor import GameActor
from pgzero.keyboard import keyboard
from pickable import Pickable
from enemy import Enemy

class Player(GameActor):

    def __init__(self, grid, scenario):

        super().__init__('hero_idle_right_0', 1, 18, grid, 2)

        self.animations['idle_right'] = [
            'hero_idle_right_0.png',
            'hero_idle_right_1.png',
            'hero_idle_right_2.png',
            'hero_idle_right_3.png'
        ]

        self.animations['walk_right'] = [
            'hero_run_right_0.png',
            'hero_run_right_1.png',
            'hero_run_right_2.png',
            'hero_run_right_3.png',
            'hero_run_right_4.png',
            'hero_run_right_5.png',
        ]

        self.animations['idle_left'] = [
            'hero_idle_left_0.png',
            'hero_idle_left_1.png',
            'hero_idle_left_2.png',
            'hero_idle_left_3.png'
        ]

        self.animations['walk_left'] = [
            'hero_run_left_0.png',
            'hero_run_left_1.png',
            'hero_run_left_2.png',
            'hero_run_left_3.png',
            'hero_run_left_4.png',
            'hero_run_left_5.png',
        ]

        self.current_animation = self.animations['idle_right']

        self.scenario = scenario

        self.score = 0

        self.gravity = 10

        self.delta = 0

        self.grounded = False

        self.jump_accumulator = 0

        self.last_position = (self.x, self.y)

        self.alive = True

    def draw(self):
        if not self.alive:
            return
        super().draw()

    def update(self):
        if not self.alive:
            return
        self.last_position = (self.x, self.y)
        self.process_player_input()
        self.process_gravity()
        self.process_collisions()

    def process_player_input(self):

        if keyboard.right:
            if self.current_animation != self.animations['walk_right']:
                self.current_animation = self.animations['walk_right']
                self.direction = GameActor.Direction['RIGHT']
            self.move(self.direction)

        elif keyboard.left:
            if self.current_animation != self.animations['walk_left']:
                self.current_animation = self.animations['walk_left']
                self.direction = GameActor.Direction['LEFT']
            self.move(self.direction)

        elif self.direction == GameActor.Direction['RIGHT']:
            self.current_animation = self.animations['idle_right']

        else:
            self.current_animation = self.animations['idle_left']

        if keyboard.z and self.grounded:
            self.jump_accumulator += 0.2
            if self.jump_accumulator > 0.5:
                self.jump_accumulator = 0.5
                self.delta = -self.jump_accumulator
                self.jump_accumulator = 0
                self.grounded = False

        if keyboard.z == False and self.jump_accumulator > 0 and self.grounded:
            self.delta = -self.jump_accumulator
            self.jump_accumulator = 0
            self.grounded = False
    
    def process_collisions(self):

        grounded = False

        for prop in self.scenario.props:
            
            if self.colliderect(prop):

                if  isinstance(prop, Pickable):
                    prop.pick(self, self.scenario)
                    continue

                if isinstance(prop, Enemy):
                    self.alive = False
            
                if self.bottom > prop.top:
                    grounded = True
                self.pos = self.last_position
                self.delta = 0
        
        self.grounded = grounded

                

    def process_gravity(self):
        if self.grounded:
            return
        self.y += self.gravity * self.delta
        self.delta += 1 / 60