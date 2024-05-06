from collections import deque

n, m = map(int, input().split())
g = [list(map(int, input().split())) for _ in range(n)]

v = [[0] * m for _ in range(n)]
d = [(0, 1), (0, -1), (1, 0), (-1, 0)]
cnt = 0
ans = 0
for i in range(n):
    for j in range(m):
        if not v[i][j] and g[i][j]:
            cnt += 1
            c = 1
            q = deque([(i, j)])
            v[i][j] = 1
            while q:
                x, y = q.popleft()
                for dx, dy in d:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < n and 0 <= ny < m and not v[nx][ny] and g[nx][ny]:
                        c += 1
                        q.append((nx, ny))
                        v[nx][ny] = 1
            ans = max(ans, c)

print(cnt)
print(ans)
