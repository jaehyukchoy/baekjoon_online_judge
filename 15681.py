import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
n, r, q = map(int, input().split())
tree = [[] for _ in range(n+1)]
for _ in range(n-1):
    u, v = map(int, input().split())
    tree[u].append(v)
    tree[v].append(u)

ans = [-1] * (n+1)
def dp(x):
    if ans[x] != -1:
        return ans[x]
    ans[x] = 1
    for xx in tree[x]:
        if ans[xx] == -1:
            ans[x] += dp(xx)
    return ans[x]

dp(r)
l = [int(input()) for _ in range(q)]
for ll in l:
    print(ans[ll])