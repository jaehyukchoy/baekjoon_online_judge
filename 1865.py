from collections import defaultdict
import sys
input = sys.stdin.readline

def bellman_ford():
    d = [0] * (n+1)
    for i in range(n):
        for s, item in graph.items():
            for e, t in item.items():
                if d[e] > d[s] + t:
                    d[e] = d[s] + t
                    if i == n-1:
                        return True
    return False

tc = int(input())
for _ in range(tc):
    n, m, w = map(int, input().split())
    graph = defaultdict(dict)
    for _ in range(m):
        s, e, t = map(int, input().split())
        if e in graph[s]:
            graph[s][e] = min(graph[s][e], t)
        else:
            graph[s][e] = t
        if s in graph[e]:
            graph[e][s] = min(graph[e][s], t)
        else:
            graph[e][s] = t
                
    for _ in range(w):
        s, e, t = map(int, input().split())
        if e in graph[s]:
            graph[s][e] = min(graph[s][e], -t)
        else:
            graph[s][e] = -t

    if bellman_ford():
        print("YES")
    else:
        print("NO")