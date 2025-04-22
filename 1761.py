import math, sys
from collections import defaultdict
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())
tree = defaultdict(list)
for _ in range(N-1):
    v1, v2, d = map(int, input().split())
    tree[v1].append((v2, d))
    tree[v2].append((v1, d))


euler = []
depth = []
first = {}
visited = [False] * (N+1)
distance = [0] * (N+1)

def dfs(node, d, cost):
    visited[node] = True
    first[node] = len(euler)
    euler.append(node)
    depth.append(d)
    distance[node] = cost
    for child, weight in tree[node]:
        if not visited[child]:
            dfs(child, d + 1, cost + weight)
            euler.append(node)
            depth.append(d)

dfs(1, 0, 0)


n = len(depth)
log = math.floor(math.log2(n)) + 1
st = [[0] * log for _ in range(n)]


for i in range(n):
    st[i][0] = i


for j in range(1, log):
    for i in range(n - (1 << j) + 1):
        left = st[i][j-1]
        right = st[i + (1 << (j-1))][j-1]
        st[i][j] = left if depth[left] < depth[right] else right


log2 = [0] * (n + 1)
for i in range(2, n + 1):
    log2[i] = log2[i // 2] + 1


def lca(u, v):
    l, r = first[u], first[v]
    if l > r:
        l, r = r, l
    j = log2[r - l + 1]
    left = st[l][j]
    right = st[r - (1 << j) + 1][j]
    return euler[left] if depth[left] < depth[right] else euler[right]

for _ in range(int(input())):
    u, v = map(int, input().split())
    print(distance[u] + distance[v] - 2 * distance[lca(u,v)])