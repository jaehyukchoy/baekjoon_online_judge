import sys
t,w=map(int,sys.stdin.readline().split())
p=[]
for _ in range(t):
    p.append(int(sys.stdin.readline()))
dp=[[0]*(w+1) for _ in range(t+1)]
for i in range(1,t+1):
    for j in range(w+1):
        if j==0:
            if p[i-1]==1:
                dp[i][j]=dp[i-1][j]+1
            else:
                dp[i][j]=dp[i-1][j]
        else:
            if p[i-1]==j%2+1:
                dp[i][j]=max(dp[i-1][j-1],dp[i-1][j])+1
            else:
                dp[i][j]=max(dp[i-1][j-1],dp[i-1][j])
print(max(dp[t]))