import sys

sys.setrecursionlimit(10**6)

input = sys.stdin.readline
N = int(input())
tree = [[] for _ in range(N + 1)]

for _ in range(N - 1):
    u, v = map(int, input().split())
    tree[u].append(v)
    tree[v].append(u)

visited = [False] * (N + 1)
dp = [[0, 0] for _ in range(N + 1)]


def dfs(n):
    visited[n] = True
    dp[n][1] = 1

    for node in tree[n]:
        if not visited[node]:
            dfs(node)
            dp[n][0] += dp[node][1]
            dp[n][1] += min(dp[node][0], dp[node][1])


dfs(1)

print(min(dp[1][1], dp[1][0]))
