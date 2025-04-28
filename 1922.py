import sys, heapq
input = sys.stdin.readline

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((c,b))
    graph[b].append((c,a))

q = []
total = 0
visited = [False] * (n+1)
heapq.heappush(q,(0,1))
while q:
    w, v = heapq.heappop(q)
    if visited[v]:
        continue
    visited[v] = True
    total += w
    for ww, vv in graph[v]:
        if not visited[vv]:
            heapq.heappush(q, (ww,vv))

print(total)