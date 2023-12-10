from collections import defaultdict

n=int(input())
cls=[[0]*n for _ in range(n)]

like=defaultdict(list)
for _ in range(n**2):
    student,a,b,c,d=map(int,input().split())
    like[student].append(a)
    like[student].append(b)
    like[student].append(c)
    like[student].append(d)

    mcnt=0
    available=[]
    for i in range(n):
        for j in range(n):
            if cls[i][j]==0:
                emp=0
                cnt=0
                for di,dj in [(1,0),(0,1),(-1,0),(0,-1)]:
                    ni,nj=i+di,j+dj
                    if 0<=ni<n and 0<=nj<n:
                        if cls[ni][nj] in like[student]:
                            cnt+=1    
                        elif cls[ni][nj]==0:
                            emp+=1

                if cnt>mcnt:
                    mcnt=cnt
                    available=[[i,j,emp]]
                elif cnt==mcnt:
                    available.append([i,j,emp])

    available.sort(key=lambda x:(-x[2],x[0],x[1]))
    x,y,_=available[0]
    cls[x][y]=student

point=[0,1,10,100,1000]
ans=0
for i in range(n):
    for j in range(n):
        cnt=0
        for di,dj in [(1,0),(0,1),(-1,0),(0,-1)]:
            ni,nj=i+di,j+dj
            if 0<=ni<n and 0<=nj<n and cls[ni][nj] in like[cls[i][j]]:
                cnt+=1
        ans+=point[cnt]
print(ans)