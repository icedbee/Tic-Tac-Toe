import numpy as np

comp, opponent = 3, 1

def isMovesLeft(grid):
    for i in range(3):
        for j in range(3):
            if grid[i][j] == 0:
                return True
    return False

def win_con(grid:np.ndarray, player:int) -> bool:
    for row in range(3):
        if grid[row][0] == grid[row][1] and grid[row][1] == grid[row][2]: #np.array_equal(grid[i], np.array([player, player, player])):
            if (grid[row][0] == player) and (player == 2 or player == 3):
                return True, 10
            elif (grid[row][0] == player) and (player == 1):
                return True, -10

    for col in range(3):
        if (grid[0][col] == grid[1][col]) and (grid[1][col] == grid[2][col]):
            if (grid[0][col] == player) and (player == 2 or player == 3):
                return True, 10
            elif (grid[0][col] == player) and (player == 1):
                return True, -10

    if (grid[0][2] == grid[1][1] == grid[2][0]):
        if (grid[0][2] == player) and (player == 2 or player == 3):
            return True, 10
        elif (grid[0][2] == player) and (player == 1):
            return True, -10

    if (grid[0][0] == grid[1][1] == grid[2][2]) and grid[0][0] == player:
        if (grid[0][0] == player) and (player == 2 or player == 3):
            return True, 10
        elif (grid[0][0] == player) and (player == 1):
            return True, -10
    
    return False, 0

#def solver(grid, depth, isMax):
def solver(grid, isMax):
    _, score = win_con(grid, comp)

    if score == 10:
        return score
    
    if score == -10:
        return score
    
    if isMovesLeft(grid) == False:
        return 0

    if isMax:
        best = -1000
        for i in range(3):
            for j in range(3):
                if grid[i][j] == 0:
                    grid[i][j] = comp

                    best = max(best, solver(grid, not isMax))

                    grid[i][j] = 0
        return best
    else:
        best = 1000
        for i in range(3):
            for j in range(3):
                if grid[i][j] == 0:
                    grid[i][j] = opponent
                    best = min(best, solver(grid, not isMax))
                    grid[i][j] = 0
        return best
    
def findBestMove(grid):
    bestVal = -1000
    bestMove = (-1, -1)
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 0:
                grid[i][j] = comp
                moveVal = solver(grid, False)
                grid[i][j] = 0

                if moveVal > bestVal:
                    bestMove = (i, j)
                    bestVal = moveVal

    return bestMove
