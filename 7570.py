import sys
input=sys.stdin.readline
n=int(input())
c=list(map(int,input().split()))
dp=[0]*(n+1)
for i in range(n):
    dp[c[i]]=dp[c[i]-1]+1
print(n-max(dp))