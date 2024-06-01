from bisect import bisect_left
import sys
input=sys.stdin.readline

n = int(input())
ll = [list(map(int, input().split())) for _ in range(n)]
ll.sort(key=lambda k: k[1])

lis=[ll[0][0]]
pos=[0]

for i in range(1, len(ll)):
    if ll[i][0] > lis[-1]:
        lis.append(ll[i][0])
        pos.append(len(lis)-1)
    else:
        idx = bisect_left(lis, ll[i][0])
        lis[idx]=ll[i][0]
        pos.append(idx)

ans=[]
t=len(lis)-1
i=n-1
while t>=0:
    while i>=0:
        if pos[i]==t:
            break
        else:
            ans.append(ll[i][0])
            i-=1
            
    i-=1
    t-=1
while i>=0:
    ans.append(ll[i][0])
    i-=1

ans.sort()
print(len(ans))
for a in ans:
    print(a)