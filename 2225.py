n, k = map(int, input().split())
MOD = 1_000_000_000

dp = [[0]*(k+1) for _ in range(n+1)]

for i in range(n+1):
    dp[i][1] = 1

for i in range(n+1):
    for j in range(2,k+1):
        for p in range(i+1):
            dp[i][j] += dp[i-p][j-1] 

print(dp[n][k]%MOD)