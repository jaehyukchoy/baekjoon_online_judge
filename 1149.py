import sys
n=int(sys.stdin.readline())
rgb=[list(map(int,sys.stdin.readline().split())) for _ in range(n)]
dp=[[0]*3 for _ in range(n)]
for i in range(n):
    if i==0:
        dp[i][0]=rgb[i][0]
        dp[i][1]=rgb[i][1]
        dp[i][2]=rgb[i][2]
    else:    
        dp[i][0]=min(dp[i-1][1]+rgb[i][0],dp[i-1][2]+rgb[i][0])
        dp[i][1]=min(dp[i-1][0]+rgb[i][1],dp[i-1][2]+rgb[i][1])
        dp[i][2]=min(dp[i-1][0]+rgb[i][2],dp[i-1][1]+rgb[i][2])
print(min(dp[n-1]))