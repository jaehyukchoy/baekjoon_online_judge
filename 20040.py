import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**6)
n,m=map(int,input().split())

parents=[i for i in range(n)]

def find(parents,x):
    if parents[x]!=x:
        parents[x]=find(parents,parents[x])
    return parents[x]

def sol():
    for i in range(m):
        a,b=map(int,input().split())
        rootA=find(parents,a)
        rootB=find(parents,b)
        if rootA==rootB:
            print(i+1)
            return
        if rootA<rootB:
            parents[rootA]=rootB
        else:
            parents[rootB]=rootA
    print(0)
    return
sol()