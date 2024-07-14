import sys, heapq
input = sys.stdin.readline

N = int(input())
M = int(input())
bus = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    bus[a].append([b, c])

start, end = map(int, input().split())

def dijkstra(start, end):
    distances = [int(1e9)] * (N + 1)
    distances[start] = 0
    q = []
    heapq.heappush(q, [distances[start], start])
    
    while q:
        cur_distance, cur = heapq.heappop(q)
        if cur_distance > distances[cur]:
            continue
        for new, d in bus[cur]:
            new_distance = cur_distance + d
            if new_distance < distances[new]:
                distances[new] = new_distance
                heapq.heappush(q, [new_distance, new])

    return distances[end]

print(dijkstra(start, end))