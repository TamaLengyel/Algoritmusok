def is_safe(row, col, cols, diag1, diag2):
    return not (cols[col] or diag1[row - col] or diag2[row + col])

def solve(row, board, cols, diag1, diag2):
    if row == 8:
        return 1
    count = 0
    for col in range(8):
        if board[row][col] == '.' and is_safe(row, col, cols, diag1, diag2):
            cols[col] = diag1[row - col] = diag2[row + col] = True
            count += solve(row + 1, board, cols, diag1, diag2)
            cols[col] = diag1[row - col] = diag2[row + col] = False
    return count

def main():
    board = [input().strip() for _ in range(8)]
    cols = [False] * 8
    diag1 = [False] * 15
    diag2 = [False] * 15
    print(solve(0, board, cols, diag1, diag2))

if __name__ == "__main__":
    main()
