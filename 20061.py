green=[[0]*4 for _ in range(6)]
blue=[[0]*6 for _ in range(4)]


def move(t,x,y):
    if t==1:
        i=0
        while i<6 and green[i][y]==0:
            i+=1
        green[i-1][y]=1
        j=0
        while j<6 and blue[x][j]==0:
            j+=1
        blue[x][j-1]=1

    elif t==2:
        i=0
        while i<6 and green[i][y]==0 and green[i][y+1]==0:
            i+=1
        green[i-1][y]=1
        green[i-1][y+1]=1
        j=0
        while j<6 and blue[x][j]==0:
            j+=1
        blue[x][j-1]=1
        blue[x][j-2]=1

    else:
        i=0
        while i<6 and green[i][y]==0:
            i+=1
        green[i-1][y]=1
        green[i-2][y]=1
        j=0
        while j<6 and blue[x][j]==0 and blue[x+1][j]==0:
            j+=1
        blue[x][j-1]=1
        blue[x+1][j-1]=1


def full_check():
    point=0

    for i in range(6):
        is_full=True
        for j in range(4):
            if green[i][j]==0:
                is_full=False
                break
        if is_full:
            point+=1
            for j in range(4):
                green[i][j]=0
            for ii in range(i,0,-1):
                for jj in range(4):
                    green[ii][jj]=green[ii-1][jj]
                    green[ii-1][jj]=0

    for j in range(6):
        is_full=True
        for i in range(4):
            if blue[i][j]==0:
                is_full=False
                break
        if is_full:
            point+=1
            for i in range(4):
                blue[i][j]=0
            for jj in range(j,0,-1):
                for ii in range(4):
                    blue[ii][jj]=blue[ii][jj-1]
                    blue[ii][jj-1]=0
    
    return point


def special():
    gcnt=0
    for i in range(2):
        for j in range(4):
            if green[i][j]==1:
                gcnt+=1
                break
    if gcnt>0:
        for i in range(5,-1+gcnt,-1):
            for j in range(4):
                green[i][j]=green[i-gcnt][j]
                green[i-gcnt][j]=0

    bcnt=0
    for j in range(2):
        for i in range(4):
            if blue[i][j]==1:
                bcnt+=1
                break
    if bcnt>0:
        for j in range(5,-1+bcnt,-1):
            for i in range(4):
                blue[i][j]=blue[i][j-bcnt]
                blue[i][j-bcnt]=0


ans=0
for _ in range(int(input())):
    t,x,y=map(int,input().split())
    move(t,x,y)
    ans+=full_check()
    special()

print(ans)
print(sum(map(sum,green))+sum(map(sum,blue)))