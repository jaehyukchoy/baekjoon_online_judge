import math
n=int(input())
sand=[list(map(int,input().split())) for _ in range(n)]

def spread(x,y,d):
    out=0
    p1=math.floor(sand[x][y]*0.01)
    p2=math.floor(sand[x][y]*0.02)
    p5=math.floor(sand[x][y]*0.05)
    p7=math.floor(sand[x][y]*0.07)
    p10=math.floor(sand[x][y]*0.1)
    a=sand[x][y]-2*(p1+p2+p7+p10)-p5
    if d==0:
        dd=[(-2,0,p2),(-1,-1,p10),(-1,0,p7),(-1,1,p1),(0,-2,p5),(0,-1,a),(1,-1,p10),(1,0,p7),(1,1,p1),(2,0,p2)]
    elif d==1:
        dd=[(-1,-1,p1),(-1,1,p1),(0,-2,p2),(0,-1,p7),(0,1,p7),(0,2,p2),(1,-1,p10),(1,0,a),(1,1,p10),(2,0,p5)]
    elif d==2:
        dd=[(-2,0,p2),(-1,-1,p1),(-1,0,p7),(-1,1,p10),(0,1,a),(0,2,p5),(1,-1,p1),(1,0,p7),(1,1,p10),(2,0,p2)]
    else:
        dd=[(-2,0,p5),(-1,-1,p10),(-1,0,a),(-1,1,p10),(0,-2,p2),(0,-1,p7),(0,1,p7),(0,2,p2),(1,-1,p1),(1,1,p1)]

    for dx,dy,s in dd:
        nx,ny=x+dx,y+dy
        if 0<=nx<n and 0<=ny<n:
            sand[nx][ny]+=s
        else:
            out+=s

    sand[x][y]=0
    return out

helper=[]
idx=1
while len(helper)<=n**2:
    for j in range(idx):
        helper.append(0)
    for j in range(idx):
        helper.append(1)
    for j in range(idx+1):
        helper.append(2)
    for j in range(idx+1):
        helper.append(3)
    idx+=2

ans=0
x=y=n//2
move=[(0,-1),(1,0),(0,1),(-1,0)]
for i in range(n**2-1):
    d=helper[i]
    x+=move[d][0]
    y+=move[d][1]
    ans+=spread(x,y,d)
print(ans)