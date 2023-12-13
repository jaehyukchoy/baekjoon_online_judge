n,m,t=map(int,input().split())
pan=[list(map(int,input().split())) for _ in range(n)]
for _ in range(t):
    x,d,k=map(int,input().split())
    k=k if d==1 else m-k
    i=1
    while i*x-1<n:
        pan[i*x-1]=pan[i*x-1][k:]+pan[i*x-1][:k]
        i+=1
    to_del=set()
    for i in range(n):
        for j in range(-1,m-1):
            if pan[i][j]!=0 and pan[i][j]==pan[i][j+1]:
                to_del.add((i,j))
                to_del.add((i,j+1))
    for j in range(m):
        for i in range(n-1):
            if pan[i][j]!=0 and pan[i][j]==pan[i+1][j]:
                to_del.add((i,j))
                to_del.add((i+1,j))
    if to_del:
        for i,j in to_del:
            pan[i][j]=0
    else:
        s=c=0
        for i in range(n):
            for j in range(m):
                if pan[i][j]!=0:
                    c+=1
                    s+=pan[i][j]
        for i in range(n):
            for j in range(m):
                if pan[i][j]!=0:
                    if pan[i][j]>s/c:
                        pan[i][j]-=1
                    elif pan[i][j]<s/c:
                        pan[i][j]+=1
    
print(sum(map(sum,pan)))
