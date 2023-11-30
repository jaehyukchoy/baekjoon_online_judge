from collections import defaultdict
r,c,k=map(int,input().split())
a=[list(map(int,input().split())) for _ in range(3)]

def helper(row,col):
    for i in range(row):
        tmp=defaultdict(int)
        one=a[i]
        for o in one:
            if o!=0:
                tmp[o]+=1
        cnt=list(tmp.items())
        cnt.sort(key=lambda x:(x[1],x[0]))
        new=[]
        new_len=0
        for p,q in cnt:
            new.append(p)
            new.append(q)
            new_len+=2
        if new_len>100:
            new_len=100
        a[i]=new[:new_len]
        col=max(col,new_len)
    for i in range(row):
        while len(a[i])<col:
            a[i].append(0)
    return row,col


row=col=3
ans=0
while ans<=100 and (r>row or c>col or a[r-1][c-1]!=k):
    ans+=1
    if row>=col:
        row,col=helper(row,col)
    else:
        a=[list(x) for x in zip(*a)]
        col,row=helper(col,row)
        a=[list(x) for x in zip(*a)]

if ans<=100:
    print(ans)
else:
    print(-1)