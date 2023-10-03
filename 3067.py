import sys
t=int(sys.stdin.readline())
n=[]
c=[]
v=[]
for i in range(t):
    n.append(int(sys.stdin.readline()))
    c.append(list(map(int,sys.stdin.readline().split())))
    v.append(int(sys.stdin.readline()))
for i in range(t):
    dp=[0]*(v[i]+1)
    dp[0]=1
    for cc in c[i]:
        for j in range(v[i]+1):
            if j-cc>=0:
                dp[j]+=dp[j-cc]
    print(dp[v[i]])