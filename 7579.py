import sys
input=sys.stdin.readline
N,M=map(int,input().split())
m=list(map(int,input().split()))
c=list(map(int,input().split()))
sc=sum(c)
dp=[[0]*(sc+1) for _ in range(N+1)]
#dp[i][j]: i까지 j(c)로 최대 m
ans=sc
for i in range(1,N+1):
    for j in range(sc+1):
        if c[i-1]>j:
            dp[i][j]=dp[i-1][j]
        else:
            dp[i][j]=max(m[i-1]+dp[i-1][j-c[i-1]],dp[i-1][j])
        if dp[i][j]>=M:
            ans=min(ans,j)
print(ans)