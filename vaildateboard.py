import numpy as np

def is_valid(board):
    # Check rows and columns
    for i in range(9):
        if not is_valid_line(board[i]) or not is_valid_line(board[:, i]):
            return False
    
    # Check 3x3 subgrids
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            if not is_valid_line(board[i:i+3, j:j+3].flatten()):
                return False
    
    return True

def is_valid_line(line):
    # Remove zeros from line
    line = line[line != 0]
    # Check if there are any duplicate values
    return len(np.unique(line)) == len(line)