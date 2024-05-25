from collections import Counter

def ccw(x1,y1,x2,y2,x3,y3):
    return (x2-x1)*(y3-y1)-(x3-x1)*(y2-y1)

def cross(x1,y1,x2,y2,x3,y3,x4,y4):
    if ccw(x1,y1,x2,y2,x3,y3)*ccw(x1,y1,x2,y2,x4,y4)<0 and ccw(x3,y3,x4,y4,x1,y1)*ccw(x3,y3,x4,y4,x2,y2)<0:
        return 1
    elif ccw(x1,y1,x2,y2,x3,y3)==0 and min(x1,x2)<=x3<=max(x1,x2) and min(y1,y2)<=y3<=max(y1,y2):
        return 1
    elif ccw(x1,y1,x2,y2,x4,y4)==0 and min(x1,x2)<=x4<=max(x1,x2) and min(y1,y2)<=y4<=max(y1,y2):
        return 1
    elif ccw(x3,y3,x4,y4,x1,y1)==0 and min(x3,x4)<=x1<=max(x3,x4) and min(y3,y4)<=y1<=max(y3,y4):
        return 1
    elif ccw(x3,y3,x4,y4,x2,y2)==0 and min(x3,x4)<=x2<=max(x3,x4) and min(y3,y4)<=y2<=max(y3,y4):
        return 1
    else:
        return 0
    
def find(x,parent):
    if x==parent[x]:
        return x
    parent[x]=find(parent[x],parent)
    return parent[x]

def union(a,b,parent):
    rootA=find(a,parent)
    rootB=find(b,parent)
    if rootA<rootB:
        parent[rootB]=rootA
    else:
        parent[rootA]=rootB

n=int(input())
lines=[list(map(int,input().split())) for _ in range(n)]
parent=[i for i in range(n)]

for i in range(n):
    x1,y1,x2,y2=lines[i]
    for j in range(i+1,n):
        x3,y3,x4,y4=lines[j]
        if cross(x1,y1,x2,y2,x3,y3,x4,y4):
            union(i,j,parent)

parent = [find(x,parent) for x in parent] # 이 부분이 필요한 이유...?

counter=Counter(parent) 
print(len(counter))
print(max(counter.values()))