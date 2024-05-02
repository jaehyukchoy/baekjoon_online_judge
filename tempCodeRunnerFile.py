n = int(input())
dp = [0] * (abs(n) + 1)
dp[0] = 0
for i in range(1, abs(n) + 1):
    if i == 1:
        dp[i] = 1
    else:
        dp[i] = (dp[i - 1] + dp[i - 2]) % 1000000000
if n == 0:
    a = 0
elif n > 0 or -n % 2 == 1:
    a = 1
else:
    a = -1
print(a)
print(dp[abs(n)])
