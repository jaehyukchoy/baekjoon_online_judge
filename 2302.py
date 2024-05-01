n = int(input())
m = []
for _ in range((int(input()))):
    m.append(int(input()))
dp = [0] * 41
dp[0] = 1
dp[1] = 1
for i in range(2, 41):
    if i in m or (i - 1) in m:
        dp[i] = dp[i - 1]
    else:
        dp[i] = dp[i - 1] + dp[i - 2]
print(dp[n])
