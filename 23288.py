from collections import deque
n, m, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
dice = [[0, 2, 0], 
        [4, 1, 3], 
        [0, 5, 0], 
        [0, 6, 0]]
direction=[(0,1),(1,0),(0,-1),(-1,0)]
d=0
x=y=0
ans=0

def bfs(q):
    global cnt
    while q:
        i,j=q.popleft()
        for di,dj in direction:
            ni=i+di
            nj=j+dj
            if 0<=ni<n and 0<=nj<m and not v[ni][nj] and board[i][j]==board[ni][nj]:
                cnt+=1
                v[ni][nj]=True
                q.append((ni,nj))

def move(to):
    if to==0:
        tmp=dice[1][2]
        dice[1][2]=dice[1][1]
        dice[1][1]=dice[1][0]
        dice[1][0]=dice[3][1]
        dice[3][1]=tmp
    elif to==1:
        tmp=dice[3][1]
        dice[3][1]=dice[2][1]
        dice[2][1]=dice[1][1]
        dice[1][1]=dice[0][1]
        dice[0][1]=tmp
    elif to==2:
        tmp=dice[1][0]
        dice[1][0]=dice[1][1]
        dice[1][1]=dice[1][2]
        dice[1][2]=dice[3][1]
        dice[3][1]=tmp
    else:
        tmp=dice[0][1]
        dice[0][1]=dice[1][1]
        dice[1][1]=dice[2][1]
        dice[2][1]=dice[3][1]
        dice[3][1]=tmp

while k>0:
    k-=1
    dx,dy=direction[d]
    nx=x+dx
    ny=y+dy
    if not (0<=nx<n and 0<=ny<m):
        nx=x-dx
        ny=y-dy
        d=(d+2)%4
    move(d)
    v=[[False]*m for _ in range(n)]
    cnt=1
    v[nx][ny]=True
    bfs(deque([(nx,ny)]))
    ans+=cnt*board[nx][ny]
    if board[nx][ny]<dice[3][1]:
        d=(d+1)%4
    elif board[nx][ny]>dice[3][1]:
        d=(d+3)%4
    x=nx
    y=ny
print(ans)