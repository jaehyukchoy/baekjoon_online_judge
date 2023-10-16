import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**6)
def sol(s):
    global ans
    v[s]=True
    next=g[s]
    route.append(s)
    if not v[next]:
        sol(next)
    else:
        if next in route:
            ans+=len(route[route.index(next):])

for _ in range(int(input())):
    g=dict()
    n=int(input())
    choice=list(map(int,input().split()))
    for i in range(n):
        g[i+1]=choice[i]
    v=[False]*(n+1)
    ans=0
    for i in range(1,n+1):
        if not v[i]:
            route=[]
            sol(i)
    print(n-ans)