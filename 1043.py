import sys
from collections import deque
input=sys.stdin.readline
n,m=map(int,input().split())
knows=list(map(int,input().split()))
knows=knows[1:]
party=[]
for _ in range(m):
    tmp=list(map(int,input().split()))
    party.append(tmp[1:])

def find_party(i):
    r=[]
    for e,p in enumerate(party):
        for m in p:
            if m==i:
                r.append(e)
                break
    return r

def sol(q):
    v=[True]*m
    while q:
        idx=q.popleft()
        v[idx]=False
        for mem in party[idx]:
            for p in find_party(mem):
                if v[p]:
                    v[p]=False
                    q.append(p)
    return v

q=[]
for w in knows:
    q+=find_party(w)
tmp=sol(deque(q))
ans=0
for a in tmp:
    if a:
        ans+=1
print(ans)