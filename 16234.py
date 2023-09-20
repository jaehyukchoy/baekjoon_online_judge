import sys
import math
sys.setrecursionlimit(10**5)

n, l, r = map(int, input().split())
land = []
for _ in range(n):
    land.append(list(map(int, input().split())))
answer = 0

d = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def dfs(x, y):
    global united
    for dx, dy in d:
        nx = x + dx
        ny = y + dy
        if (
            0 <= nx < n
            and 0 <= ny < n
            and l <= abs(land[nx][ny] - land[x][y]) <= r
            and z[nx][ny] != 1
        ):
            united = True
            z[x][y] = 1
            z[nx][ny] = 1
            dfs(nx, ny)

def update():
    idx = []
    s = 0
    for i in range(n):
        for j in range(n):
            if z[i][j] == 1:
                z[i][j] = 2
                s += land[i][j]
                idx.append((i, j))
    return idx, math.floor(s / len(idx))



while True:
    z = [[0] * n for _ in range(n)]
    i = []
    v = []
    for x in range(n):
        for y in range(n):
            if z[x][y] == 0:
                united = False
                dfs(x,y)
                if united:
                    _i, _v = update()
                    i.append(_i)
                    v.append(_v)
    if not i:
        break

    for idx, i_arr in enumerate(i):
        for ix, iy in i_arr:
            land[ix][iy] = v[idx]

    answer += 1

print(answer)
