import sys
input = sys.stdin.readline
n = int(input())
dp = [-1, -1, -1, 1, -1, 1]
for i in range(6,n+1):
    d3 = dp[i-3]
    d5 = dp[i-5]
    if d3 != -1 and d5 != -1:
        dp.append(min(d3,d5)+1)
    elif d3 != -1:
        dp.append(d3+1)
    elif d5 != -1:
        dp.append(d5+1)
    else:
        dp.append(-1)
print(dp[n])