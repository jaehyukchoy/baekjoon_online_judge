import sys
from copy import deepcopy
from collections import deque
from itertools import combinations
input = sys.stdin.readline
n, m = map(int, input().split())
graph = []
for _ in range(n):
    tmp = list(map(int, input().split()))
    graph.append(tmp)

def bfs(g, q):
    visited = deque()
    d = [(1,0),(-1,0),(0,1),(0,-1)]
    while q:
        x, y = q.popleft()
        if (x,y) not in visited:
            visited.append((x,y))
            for dx, dy in d:
                nn = x + dx
                nm = y + dy
                if 0 <= nn < n and 0 <= nm < m and g[nn][nm] == 0:
                    g[nn][nm] = 2
                    q.append((nn,nm))

area = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            area.append((i,j))

ans = 0
for wall in combinations(area, 3):
    graph_cp = deepcopy(graph)
    for wx, wy in wall:
        graph_cp[wx][wy] = 1
    q = deque()
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 2:
                q.append((i,j))
    bfs(graph_cp, q)
    cnt = 0
    for i in range(n):
        for j in range(m):
            if graph_cp[i][j] == 0:
                cnt += 1
    ans = max(ans,cnt)
print(ans)