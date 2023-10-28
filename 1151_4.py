# 시간초과 코드임.
import sys
input=sys.stdin.readline
n,m=map(int,input().split())
k=[]
p=[]
for _ in range(n):
    tmp=list(map(int,input().split()))
    k.append(tmp[0])
    p.append(tmp[1:])

def move_sum(door,k,p):
    s=abs(door-p[0])
    for i in range(k-1):
        s+=abs(p[i]-p[i+1])
    s+=abs(door-p[k-1])
    return s

tot=sys.maxsize
for d in range(1,m+1):
    s=0
    for i in range(n):
        s+=move_sum(d,k[i],p[i])
    if s<tot:
        door=d
        tot=s
print(door)