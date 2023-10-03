import sys
from collections import deque
input=sys.stdin.readline

while True:
    tmp=list(map(int,input().split()))
    if tmp==[0]:
        break
    nn=tmp[0]
    hh=tmp[1:]
    
    ans=0
    s=deque([(-1,-1)])
    for i,h in enumerate(hh):
        if s[-1][1]<h:
            s.append((i,h))
        else:
            while s[-1][1]>=h:
                start,height=s.pop()
                ans=max(ans,(i-start)*height)
            s.append((start,h))
             
    while s:
        start,height=s.pop()
        ans=max(ans,(nn-start)*height)
    print(ans)