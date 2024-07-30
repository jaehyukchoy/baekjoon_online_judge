from collections import defaultdict
import sys, heapq
input = sys.stdin.readline

n = int(input())
m = int(input())

graph = defaultdict(dict)
for _ in range(m):
    a, b, c = map(int, input().split())
    if b in graph[a]:
        graph[a][b] = min(graph[a][b], c)
    else:
        graph[a][b] = c

def dijkstra(start):
    distances = [float('inf')] * (n+1)
    distances[start] = 0
    q = []
    heapq.heappush(q, [distances[start], start])
    while q:
        cur_distance, cur_dest = heapq.heappop(q)
        if distances[cur_dest] < cur_distance:
            continue
        for new_dest, new_distance in graph[cur_dest].items():
            distance = cur_distance + new_distance
            if distance < distances[new_dest]:
                distances[new_dest] = distance
                heapq.heappush(q, [distance, new_dest])
    return distances

for i in range(1, n+1):
    ans = dijkstra(i)
    ans = [0 if i==float('inf') else i for i in ans]
    print(' '.join(map(str, ans[1:])))
