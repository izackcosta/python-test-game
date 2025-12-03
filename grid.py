class Grid:

    def __init__(self, width, height, cell_size):
        self.width = width
        self.height = height
        self.cell_size = cell_size
        self.grid = self.create_grid()

    def create_grid(self):
        
        grid = []

        for y in range(0, self.height // self.cell_size):
            row = []
            for x in range(0, self.width // self.cell_size):
                row.append((x * self.cell_size, y * self.cell_size))
            grid.append(row)

        return grid
    
    def position_in_cell(self, prop, x, y):
        prop.topleft = (self.grid[y][x][0], self.grid[y][x][1])

    def get_cell_x(self, x):
        return x * self.cell_size + self.cell_size // 2