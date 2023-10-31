import sys
from collections import deque
input=sys.stdin.readline
n,m=map(int,input().split())
g=[list(map(int,input().split())) for _ in range(n)]

def make_island():
    v=[[False]*m for _ in range(n)]
    r=[[0]*m for _ in range(n)]
    island=0
    for i in range(n):
        for j in range(m):
            if g[i][j]==1 and not v[i][j]:
                q=deque([(i,j)])
                island+=1
                while q:
                    x,y=q.popleft()
                    r[x][y]=island
                    for dx,dy in [(1,0),(0,1),(-1,0),(0,-1)]:
                        nx=x+dx
                        ny=y+dy
                        if 0<=nx<n and 0<=ny<m and g[nx][ny]==1 and not v[nx][ny]:
                            v[nx][ny]=True
                            q.append((nx,ny))
    return r,island

def make_edge(g):
    edges=[]
    for i in range(n):
        b_island=-1
        b_idx=-1
        for j in range(m):
            if g[i][j]!=0:
                if b_island!=-1 and g[i][j]!=b_island and j-b_idx>2:
                    edges.append((j-b_idx-1,b_island,g[i][j]))
                b_island=g[i][j]
                b_idx=j
    for j in range(m):
        b_island=-1
        b_idx=-1
        for i in range(n):
            if g[i][j]!=0:
                if b_island!=-1 and g[i][j]!=b_island and i-b_idx>2:
                    edges.append((i-b_idx-1,b_island,g[i][j]))
                b_island=g[i][j]
                b_idx=i
    return edges

island,island_cnt=make_island()
parent = [i for i in range(island_cnt + 1)]
edges=make_edge(island)
edges.sort()

def find(parent, x):
    if parent[x] == x:
        return x
    parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    rootA = find(parent, a)
    rootB = find(parent, b)
    if rootA < rootB:
        parent[rootB] = rootA
    else:
        parent[rootA] = rootB

result = 0
for edge in edges:
    cost, a, b = edge
    if find(parent, a) != find(parent, b):
        union(parent, a, b)
        result += cost

for idx in range(1,island_cnt):
    if find(parent,idx)!=find(parent,idx+1):
        result=-1
        break

print(result)