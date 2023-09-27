input()
n=list(map(int,input().split()))
input()
m=list(map(int,input().split()))
n.sort()
for mm in m:
    ans=0
    p=0
    q=len(n)-1
    mi=(p+q)//2
    while p<=q:
        mi=(p+q)//2
        if n[mi]<mm:
            p=mi+1
        elif n[mi]>mm:
            q=mi-1
        else:
            ans=1
            break
    print(ans)