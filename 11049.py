n=int(input())
a=[tuple(map(int,input().split())) for _ in range(n)]
dp=[[0]*n for _ in range(n)]
for x in range(n-1):
    dp[x][x+1]=a[x][0]*a[x][1]*a[x+1][1]
for i in range(2,n):
    for x in range(n-i):
        dp[x][x+i]=2**31
        for j in range(i):
            dp[x][x+i]=min(dp[x][x+i],dp[x][x+j]+dp[x+j+1][x+i]+a[x][0]*a[x+j][1]*a[x+i][1])
print(dp[0][n-1])