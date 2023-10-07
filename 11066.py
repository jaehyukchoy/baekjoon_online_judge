import sys
input=sys.stdin.readline
for t in range(int(input())):
    k=int(input())
    s=list(map(int,input().split()))
    dp=[[0]*k for _ in range(k)]
    for i in range(1,k):
        if i==1:
            for x in range(k-i):
                dp[x][x+i]=s[x]+s[x+1]
        else:
            for x in range(k-i):
                dp[x][x+i]=10**9
                tmp=sum(s[x:x+i+1])
                for j in range(i):
                    dp[x][x+i]=min(dp[x][x+i],dp[x][x+j]+dp[x+j+1][x+i]+tmp)
    print(dp[0][k-1])