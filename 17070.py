import sys
input = sys.stdin.readline

N = int(input())
house = [list(map(int, input().split())) for _ in range(N)]


dp = [[[0] * 3 for _ in range(N)] for _ in range(N)]
dp[0][1][0] = 1

def dfs(x, y, d):
    if x < 0 or y < 0 or house[x][y] == 1:
        return 0
    if dp[x][y][d] != 0:
        return dp[x][y][d]
    if d == 0:
        dp[x][y][d] = dfs(x, y-1, 0) + dfs(x, y-1, 2)
    if d == 1:
        dp[x][y][d] = dfs(x-1, y, 1) + dfs(x-1, y, 2)
    if d == 2:
        if 0 <= x-1 and 0 <= y-1 and house[x-1][y] == 0 and house[x][y-1] == 0:
            dp[x][y][d] = dfs(x-1, y-1, 0) + dfs(x-1, y-1, 1) + dfs(x-1, y-1, 2)
    return dp[x][y][d]

dfs(N-1, N-1, 0)
dfs(N-1, N-1, 1)
dfs(N-1, N-1, 2)

print(sum(dp[N-1][N-1]))