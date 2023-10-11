import sys
from collections import defaultdict
input=sys.stdin.readline
sys.setrecursionlimit(10**6)

def sol(i):
    if dp[i]!=-1:
        return dp[i]
    tmp=0
    for before_node in g[i]:
        tmp=max(tmp,sol(before_node))
    dp[i]=tmp+D[i-1]
    return dp[i]
    

for _ in range(int(input())):
    g=defaultdict(list)
    N,K=map(int,input().split())
    D=list(map(int,input().split()))
    for _ in range(K):
        X,Y=map(int,input().split())
        g[Y].append(X)
    W=int(input())
    dp=[-1]*(N+1)
    print(sol(W))