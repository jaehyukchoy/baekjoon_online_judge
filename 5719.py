from collections import defaultdict, deque
import sys, heapq
input = sys.stdin.readline


def dijkstra(n, graph, start):
    dist = [float('inf')] * n
    dist[start] = 0
    heap = [(0, start)]
    prev = [[] for _ in range(n)]

    while heap:
        d, u = heapq.heappop(heap)
        if d > dist[u]:
            continue
        for v, cost in graph[u]:
            new_dist = d + cost
            if new_dist < dist[v]:
                dist[v] = new_dist
                heapq.heappush(heap, (new_dist, v))
                prev[v] = [u]
            elif new_dist == dist[v]:
                prev[v].append(u)

    return dist, prev


def remove_shortest_edges(graph, prev, dest):
    q = deque([dest])
    visited = [False] * len(graph)

    while q:
        v = q.popleft()
        if visited[v]:
            continue
        visited[v] = True
        for u in prev[v]:
            graph[u] = [(to, cost) for (to, cost) in graph[u] if to != v]
            q.append(u)



while True:
    N, M = map(int, input().split())
    if N == 0 and M == 0:
        break
    S, D = map(int, input().split())

    graph = [[] for _ in range(N)]
    for _ in range(M):
        U, V, P = map(int, input().split())
        graph[U].append((V, P))

    dist, prev = dijkstra(N, graph, S)

    remove_shortest_edges(graph, prev, D)

    new_dist, _ = dijkstra(N, graph, S)
    print(new_dist[D] if new_dist[D] != float('inf') else -1)

