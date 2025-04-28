import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
n = int(input())
forest = [list(map(int, input().split())) for _ in range(n)]

dp = [[0] * n for _ in range(n)]

def dfs(i,j):
    if dp[i][j]:
        return dp[i][j]
    
    dp[i][j] = 1
    for di, dj in [(1,0),(0,1),(-1,0),(0,-1)]:
        ni, nj = i+di, j+dj
        if 0<=ni<n and 0<=nj<n and forest[i][j]<forest[ni][nj]:
            dp[i][j] = max(dp[i][j], dfs(ni,nj) + 1)
    
    return dp[i][j]
    
ans = 0

for i in range(n):
    for j in range(n):
        ans = max(ans, dfs(i,j))

print(ans)