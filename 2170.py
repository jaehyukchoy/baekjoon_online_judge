import sys
input=sys.stdin.readline
n=int(input())
point=[list(map(int,input().split())) for _ in range(n)]
point.sort()
l=[]
for x,y in point:
    flag=False
    for i,[lx,ly] in enumerate(l):
        if lx<=x<=ly or lx<=y<=ly:
            if x<lx:
                l[i][0]=x
            if y>ly:
                l[i][1]=y
            flag=True
            break
    if not flag:
        l.append([x,y])
ans=0
for lx,ly in l:
    ans+=ly-lx
print(ans)