import sys
input = sys.stdin.readline
n, m, x, y, k = map(int,input().split())
board = []
for _ in range(n):
    board.append(list(map(int,input().split())))
com = list(map(int,input().split()))
dice = [0 for _ in range(6)]
for c in com:
    d1, d2, d3, d4, d5, d6 = dice[0], dice[1], dice[2], dice[3], dice[4], dice[5]
    if c == 1 and y < m-1:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = d1, d6, d2, d3, d5, d4
        y += 1
    elif c == 2 and y > 0:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = d1, d3, d4, d6, d5, d2
        y -= 1
    elif c == 3 and x > 0:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = d3, d2, d5, d4, d6, d1
        x -= 1
    elif c == 4 and x < n-1:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = d6, d2, d1, d4, d3, d5
        x += 1
    else:
        continue
    if board[x][y] == 0:
            board[x][y] = dice[5]
    else:
        dice[5] = board[x][y]
        board[x][y] = 0
    print(dice[2])