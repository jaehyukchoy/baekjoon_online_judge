import sys
input = sys.stdin.readline
n, m = map(int, input().split())
x, y, d = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(n)]
clean = [[0] * m for _ in range(n)]
move = [(-1, 0), (0, 1), (1, 0), (0, -1)]
cnt = 0
while True:
    clean[x][y] = 1
    nd = (d - 1) % 4
    dx, dy = move[nd]
    nx = x + dx
    ny = y + dy
    if room[nx][ny] == 0 and clean[nx][ny] == 0:
        d = nd
        x = nx
        y = ny
        cnt = 0
    else:
        d = nd
        cnt += 1
    if cnt == 4:
        dx, dy = move[(d + 2) % 4]
        nx = x + dx
        ny = y + dy
        if room[nx][ny] == 1:
            break
        else:
            x = nx
            y = ny
            cnt = 0
print(sum(map(sum,clean)))