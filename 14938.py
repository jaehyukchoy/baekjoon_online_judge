from collections import defaultdict
import sys, heapq
input = sys.stdin.readline

n, m, r = map(int, input().split())
t = list(map(int, input().split()))
graph = defaultdict(dict)
for _ in range(r):
    a, b, l = map(int, input().split())
    graph[a][b] = l
    graph[b][a] = l

def dijkstra(s):
    d = [float('inf')] * (n+1)
    d[s] = 0
    q = []
    heapq.heappush(q, [d[s], s])
    while q:
        c_d, c_dest = heapq.heappop(q)
        if c_d > d[c_dest]:
            continue
        for n_dest, n_d in graph[c_dest].items():
            n_d += c_d
            if n_d < d[n_dest]:
                d[n_dest] = n_d
                heapq.heappush(q, [n_d, n_dest])
    return d

ans = []
for i in range(1, n+1):
    arr = dijkstra(i)
    tmp = 0
    for idx, val in enumerate(arr):
        if val <= m:
            tmp += t[idx-1]
    ans.append(tmp)

print(max(ans))