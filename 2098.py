import sys,math
input=sys.stdin.readline
n=int(input())
w=[list(map(int,input().split())) for _ in range(n)]
dp=[[-1]*(1<<n) for _ in range(n)] # dp[현재노드][방문노드] 출발노드로 가는 최소값
def dfs(s,v):
    if v==(1<<n)-1:
        return w[s][0] if w[s][0]!=0 else math.inf
    if dp[s][v]==-1:
        tmp=math.inf
        for i in range(1,n):
            if w[s][i]!=0 and v&(1<<i)==0:
                tmp=min(tmp,dfs(i,v|(1<<i))+w[s][i])
        dp[s][v]=tmp
    return dp[s][v]
print(dfs(0,1))