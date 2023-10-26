import sys
input=sys.stdin.readline
l=list(input().rstrip())
n=len(l)
dp=[[0]*(n+1) for _ in range(n+1)]
for i in range(n):
    for j in range(1,n-i+1):
        if i==0:
            dp[j][j+i]=1
        elif i==1:
            if l[j-1]==l[j+i-1]:
                dp[j][j+i]=1
        else:
            if l[j-1]==l[j+i-1]:
                dp[j][j+i]=dp[j+1][j+i-1]

ddp=[2500]*(n+1)
ddp[0]=0
for i in range(1,n+1):
    for j in range(i,n+1):
        if dp[i][j]==1:
            ddp[j]=min(ddp[j],ddp[i-1]+1)
        else:
            ddp[j]=min(ddp[j],ddp[j-1]+1)
print(ddp[n])