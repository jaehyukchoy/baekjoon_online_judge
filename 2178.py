from collections import deque

n, m = map(int, input().split())
miro = [list(map(int, list(input()))) for _ in range(n)]

q = deque([(0, 0)])
v = [[0] * m for _ in range(n)]
d = [(1, 0), (-1, 0), (0, 1), (0, -1)]

v[0][0] = 1
while q:
    x, y = q.popleft()
    for dx, dy in d:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < m and not v[nx][ny] and miro[nx][ny]:
            v[nx][ny] = v[x][y] + 1
            q.append((nx, ny))
print(v[n - 1][m - 1])
