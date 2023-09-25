R,C,M=map(int,input().split())
shark=[[()]*C for _ in range(R)]
dir=[(-1,0),(1,0),(0,1),(0,-1)]
for _ in range(M):
    r,c,s,d,z=map(int,input().split())
    di,dj=dir[d-1]
    shark[r-1][c-1]=(s,di,dj,z)
man=-1
ans=0
while man<C-1:
    man+=1
    for i in range(R):
        if shark[i][man]:
            s,di,dj,z=shark[i][man]
            ans+=z
            shark[i][man]=()
            break
    move=[]
    for i in range(R):
        for j in range(C):
            if shark[i][j]:
                s,di,dj,z=shark[i][j]
                ni=i
                nj=j
                for t in range(s):
                    ni=ni+di
                    nj=nj+dj
                    if 0<=ni<R and 0<=nj<C:
                        continue
                    else:
                        di*=-1
                        dj*=-1 
                        ni=ni+2*di
                        nj=nj+2*dj
                move.append((ni,nj,s,di,dj,z))
    shark=[[()]*C for _ in range(R)]
    for i,j,s,di,dj,z in move:
        if shark[i][j]:
            ss,ddi,ddj,zz=shark[i][j]
            if z>zz:
                shark[i][j]=(s,di,dj,z)
        else:
            shark[i][j]=(s,di,dj,z)

print(ans)