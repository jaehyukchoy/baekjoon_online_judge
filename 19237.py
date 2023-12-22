n,m,k=map(int,input().split())
sea=[list(map(lambda x:[int(x),k],input().split())) for _ in range(n)]
d=[(),(-1,0),(1,0),(0,-1),(0,1)]
shark=dict()
for i in range(n):
    for j in range(n):
        if sea[i][j][0]>0:
            shark[sea[i][j][0]]=[(i,j)]
for s,dd in enumerate(list(map(int,input().split()))):
    shark[s+1].append(dd)
for s in range(1,m+1):
    tmp=dict()
    for i in range(1,5):
        tmp[i]=list(map(int,input().split()))
    shark[s].append(tmp)

ans=0
while ans<=1000:
    ans+=1
    
    tomove=[]
    for s,_ in shark.items():
        i,j=shark[s][0]
        available=set()
        for di,dj in [(-1,0),(1,0),(0,-1),(0,1)]:
            ni,nj=i+di,j+dj
            if 0<=ni<n and 0<=nj<n and (sea[ni][nj][0]==0 or sea[ni][nj][1]<=0):
                available.add((ni,nj))
        if not available:
            for di,dj in [(-1,0),(1,0),(0,-1),(0,1)]:
                ni,nj=i+di,j+dj
                if 0<=ni<n and 0<=nj<n and sea[ni][nj][0]==s:
                    available.add((ni,nj))
        for p in shark[s][2][shark[s][1]]:
            di,dj=d[p]
            ni,nj=i+di,j+dj
            if (ni,nj) in available:
                tomove.append([s,ni,nj,p])
                break
    
    for s,i,j,dd in tomove:
        shark[s][0]=(i,j)
        shark[s][1]=dd

    chk=dict()
    to_del=[]
    for s,_ in shark.items():
        if shark[s][0] not in chk:
            chk[shark[s][0]]=s
        else:
            if chk[shark[s][0]]>s:
                to_del.append(chk[shark[s][0]])
                chk[shark[s][0]]=s
            else:
                to_del.append(s)
    for s in to_del:
        del(shark[s])
        
    for i in range(n):
        for j in range(n):
            sea[i][j][1]-=1

    for s,_ in shark.items():
        i,j=shark[s][0]
        sea[i][j]=[s,k]

    if len(shark)==1:
        break

print(ans) if ans<=1000 else print(-1)