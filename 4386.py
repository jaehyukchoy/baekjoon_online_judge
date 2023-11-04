import sys
input=sys.stdin.readline
n=int(input())
stars=[tuple(map(float,input().split())) for _ in range(n)]

def distance(p1,p2):
    x1,y1=p1
    x2,y2=p2
    return ((x1-x2)**2+(y1-y2)**2)**0.5

edges=[]
for i in range(n):
    for j in range(i+1,n):
        edges.append((distance(stars[i],stars[j]),i,j))

parents=[i for i in range(n)]

def find(parents,x):
    if parents[x]==x:
        return x
    return find(parents,parents[x])

def union(parents,a,b):
    rootA=find(parents,a)
    rootB=find(parents,b)
    if rootA<rootB:
        parents[rootB]=rootA
    else:
        parents[rootA]=rootB

edges.sort()
ans=0
for c,a,b in edges:
    if find(parents,a)!=find(parents,b):
        union(parents,a,b)
        ans+=c
print(ans)