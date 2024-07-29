import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int,input().split()))

dp = [1]*N
dp_rev = [1]*N

for i in range(N):
    for j in range(i):
        if A[i] > A[j]:
            dp[i] = max(dp[i], dp[j]+1)
        
        p = N-1-i
        q = N-1-j
        if A[p] > A[q]:
            dp_rev[p] = max(dp_rev[p], dp_rev[q]+1)

ans=0
for x in range(N):
    ans=max(ans,dp[x]+dp_rev[x])
print(ans-1)