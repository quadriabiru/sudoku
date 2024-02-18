import numpy as np
import random

# Function to check if there's repetition in a subgrid
def check_subgrid(grid, row_start, col_start, number):
    for i in range(3):
        for j in range(3):
            if grid[row_start + i][col_start + j] == number:
                return False
    return True

# Generate initial empty grid

def generate_grid(x):
    rows = 9
    cols = 9 
    grid = np.zeros((rows, cols), dtype=int)

    # Populate the grid randomly
    for _ in range(x):
        placed = False

        while placed == False:
            row = random.randrange(0, rows)
            col = random.randrange(0, cols)
            number = random.randint(1, 9)
            if grid[row][col] == 0 and \
            number not in grid[row, :] and \
            number not in grid[:, col] and \
            check_subgrid(grid, (row // 3) * 3, (col // 3) * 3, number):
                grid[row][col] = number
                placed = True
    return grid


