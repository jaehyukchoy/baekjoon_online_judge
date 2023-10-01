def prime_list(n=10000):
    l=[True]*n
    for i in range(2,int(n**0.5)+1):
        for j in range(2*i,n,i):
            l[j]=False
    return [i for i in range(1000,n) if l[i]]
prime=prime_list()

def bfs(q,e):
    while q:
        s,c=q.popleft()
        if s==e:
            return c
        for i in range(4):
            for j in range(10):
                if i==0:
                    n=s%(10**(i+1))
                else:
                    n=(s%(10**(i+1))-s%(10**i))/(10**i)
                ns=int(s+(j-n)*(10**i))
                if not v[ns] and ns in prime:
                    q.append((ns,c+1))
                    v[ns]=True
    return 'Impossible'


import sys
from collections import deque
t=int(sys.stdin.readline())
tt=[]
for i in range(t):
    tt.append(tuple(map(int,sys.stdin.readline().split())))
for s,e in tt:
    v=[False]*10000
    q=deque([(s,0)])
    v[s]=True
    ans=bfs(q,e)
    print(ans)