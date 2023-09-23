from collections import deque
n=int(input())
sea=[list(map(int,input().split())) for _ in range(n)]

d=[(1,0),(-1,0),(0,1),(0,-1)]   

def bfs(q,shark):
    global cnt
    checklist=[]
    checkpoint=n**2
    while q:
        x,y,t=q.popleft()
        if t>checkpoint:
            sea[shark[0]][shark[1]]=0
            checklist.sort()
            sea[checklist[0][0]][checklist[0][1]]=9
            cnt+=1
            return t
        for dx,dy in d:
            nx=x+dx
            ny=y+dy
            if 0<=nx<n and 0<=ny<n and not v[nx][ny]:
                if sea[nx][ny]==0 or sea[nx][ny]==size:
                    v[nx][ny]=True
                    q.append((nx,ny,t+1))
                elif sea[nx][ny]<size:
                    checkpoint=t
                    checklist.append((nx,ny))
    
    if checklist:
        sea[shark[0]][shark[1]]=0
        checklist.sort()
        sea[checklist[0][0]][checklist[0][1]]=9
        cnt+=1
        return t+1
        
    return False
cnt=0
size=2
ans=0
while True:
    v=[[False]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if sea[i][j]==9:
                q=deque([(i,j,0)])
                v[i][j]=True
                shark=(i,j)
    tmp=bfs(q,shark)
    if not tmp:
        break
    ans+=tmp
    if cnt==size:
        size+=1
        cnt=0


print(ans)