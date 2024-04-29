n, m = map(int, input().split())
x = list(map(int, input().split()))
dp = [0] * (n + 1)
dp[1] = x[0]
for i in range(2, n + 1):
    dp[i] = dp[i - 1] + x[i - 1]
for _ in range(m):
    i, j = map(int, input().split())
    print(dp[j] - dp[i - 1])
