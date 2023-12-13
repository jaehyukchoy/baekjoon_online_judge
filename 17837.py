n,k=map(int,input().split())
board=[list(map(int,input().split())) for _ in range(n)]
d=[(),(0,1),(0,-1),(-1,0),(1,0)]
m=[]
p=[]
place=[[[] for _ in range(n)] for _ in range(n)]
for i in range(k):
    x,y,t=map(int,input().split())
    m.append(t)
    p.append((x-1,y-1))
    place[x-1][y-1].append(i)

ans=0
while ans<=1000:
    ans+=1
    for i in range(k):
        x,y=p[i]
        dx,dy=d[m[i]]
        nx,ny=x+dx,y+dy
        if not (0<=nx<n and 0<=ny<n) or board[nx][ny]==2:
            m[i] = m[i]-1 if m[i]%2==0 else m[i]+1
            dx,dy=d[m[i]]
            nx,ny=x+dx,y+dy

        if 0<=nx<n and 0<=ny<n and (board[nx][ny]==0 or board[nx][ny]==1):
            idx=place[x][y].index(i)
            left=place[x][y][:idx]
            togo=place[x][y][idx:]
            place[x][y]=left
            place[nx][ny] = place[nx][ny]+togo if board[nx][ny]==0 else place[nx][ny]+togo[::-1]
            for tg in togo:
                p[tg]=(nx,ny)
        for a in range(n):
            for b in range(n):
                if len(place[a][b])>=4:
                    print(ans)
                    exit()

print(-1)