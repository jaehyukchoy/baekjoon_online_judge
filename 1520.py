import sys
sys.setrecursionlimit(10**6)
m, n = map(int, input().split())
zido = [list(map(int, input().split())) for _ in range(m)]

d = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def dfs(x, y):
    if x == m - 1 and y == n - 1:
        return 1
    if v[x][y] == -1:
        v[x][y] = 0
        for dx, dy in d:
            nx, ny = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny < n and zido[nx][ny] < zido[x][y]:
                v[x][y] += dfs(nx, ny)
    return v[x][y]


v = [[-1] * n for _ in range(m)]

print(dfs(0, 0))
