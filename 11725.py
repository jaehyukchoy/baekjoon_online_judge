import sys
from collections import deque

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N = int(input())
edges = dict()
for _ in range(N - 1):
    x, y = map(int, input().split())
    if x not in edges:
        edges[x] = []
    if y not in edges:
        edges[y] = []
    edges[x].append(y)
    edges[y].append(x)

parents = [0] * (N + 1)

q = deque([1])

while q:
    now = q.popleft()
    for next in edges[now]:
        if parents[next] == 0:
            parents[next] = now
            q.append(next)


for i in range(2, N + 1):
    print(parents[i])
