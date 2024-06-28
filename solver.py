import numpy as np

player, opponent = 3, 1

def win_con(grid:np.ndarray, player:int) -> bool:
    for i in range(3):
        if np.array_equal(grid[i], np.array([player, player, player])):
            return True

        if (grid[0][i] == grid[1][i] == grid[2][i]) and grid[0][i] == player:
            return True

    if (grid[0][2] == grid[1][1] == grid[2][0]) and grid[0][2] == player:
        return True

    if (grid[0][0] == grid[1][1] == grid[2][2]) and grid[0][0] == player:
        return True
    
    return False

def isMovesLeft(grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 0:
                return True
    return False

def solver(grid, depth, isMax):
    tmp_grid = np.copy(grid)
    score = 0
    if win_con(tmp_grid, player):
        score = 10

    if score == 10:
        return score
    
    if score == -10:
        return score
    
    if isMovesLeft(grid) == False:
        return 0

    if isMax:
        best = -10
        for i in range(len(tmp_grid)):
            for j in range(len(tmp_grid[i])):
                if grid[i][j] == 0:
                    grid[i][j] = player

                    best = max(best, solver(grid, depth+1, not isMax))

                    grid[i][j] = 0
        return best
    else:
        best = 10
        for i in range(len(tmp_grid)):
            for j in range(len(tmp_grid[i])):
                if grid[i][j] == 0:
                    grid[i][j] = opponent
                    best = min(best, solver(grid, depth+1, not isMax))
                    grid[i][j] = 0
        return best
    
def findBestMove(grid):
    bestVal = -10
    bestMove = (-1, -1)
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 0:
                grid[i][j] = player
                moveVal = solver(grid, 0, False)
                grid[i][j] = 0

                if moveVal > bestVal:
                    bestMove = (i, j)
                    bestVal = moveVal

    return bestMove
