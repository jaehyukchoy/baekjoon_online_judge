import sys
from queue import PriorityQueue
input=sys.stdin.readline
n=int(input())
sq=PriorityQueue()
lq=PriorityQueue()
num_l=[int(input()) for _ in range(n)]

for i,num in enumerate(num_l):
    if i==0:
        mid=num
    elif i%2==1:
        if mid<num:
            lq.put(num)
        else:
            lq.put(mid)
            sq.put(-num)
            mid=-sq.get()
    else:
        if mid<num:
            sq.put(-mid)
            lq.put(num)
            mid=lq.get()
        else:
            sq.put(-num)
    print(mid)