from enemy import Enemy

class PatrolEnemy(Enemy):

    def __init__(self, image, x, y, grid, speed, patrol_points, game):
        super().__init__(image, x, y, grid, speed, 0, game)
        self.patrol_points = patrol_points
        self.current_point_index = 0
        self.go_to_next_point()

    def go_to_next_point(self):
        if self.grid.get_cell_x(self.patrol_points[self.current_point_index]) < self.x:
            self.direction = -1
        else:
            self.direction = 1

    def arrived_at_point(self):
        target_x = self.grid.get_cell_x(self.patrol_points[self.current_point_index])
        return (self.direction == 1 and self.x >= target_x) or (self.direction == -1 and self.x <= target_x)

    def update(self):
        self.move(self.direction)
        if self.arrived_at_point():
            self.current_point_index = (self.current_point_index + 1) % len(self.patrol_points)
            self.go_to_next_point()
        self.current_animation = self.animations['walk_right'] if self.direction == 1 else self.animations['walk_left']
        super().update()

    def restart(self):
        super().restart()
        self.current_point_index = 0
        self.go_to_next_point()
