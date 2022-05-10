import sys
from collections import deque
input = sys.stdin.readline
m, n = map(int,input().split())
graph = []
for _ in range(n):
    tmp = list(map(int,input().split()))
    graph.append(tmp)

def bfs(q):
    neighbor = [(1,0),(-1,0),(0,1),(0,-1)]
    while q:
        x, y = q.popleft()
        for dx, dy in neighbor:
            nn = x + dx
            nm = y + dy
            if 0 <= nn < n and 0 <= nm < m and graph[nn][nm] == 0:
                graph[nn][nm] = graph[x][y] + 1
                q.append((nn,nm))

q = deque()
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            q.append((i,j))

bfs(q)

ans = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            print(-1)
            exit()
        ans = max(ans,graph[i][j])
print(ans-1)