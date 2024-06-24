import numpy as np

def win_con(grid:np.ndarray, player:int) -> bool:
    for i in range(3):
        if np.array_equal(grid[i], np.array([player, player, player])):
            print(f"Player {player} has won the game!")
            return True

        if (grid[0][i] == grid[1][i] == grid[2][i]) and grid[0][i] == player:
            print(f"Player {player} has won the game!")
            return True

    if (grid[0][2] == grid[1][1] == grid[2][0]) and grid[0][2] == player:
        print(f"Player {player} has won the game!")
        return True

    if (grid[0][0] == grid[1][1] == grid[2][2]) and grid[0][0] == player:
        print(f"Player {player} has won the game!")
        return True

def game_play(grid:np.ndarray, move:str, player:int) -> np.ndarray:
    move = move.split(",")
    grid[move[0]][move[1]] = player
    return grid

def score(win:bool, owin:bool) -> int:
    if win:
        return 10
    elif owin:
        return -10
    else:
        return 0

def solver(grid:np.ndarray, player:int, opponent:bool) -> None:
    tmp_grid = np.copy(grid)
    if win_con(tmp_grid, 3):
        return score()
    
    scores = []
    moves = []

    #game.get_available_moves.each do |move|
    for i in range(len(tmp_grid)):
        for j, num in enumerate(tmp_grid[i]):
            if num == 0:
                continue
            
            move = f'{i},{j}'
            possible_game = game_play(tmp_grid, move, player)#game.get_new_state(f'{i},{j}')
            scores.append(solver(possible_game))
            moves.append(move)

    if not opponent:
        max_score_index = scores.index(max(scores)) #scores.each_with_index.max[1]
        return scores[max_score_index], moves[max_score_index]
    else:
        min_score_index = scores.index(min(scores)) #scores.each_with_index.min[1]
        return scores[min_score_index], moves[min_score_index]
