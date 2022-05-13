import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int,input().split())
board = [list(input().rstrip()) for _ in range(n)]
visited = [[[[False for _ in range(m)] for _ in range(n)] for _ in range(m)] for _ in range(n)]
d = [[-1, 0], [1, 0], [0, -1], [0, 1]]
q = deque()

def move(x, y, dx, dy):
    cnt = 0
    while board[x+dx][y+dy] != '#' and board[x][y] != 'O':
        x += dx
        y += dy
        cnt += 1
    return x, y, cnt

for i in range(n):
    try:
        ry = board[i].index('R')
        rx = i
    except:
        pass
    try:
        by = board[i].index('B')
        bx = i
    except:
        pass

q.append([rx, ry, bx, by, 1])
visited[rx][ry][bx][by] = True

while q:
    rx, ry, bx, by, count = q.popleft()
    if count > 10:
        break
    for i in range(4):
        rx_, ry_, rcnt = move(rx, ry, d[i][0], d[i][1])
        bx_, by_, bcnt = move(bx, by, d[i][0], d[i][1])
        if board[bx_][by_] == 'O':
            continue
        if board[rx_][ry_] == 'O':
            print(count)
            exit()
        if rx_ == bx_ and ry_ == by_:
            if rcnt > bcnt:
                rx_ -= d[i][0]
                ry_ -= d[i][1]
            else:
                bx_ -= d[i][0]
                by_ -= d[i][1]
        if not visited[rx_][ry_][bx_][by_]:
            visited[rx_][ry_][bx_][by_] = True
            q.append([rx_, ry_, bx_, by_, count + 1])
print(-1)