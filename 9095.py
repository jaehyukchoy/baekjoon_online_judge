import sys
input = sys.stdin.readline
t = int(input())
dp = [1,2,4]
idx = 3
answer = []
for _ in range(t):
    n = int(input())
    while idx < n:
        dp.append(dp[idx-1] + dp[idx-2] + dp[idx-3])
        idx += 1
    answer.append(dp[n-1])
for a in answer:
    print(a)