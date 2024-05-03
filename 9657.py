n = int(input())
dp = [0] * (n + 1)
dp[1] = 0
for i in range(2, n + 1):
    if i == 2:
        dp[2] = 1
    elif i == 3:
        dp[3] = 0
    elif i == 4:
        dp[4] = 0
    else:
        dp[i] = (max(dp[i - 1], dp[i - 3], dp[i - 4]) + 1) % 2
if dp[n] == 0:
    print("SK")
else:
    print("CY")
