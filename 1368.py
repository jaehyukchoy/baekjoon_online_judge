import sys
input=sys.stdin.readline
n=int(input())
edges=[]
for i in range(n):
    edges.append((int(input()),0,i+1))
con=[list(map(int,input().split())) for _ in range(n)]

parent=[i for i in range(n+1)]

for i in range(n):
    for j in range(i+1,n):
        edges.append((con[i][j],i+1,j+1))
edges.sort()

def find(parent,x):
    if parent[x]==x:
        return x
    return find(parent,parent[x])

def union(parent,a,b):
    rootA=find(parent,a)
    rootB=find(parent,b)
    if rootA<rootB:
        parent[rootB]=rootA
    else:
        parent[rootA]=rootB

result=0
for c,i,j in edges:
    if find(parent,i)!=find(parent,j):
        union(parent,i,j)
        result+=c

print(result)