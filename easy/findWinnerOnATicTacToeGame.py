# 1275. Find Winner on a Tic Tac Toe Game
# https://leetcode.com/problems/find-winner-on-a-tic-tac-toe-game/

def tictactoe(self, moves: List[List[int]]) -> str:
    grid = [["" for i in range(3)] for j in range(3)]
    for idx, move in enumerate(moves):
        i, j = move[0], move[1]
        if idx % 2 == 0:
            grid[i][j] = "A"
        else: 
            grid[i][j] = "B"
    for i in range(3):
        if grid[i][0] == grid[i][1] == grid[i][2] and grid[i][0] in ["A", "B"]:
            return grid[i][0]
        elif grid[0][i] == grid[1][i] == grid[2][i] and grid[0][i] in ["A", "B"]:
            return grid[0][i]
    if grid[0][0] == grid[1][1] == grid[2][2] and grid[0][0] in ["A", "B"]:
        return grid[0][0]
    elif grid[0][2] == grid[1][1] == grid[2][0] and grid[0][2] in ["A", "B"]:
        return grid[0][2]
    if len(moves) == 9:
        return "Draw"
    else:
        return "Pending"