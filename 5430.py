import sys
from collections import deque
input=sys.stdin.readline
t=int(input())
for _ in range(t):
    p=input().rstrip()
    n=int(input())
    if n==0:
        input()
        x=deque()
    else:
        tmp=input().rstrip()
        tmp=tmp[1:len(tmp)-1].split(',')
        x=deque(tmp)
    front=1
    err=False
    for pp in p:
        if pp=='R':
            front*=-1
        else:
            if not x:
                err=True
                print('error')
                break
            if front==1:
                x.popleft()
            else:
                x.pop()
    if not err:
        if not x:
            print('[]')    
        else:
            print('[',end='')

            if front==1:
                for i in range(len(x)-1):
                    print(x[i],end=',')
                print(x[-1],end='')
            else:
                for i in range(len(x)-1,0,-1):
                    print(x[i],end=',')
                print(x[0],end='')
            print(']')