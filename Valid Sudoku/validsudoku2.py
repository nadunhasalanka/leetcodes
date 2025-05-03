board = [["8","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
def isValidSudoku(board):
    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    subgrids = [set() for _ in range(9)]

    for r in range(9):
        for c in range(9):
            num = board[r][c]
            if num == '.':
                continue

            # check rows
            if num in rows[r]:
                return False
            rows[r].add(num)

            # check columns
            if num in cols[c]:
                return False
            cols[c].add(num)

            # subgrid index need to be find
            subgrid_index = (r // 3) * 3 + (c // 3)
            if num in subgrids[subgrid_index]:
                return False
            subgrids[subgrid_index].add(num)

    return True

print(isValidSudoku(board))

# idea is to check each row, column, and sub-box for duplicates.
# here the time complexity is O(n) because here the sub-boxes are checked in one single loop.
# the idea in the subgrid is to find the index of the subgrid by using the column and its row
# so how that works is that we can find the index of the subgrid by given formula:
    # subgrid_index = (r // 3) * 3 + (c // 3)
# and then we can check if the number is in the subgrid or not.
# r is the row and c is the column.


