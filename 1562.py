n=int(input())
dp=[[[0]*1024 for _ in range(10)] for _ in range(n+1)]
for i in range(1,n+1):
    for j in range(10):
        if i==1:
            dp[i][j][pow(2,j)]=1
        else:
            if j!=0:
                for k in range(1024):
                    dp[i][j][k|pow(2,j)]+=dp[i-1][j-1][k]
            if j!=9:
                for k in range(1024):
                    dp[i][j][k|pow(2,j)]+=dp[i-1][j+1][k]

ans=0
for j in range(1,10):
    ans+=dp[n][j][1023]
    ans%=1000000000
print(ans)