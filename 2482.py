n = int(input())
k = int(input())
dp = [[0] * (n + 1) for _ in range(k + 1)]

for j in range(1, n + 1):
    dp[1][j] = j

for i in range(2, k + 1):
    for j in range(i, n + 1):
        if j == n:
            dp[i][j] = (dp[i][j - 1] + dp[i - 1][j - 3]) % 1000000003
        else:
            dp[i][j] = (dp[i][j - 1] + dp[i - 1][j - 2]) % 1000000003

print(dp[k][n])
