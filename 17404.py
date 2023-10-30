import sys
input=sys.stdin.readline
n=int(input())
rgb=[list(map(int,input().split())) for _ in range(n)]
dp=[[0]*3 for _ in range(n)]
ans=sys.maxsize
for start in range(3):
    if start==0:
        dp[0][0]=rgb[0][0]
        dp[0][1]=sys.maxsize
        dp[0][2]=sys.maxsize
    elif start==1:
        dp[0][0]=sys.maxsize
        dp[0][1]=rgb[0][1]
        dp[0][2]=sys.maxsize
    else:
        dp[0][0]=sys.maxsize
        dp[0][1]=sys.maxsize
        dp[0][2]=rgb[0][2]
    for i in range(1,n):
        if i==n-1:
            if start==0:
                dp[i][0]=sys.maxsize
                dp[i][1]=min(dp[i-1][0]+rgb[i][1],dp[i-1][2]+rgb[i][1])
                dp[i][2]=min(dp[i-1][0]+rgb[i][2],dp[i-1][1]+rgb[i][2])
            elif start==1:
                dp[i][0]=min(dp[i-1][1]+rgb[i][0],dp[i-1][2]+rgb[i][0])
                dp[i][1]=sys.maxsize
                dp[i][2]=min(dp[i-1][0]+rgb[i][2],dp[i-1][1]+rgb[i][2])
            else:
                dp[i][0]=min(dp[i-1][1]+rgb[i][0],dp[i-1][2]+rgb[i][0])
                dp[i][1]=min(dp[i-1][0]+rgb[i][1],dp[i-1][2]+rgb[i][1])
                dp[i][2]=sys.maxsize
        else:    
            dp[i][0]=min(dp[i-1][1]+rgb[i][0],dp[i-1][2]+rgb[i][0])
            dp[i][1]=min(dp[i-1][0]+rgb[i][1],dp[i-1][2]+rgb[i][1])
            dp[i][2]=min(dp[i-1][0]+rgb[i][2],dp[i-1][1]+rgb[i][2])
    ans=min(ans,min(dp[n-1]))
print(ans)