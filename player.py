from game_actor import GameActor
from pgzero.keyboard import keyboard
from pickable import Pickable
from enemy import Enemy
import pgzero.clock as clock

class Player(GameActor):

    def __init__(self, grid, scenario, game):

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

        self.gravity = 15

        self.delta = 0

        self.grounded = False

        self.jump_accumulator = 0

        self.last_position = (self.x, self.y)

        self.alive = True

        self.debug_immortal = True

        self.game = game

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
        super().update()

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
            self.jump_accumulator += 0.15
            if self.jump_accumulator > 0.4:
                self.game['play_jump_sound']()
                self.jump_accumulator = 0.4
                self.delta = -self.jump_accumulator
                self.jump_accumulator = 0
                self.grounded = False

        if keyboard.z == False and self.jump_accumulator > 0 and self.grounded:
            self.game['play_jump_sound']()
            self.delta = -self.jump_accumulator
            self.jump_accumulator = 0
            self.grounded = False
    
    def process_collisions(self):

        for prop in self.scenario.props:
            
            if self.colliderect(prop):

                if  isinstance(prop, Pickable):
                    prop.pick()
                    continue

                if isinstance(prop, Enemy) and not self.debug_immortal:
                    self.die()
                    continue

    def process_gravity(self):
        self.y += self.gravity * self.delta
        for prop in self.scenario.props:
            if isinstance(prop, Pickable) or isinstance(prop, Enemy):
                continue
            while self.colliderect(prop):
                if  abs(self.bottom - prop.top) < abs(self.top - prop.bottom):
                    self.y -= 1
                    self.grounded = True
                else:
                    self.y += 1
                self.delta = 0
                return
        self.grounded = False
        self.delta += 1 / 60

    def die(self):
        self.game['play_die_sound']()
        self.alive = False
        clock.schedule(self.game['call_game_over'], 2)

    def restart(self):
        self.grid.position_in_cell(self, self.initial_position[0], self.initial_position[1])
        self.direction = GameActor.Direction['RIGHT']
        self.current_animation = self.animations['idle_right']
        self.alive = True
