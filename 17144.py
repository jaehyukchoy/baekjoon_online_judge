import math
r,c,t=map(int,input().split())
room=[list(map(int,input().split())) for _ in range(r)]
d=[(1,0),(-1,0),(0,1),(0,-1)]
for x in range(2,r-2):
    if room[x][0]==-1:
        aircon=x
        break

while t>0:
    t-=1
    tmp=[[0]*c for _ in range(r)]
    for x in range(r):
        for y in range(c):
            cnt=0
            for dx,dy in d:
                nx=x+dx
                ny=y+dy
                if room[x][y]>0 and 0<=nx<r and 0<=ny<c and room[nx][ny]!=-1:
                    tmp[nx][ny]+=math.floor(room[x][y]/5)
                    cnt+=1
            tmp[x][y]-=math.floor(room[x][y]/5)*cnt
    for x in range(r):
        for y in range(c):
            room[x][y]+=tmp[x][y]
    up=aircon
    down=aircon+1
    tmp=room[up][c-1]
    tmp2=room[0][c-1]
    tmp3=room[0][0]
    for y in range(c-1,1,-1):
        room[up][y]=room[up][y-1]
    room[up][1]=0
    for x in range(up-1):
        room[x][c-1]=room[x+1][c-1]
    room[up-1][c-1]=tmp
    for y in range(c-2):
        room[0][y]=room[0][y+1]
    room[0][c-2]=tmp2
    for x in range(up-1,1,-1):
        room[x][0]=room[x-1][0]
    room[1][0]=tmp3

    tmp=room[down][c-1]
    tmp2=room[r-1][c-1]
    tmp3=room[r-1][0]
    for y in range(c-1,1,-1):
        room[down][y]=room[down][y-1]
    room[down][1]=0
    for x in range(r-1,down+1,-1):
        room[x][c-1]=room[x-1][c-1]
    room[down+1][c-1]=tmp
    for y in range(c-2):
        room[r-1][y]=room[r-1][y+1]
    room[r-1][c-2]=tmp2
    for x in range(down+1,r-2):
        room[x][0]=room[x+1][0]
    room[r-2][0]=tmp3
ans=0
for x in range(r):
    for y in range(c):
        if room[x][y]>0:
            ans+=room[x][y]
print(ans)