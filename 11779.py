from collections import defaultdict
import sys, heapq
input = sys.stdin.readline

n = int(input())
m = int(input())

def dijkstra(s, e):
    p = [[] for _ in range(n+1)]
    p[s].append(s)
    d = [float('inf')] * (n+1)
    d[s] = 0
    q = []
    heapq.heappush(q, [0, s])
    while q:
        cur_d, cur = heapq.heappop(q)
        if cur_d > d[cur]:
            continue
        for next, next_d in g[cur].items():
            if cur_d + next_d < d[next]:
                tmp = p[cur][:]
                tmp.append(next)
                p[next] = tmp
                d[next] = cur_d + next_d
                heapq.heappush(q, [d[next], next])
    return d[e], p[e]

g = defaultdict(dict)
for _ in range(m):
    s, e, c = map(int, input().split())
    if e in g[s]:
        g[s][e] = min(g[s][e], c)
    else:
        g[s][e] = c
    
x, y = map(int, input().split())
a1, a2 = dijkstra(x, y)
print(a1)
print(len(a2))
print(' '.join(map(str, a2)))