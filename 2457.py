import sys
input=sys.stdin.readline
n=int(input())
flowers=[]
for _ in range(n):
    sm,sd,em,ed=map(int,input().split())
    s=e=0
    for i in range(1,sm):
        if i==1 or i==3 or i==5 or i==7 or i==8 or i==10 or i==12:
            s+=31
        elif i==4 or i==6 or i==9 or i==11:
            s+=30
        else:
            s+=28
    s+=sd
    for i in range(1,em):
        if i==1 or i==3 or i==5 or i==7 or i==8 or i==10 or i==12:
            e+=31
        elif i==4 or i==6 or i==9 or i==11:
            e+=30
        else:
            e+=28
    e+=ed
    flowers.append((s,e))
now=60
ans=0
while now<335:
    m=0
    flowers.sort()
    for i in range(n):
        if flowers[i][0]<=now:
            m=max(m,flowers[i][1])
    if m==now:
        ans=0
        break
    now=m
    ans+=1
print(ans)