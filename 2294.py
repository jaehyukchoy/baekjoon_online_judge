import sys
n,k=map(int,sys.stdin.readline().split())
c=[]
for _ in range(n):
    c.append(int(sys.stdin.readline()))
dp=[k+1]*(k+1)
dp[0]=0
for cc in c:
    for i in range(1,k+1):
        if i-cc>=0:
            dp[i]=min(dp[i-cc]+1,dp[i])
if dp[k]==k+1:
    print(-1)
else:
    print(dp[k])