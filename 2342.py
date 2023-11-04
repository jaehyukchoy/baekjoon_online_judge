import sys
input=sys.stdin.readline
ddr=list(map(int,input().split()))
ddr=ddr[:-1]
l=len(ddr)
dp=[[[float('inf')]*5 for _ in range(5)] for _ in range(l+1)]
dp[0][0][0]=0
for i in range(l):
    a=ddr[i]
    for j in range(5):
        if j!=a:
            for k in range(5):
                if k==0:
                        dp[i+1][a][j]=min(dp[i+1][a][j],dp[i][k][j]+2)
                elif k!=j:
                    if a==k:
                        dp[i+1][a][j]=min(dp[i+1][a][j],dp[i][k][j]+1) 
                    elif abs(a-k)==1 or abs(a-k)==3:
                        dp[i+1][a][j]=min(dp[i+1][a][j],dp[i][k][j]+3)
                    elif abs(a-k)==2:
                        dp[i+1][a][j]=min(dp[i+1][a][j],dp[i][k][j]+4)
            for k in range(5):
                if k==0:
                        dp[i+1][j][a]=min(dp[i+1][j][a],dp[i][j][k]+2)
                elif k!=j:
                    if a==k:
                        dp[i+1][j][a]=min(dp[i+1][j][a],dp[i][j][k]+1)
                    elif abs(a-k)==1 or abs(a-k)==3:
                        dp[i+1][j][a]=min(dp[i+1][j][a],dp[i][j][k]+3)
                    elif abs(a-k)==2:
                        dp[i+1][j][a]=min(dp[i+1][j][a],dp[i][j][k]+4)
print(min(map(min,dp[-1])))