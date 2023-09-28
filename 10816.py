n_len=int(input())
n=list(map(int,input().split()))
m_len=int(input())
m=list(map(int,input().split()))
n.sort()
ans=[]
for mm in m:
    p=0
    q=n_len-1
    x=-1
    while p<=q:
        mid=(p+q)//2
        if n[mid]<mm:
            p=mid+1
        elif n[mid]>mm:
            q=mid-1
        else:
            x=mid
            p=mid+1
    p=0
    q=n_len-1
    y=-1  
    while p<=q:
        mid=(p+q)//2
        if n[mid]<mm:
            p=mid+1
        elif n[mid]>mm:
            q=mid-1
        else:
            y=mid
            q=mid-1
    if x==-1:
        ans.append(0)
    else:
        ans.append(x-y+1)
for a in ans:
    print(a,end=' ')