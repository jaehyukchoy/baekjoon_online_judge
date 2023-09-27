k,n=map(int,input().split())
kk=[]
for _ in range(k):
    kk.append(int(input()))
kk.sort()
q=kk[k-1]
p=1
while p<=q:
    mi=(p+q)//2
    tmp=0
    for kkk in kk:
        tmp+=kkk//mi
    if tmp<n:
        q=mi-1
    else:
        p=mi+1
print(q)