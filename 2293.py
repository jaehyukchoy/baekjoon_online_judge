import sys
n,k=map(int,sys.stdin.readline().split())
c=[]
for _ in range(n):
    c.append(int(sys.stdin.readline()))
dp=[0]*(k+1)
dp[0]=1
for cc in c:
    for i in range(1,k+1):
        if i-cc>=0:
            dp[i]+=dp[i-cc]
print(dp[k])