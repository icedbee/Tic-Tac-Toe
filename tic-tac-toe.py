import numpy as np
from solver import findBestMove, win_con

def UI_Print(grid:np.ndarray, x:bool) -> None:
    for i in range(len(grid)):
        for j, num in enumerate(grid[i]):
            if num == 1:
                if x:
                    print(" X ", end="")
                else:
                    print(" O ", end="")
            elif num == 2:
                if x:
                    print(" O ", end="")
                else:
                    print(" X ", end="")
            else:
                print("   ", end="")

            if j != len(grid[i])-1:
                print("|", end="")

        if i != 2:
            print("\n---|---|---")

    print()

if __name__ == "__main__":
    while 1:
        turn_count = 1
        grid = np.zeros((3,3))
        while 1:
            ai_input = input("Do you want to play against the computer? (y/n)\n")
            if ai_input == 'y' or ai_input == 'Y':
                print("Alright, you will playing against the computer!")
                ai = True
                break
            elif ai_input == 'n' or ai_input == 'N':
                print("Alright, you won't be playing against the computer!")
                ai = False
                break
            else:
                print("You didn't enter y or n! Try again.")

        while 1:
            x_o = input("Does Player 1 want to be x or o? (x/o)\n")
            if x_o == 'x' or x_o == 'X':
                print("Player 2 is O then!")
                x = True
                break
            elif x_o == 'o' or x_o == 'O':
                print("Player 2 is X then!")
                x = False
                break
            else:
                print("You didn't enter an X or an O! Try again.")

        while 1:
            p1_input = input("What column and row would player 1 like to go in? (please input your answer as \"row,column\")\n").split(",")
            grid[int(p1_input[0])-1][int(p1_input[1])-1] = 1
            if turn_count > 2:
                if win_con(grid, 1):
                    print(f"Player 1 has won the game!")
                    UI_Print(grid, x)
                    p_again = input("Would you like to play again? (y/n)\n")
                    if p_again == 'n':
                        exit(0)
                    else:
                        break

            UI_Print(grid, x)

            if turn_count == 5:
                print("Cat's Game!")
                p_again = input("Would you like to play again? (y/n)\n")
                if p_again == 'n':
                    exit(0)
                else:
                    break
            
            if ai:
                move = findBestMove(grid)
                grid[move[0]][move[1]] = 2
                print(f'The computer has gone to the coordinates {move[0]+1},{move[1]+1}!')
                if turn_count > 2:
                    if win_con(grid, 3):
                        print(f"The computer has won the game!")
                        UI_Print(grid, x)
                        p_again = input("Would you like to play again? (y/n)\n")
                        if p_again == 'n':
                            exit(0)
                        else:
                            break
            else:
                p2_input = input("What column and row would player 2 like to go in? (please input your answer as \"row,column\")\n").split(",")
                grid[int(p2_input[0])-1][int(p2_input[1])-1] = 2
                if turn_count > 2:
                    if win_con(grid, 2):
                        print(f"Player 2 has won the game!")
                        UI_Print(grid, x)
                        p_again = input("Would you like to play again? (y/n)\n")
                        if p_again == 'n':
                            exit(0)
                        else:
                            break

            UI_Print(grid, x)
            turn_count += 1
