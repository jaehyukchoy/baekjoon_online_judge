n = int(input())
p = list(map(int, input().split()))
dp = [0] * (n + 1)
dp[1] = p[0]
for i in range(2, n + 1):
    for j in range(1, i + 1):
        dp[i] = max(dp[i], p[j - 1] + dp[i - j])
print(dp[n])
