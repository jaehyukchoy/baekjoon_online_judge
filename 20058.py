from collections import deque
n,q=map(int,input().split())
ice=[list(map(int,input().split())) for _ in range(2**n)]
l=list(map(int,input().split()))
d=[(0,1),(1,0),(0,-1),(-1,0)]

def melt():
    to_melt=set()
    for i in range(2**n):
        for j in range(2**n):
            if ice[i][j]>0:
                cnt=0
                for di,dj in d:
                    ni,nj=i+di,j+dj
                    if 0<=ni<2**n and 0<=nj<2**n and ice[ni][nj]>0:
                        cnt+=1
                if cnt<3:
                    to_melt.add((i,j))
    
    for i,j in to_melt:
        ice[i][j]-=1
        
def rotate(x,y,l):
    i=x
    j=y
    k=0
    while k<2**(l-1):
        tmp=[]
        for _ in range(2**l-1-2*k):
            tmp.append(ice[i][j])
            j+=1
        for _ in range(2**l-1-2*k):
            tmp.append(ice[i][j])
            i+=1
        for _ in range(2**l-1-2*k):
            tmp.append(ice[i][j])
            j-=1
        for _ in range(2**l-1-2*k):
            tmp.append(ice[i][j])
            i-=1
        idx=-len(tmp)//4
        for _ in range(2**l-1-2*k):
            ice[i][j]=tmp[idx]
            j+=1
            idx+=1
        for _ in range(2**l-1-2*k):
            ice[i][j]=tmp[idx]
            i+=1
            idx+=1
        for _ in range(2**l-1-2*k):
            ice[i][j]=tmp[idx]
            j-=1
            idx+=1
        for _ in range(2**l-1-2*k):
            ice[i][j]=tmp[idx]
            i-=1
            idx+=1

        k+=1
        i+=1
        j+=1
 

def firestorm(l):
    if l>0:
        for i in range(0,2**n,2**l):
            for j in range(0,2**n,2**l):
                rotate(i,j,l)
    melt()
    
    
def bfs(x,y,v):
    q=deque([(x,y)])
    v[x][y]=True
    cnt=0
    while q:
        cnt+=1
        i,j=q.popleft()
        for di,dj in d:
            ni,nj=i+di,j+dj
            if 0<=ni<2**n and 0<=nj<2**n and not v[ni][nj] and ice[ni][nj]>0:
                q.append((ni,nj))
                v[ni][nj]=True
    return cnt

def biggest():
    v=[[False]*2**n for _ in range(2**n)]
    big=0
    for i in range(2**n):
        for j in range(2**n):
            if not v[i][j] and ice[i][j]>0:
                big=max(big,bfs(i,j,v))
    return big

for ll in l:
    firestorm(ll)

print(sum(map(sum,ice)))
print(biggest())