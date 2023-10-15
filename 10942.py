import sys
input=sys.stdin.readline
n=int(input())
l=list(map(int,input().split()))
m=int(input())
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
for _ in range(m):
    s,e=map(int,input().split())
    print(dp[s][e])