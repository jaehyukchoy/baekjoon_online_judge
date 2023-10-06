import sys
from collections import deque
input=sys.stdin.readline
n=int(input())
WALL=-1
DOOR=1
MAN=2

def sol(q):
    v=[[-1]*(w+2) for _ in range(h+2)]
    v[q[0][0]][q[0][1]]=0
    while q:
        x,y=q.popleft()
        for dx,dy in [(0,1),(0,-1),(1,0),(-1,0)]:
            nx=x+dx
            ny=y+dy
            if 0<=nx<h+2 and 0<=ny<w+2 and v[nx][ny]==-1:
                if prison[nx][ny]==0:
                    v[nx][ny]=v[x][y]
                    q.appendleft((nx,ny))
                elif prison[nx][ny]==DOOR:
                    v[nx][ny]=v[x][y]+1
                    q.append((nx,ny))
    return v

for _ in range(n):
    q=deque()
    h,w=map(int,input().split())
    prison=[[0]*(w+2) for _ in range(h+2)]
    for i in range(h):
        tmp=input()
        for j in range(w):
            if tmp[j]=='#':
                prison[i+1][j+1]=DOOR
            elif tmp[j]=='*':
                prison[i+1][j+1]=WALL
            elif tmp[j]=='$':
                q.append((i+1,j+1))
    
    # 죄수1 에서 좌표로 가기위해 여는 문의 수
    a=sol(deque([q[0]])) 
    # 죄수2 에서 좌표로 가기위해 여는 문의 수
    b=sol(deque([q[1]])) 
    # 각 좌표에서 바깥까지 여는 문의 수
    c=sol(deque([(0,0)])) 
    
    # 결론: 죄수1, 죄수2가 각 좌표로 간 다음 각 좌표에서 바깥까지 감
    ans=10000
    for i in range(h+2):
        for j in range(w+2):
            if a[i][j]!=-1 and b[i][j]!=-1 and c[i][j]!=-1:
                if prison[i][j]==DOOR:
                    ans=min(ans,a[i][j]+b[i][j]+c[i][j]-2)
                else:
                    ans=min(ans,a[i][j]+b[i][j]+c[i][j])
    print(ans)