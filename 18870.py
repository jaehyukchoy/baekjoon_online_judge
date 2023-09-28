n=int(input())
x=list(map(int,input().split()))
s=list(set(x))
s.sort()
ans=[]
for xx in x:
    p=0
    q=len(s)-1
    while p<=q:
        mid=(p+q)//2
        if s[mid]<xx:
            p=mid+1
        elif s[mid]>xx:
            q=mid-1
        else:
            ans.append(mid)
            break
    
for a in ans:
    print(a,end=' ')