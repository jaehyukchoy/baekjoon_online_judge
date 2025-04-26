import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
tree = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

LOG = 17
parent = [[-1] * (LOG+1) for _ in range(n+1)]
depth = [0] * (n+1)

def dfs(cur, p):
    for next in tree[cur]:
        if next != p:
            depth[next] = depth[cur] + 1
            parent[next][0] = cur
            dfs(next, cur)

dfs(1, -1)

for j in range(1, LOG+1):
    for i in range(1, n+1):
        if parent[i][j-1] != -1:
            parent[i][j] = parent[parent[i][j-1]][j-1]

def lca(u, v):
    if depth[u] < depth[v]:
        u, v = v, u

    for j in reversed(range(LOG+1)):
        if depth[u] - depth[v] >= (1 << j):
            u = parent[u][j]

    if u == v:
        return u

    for j in reversed(range(LOG+1)):
        if parent[u][j] != -1 and parent[u][j] != parent[v][j]:
            u = parent[u][j]
            v = parent[v][j]

    return parent[u][0]

m = int(input())
for _ in range(m):
    u, v = map(int, input().split())
    print(lca(u, v))
