import numpy as np
import generategrid, vaildateboard

def possible(row, column, number):
    global grid
    # Is the number in the row?
    for i in range(0,9):
        if grid[row][i] == number:
            return False

    #Is the number in the column?
    for i in range(0,9):
        if grid[i][column] == number:
            return False
        
    #Is the number in the 3x3 sub-grid
    x = (column // 3) * 3
    y = (row // 3) * 3

    for i in range(0,3):
        for j in range(0,3):
            if grid[y + i][x + j] == number:
                return False
        
    return True

def solve():
    global grid
    for row in range(0, 9):
        for column in range(0, 9):
            if grid[row][column] == 0:
                for number in range(1, 10):
                    if possible(row, column, number):
                        grid[row][column] = number
                        if solve():  # Check if the puzzle is solved after placing the number
                            return True
                        grid[row][column] = 0  # Backtrack if the number doesn't lead to a solution
                return False  # Return False if no valid number is found for this cell
    return True  # Return True if all cells are filled (puzzle solved)

grid = generategrid.generate_grid(20)

print(grid)

solve()

print(grid)

'''if __name__ == '__main__':
    grid = generategrid.generate_grid(30)

    print(grid)

    solve()

    print(grid)

    if vaildateboard.is_valid(grid):
        print("The Sudoku puzzle has been solved properly.")
    else:
        print("The Sudoku puzzle has not been solved properly.")'''

