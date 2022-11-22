# https://school.programmers.co.kr/learn/courses/30/lessons/12952?language=python3
# N-Queen, level 2
def solution(n):
    queen_cols = [0] * n  # queen[i] = j means queen is in (i, j)
    return dfs(queen_cols, row=0)  # start from row 0


def dfs(queen_cols, row=0) -> int:
    """Count the number of ways to place queens from the row to the end."""
    if row == len(queen_cols):  # all queens are placed
        print(queen_cols)
        return 1

    count = 0
    for col in range(len(queen_cols)):  # try all columns
        queen_cols[row] = col  # place queen in (row, col)
        if is_available(queen_cols, row):  # check if it is available
            count += dfs(queen_cols, row + 1)  # place next queen
    
    return count


def is_available(queen_cols, row):
    for fore_row in range(row):  # check all rows before the row
        # check if there is a queen in the same column
        if queen_cols[fore_row] == queen_cols[row]:
            return False
        # check if there is a queen in the diagonal
        if abs(queen_cols[fore_row] - queen_cols[row]) == row - fore_row:
            return False

    return True
