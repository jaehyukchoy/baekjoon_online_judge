from collections import deque
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

T = int(input())
d = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def dfs(x, y):
    v[y][x] = True
    for dx, dy in d:
        nx, ny = x + dx, y + dy
        if 0 <= nx < M and 0 <= ny < N and not v[ny][nx] and g[ny][nx] == 1:
            dfs(nx, ny)
            

for _ in range(T):
    M, N, K = map(int, input().split())
    g = [[0] * M for _ in range(N)]
    q = deque([])
    for _ in range(K):
        x, y = map(int, input().split())
        g[y][x] = 1
        q.append((x, y))
    v = [[False] * M for _ in range(N)]
    ans = 0
    while q:
        x, y = q.popleft()
        if not v[y][x]:
            ans += 1
            dfs(x, y)
    print(ans)