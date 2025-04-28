import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

dp = [0] * n
dp[0] = arr[0]


for i in range(1, n):
    dp[i] = max(dp[i-1] + arr[i], arr[i])

answer = max(dp)

remove = [0] * n
remove[0] = arr[0]
for i in range(1, n):
    remove[i] = max(dp[i-1], remove[i-1] + arr[i])

answer = max(answer, max(remove))

print(answer)
