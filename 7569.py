from collections import deque

m, n, h = map(int, input().split())
tomato = []
for _ in range(h):
    tomato.append([list(map(int, input().split())) for _ in range(n)])

d = [(0, 1, 0), (0, 0, 1), (0, -1, 0), (0, 0, -1), (1, 0, 0), (-1, 0, 0)]

q = deque()
for i in range(h):
    for j in range(n):
        for k in range(m):
            if tomato[i][j][k] == 1:
                q.append((i, j, k))

while q:
    x, y, z = q.popleft()
    for dx, dy, dz in d:
        nx, ny, nz = x + dx, y + dy, z + dz
        if 0 <= nx < h and 0 <= ny < n and 0 <= nz < m and tomato[nx][ny][nz] == 0:
            tomato[nx][ny][nz] = tomato[x][y][z] + 1
            q.append((nx, ny, nz))

flag = False
ans = 0
for i in range(h):
    for j in range(n):
        for k in range(m):
            if tomato[i][j][k] == 0:
                flag = True
            ans = max(ans, tomato[i][j][k])

if flag:
    print(-1)
else:
    print(ans - 1)
