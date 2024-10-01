import sys
import heapq
from collections import defaultdict

input = sys.stdin.readline
V, E = map(int, input().split())
g = defaultdict(list)

for _ in range(E):
    A, B, C = map(int, input().split())
    g[A].append((C, B))
    g[B].append((C, A))

def prim(start):
    visited = [False] * (V + 1) 
    q = []
    total_weight = 0
    heapq.heappush(q, (0, start)) 

    while q:
        weight, current_vertex = heapq.heappop(q)
        
        if not visited[current_vertex]:
            visited[current_vertex] = True
            total_weight += weight
            edges_in_mst += 1

            for next_weight, next_vertex in g[current_vertex]:
                if not visited[next_vertex]:
                    heapq.heappush(q, (next_weight, next_vertex))

    return total_weight

print(prim(1))
