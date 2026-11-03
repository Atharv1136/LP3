#Practical 05
n = int(input("Enter N: "))
board = [[0]*n for i in range(n)]

def safe(r, c):
    for i in range(r):
        if board[i][c] == 1:
            return False
        if c-(r-i) >= 0 and board[i][c-(r-i)] == 1:
            return False
        if c+(r-i) < n and board[i][c+(r-i)] == 1:
            return False
    return True

def solve(r):
    if r == n:
        return True
    for c in range(n):
        if safe(r, c):
            board[r][c] = 1
            if solve(r+1):
                return True
            board[r][c] = 0
    return False

if solve(0):
    for row in board:
        print(row)
else:
    print("No solution")