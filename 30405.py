import sys
input=sys.stdin.readline
n,m=map(int,input().split())
a=[]
for _ in range(n):
    tmp=list(map(int,input().split()))
    a.append(tmp[1])
    a.append(tmp[-1])
