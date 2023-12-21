from copy import deepcopy
sea=[]
d=[(-1,0),(-1,-1),(0,-1),(1,-1),(1,0),(1,1),(0,1),(-1,1)]
for i in range(4):
    a1,b1,a2,b2,a3,b3,a4,b4=map(int,input().split())
    sea.append([[a1,b1-1],[a2,b2-1],[a3,b3-1],[a4,b4-1]])

SHARK=0
DEAD=-1

def fish_move():
    for fish in range(1,17):
        for i in range(4):
            flag=False
            for j in range(4):
                if sea[i][j][0]==fish:
                    flag=True
                    dd=sea[i][j][1]
                    for di in range(8):
                        nd=(dd+di)%8
                        di,dj=d[nd]
                        ni,nj=i+di,j+dj
                        if 0<=ni<4 and 0<=nj<4 and sea[ni][nj][0]!=SHARK:
                            sea[i][j]=sea[ni][nj]
                            sea[ni][nj]=[fish,nd]
                            break
                if flag:
                    break
            if flag:
                break


def shark_move(p):
    for i in range(4):
        for j in range(4):
            if sea[i][j][0]==SHARK:
                di,dj=d[sea[i][j][1]]
                ni,nj=i+p*di,j+p*dj
                if 0<=ni<4 and 0<=nj<4 and sea[ni][nj][0]>=1:
                    to_die=sea[ni][nj][0]
                    sea[ni][nj][0]=SHARK
                    sea[i][j][0]=DEAD
                    return to_die
    return 0


def sol(point):
    global ans,sea
    ans=max(ans,point)
    for p in range(1,4):
        backup=deepcopy(sea)
        fish_move()
        sp=shark_move(p)
        if sp!=0:
            sol(point+sp)
        sea=backup


ans=sea[0][0][0]
sea[0][0][0]=SHARK
sol(ans)
print(ans)