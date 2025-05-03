board = [["8","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
def isValidSudoku(board):
    # check rows
    for row in board:
        seen = set()
        for num in row:
            if num == '.':
                continue
            if num in seen:
                return False
            seen.add(num)
        
    # print("hello from 1")
        
    # then Columns
    for column in range(9):
        seen = set()
        for row in range(9):
            num = board[row][column]
            if num == ".":
                continue
            if num in seen:
                return False
            seen.add(num)

    # print("hello from 2")

    # next sub ones
    for i in range(0,9,3):
        for j in range(0,9,3):
            seen = set()
            for row in range(i, i + 3):
                for column in range(j, j + 3):
                    num = board[row][column]
                    print(num)
                    if num == ".":
                        continue
                    if num in seen:
                       return False
                    seen.add(num)

    return True

print(isValidSudoku(board))

# idea is to check each row, column, and sub-box for duplicates.
# code is working fine but the the time complexity is O(n^2) which is not good. because of the nested loops checks in the sub-boxes.
# sub boxes are pretty hard to check and lets see if we can do better than this.

