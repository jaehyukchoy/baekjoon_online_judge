import sys
from itertools import combinations
input=sys.stdin.readline
n,s=map(int,input().split())
a=list(map(int,input().split()))
left=a[:n//2]
right=a[n//2:]
leftS=[0]
rightS=[0]
for i in range(1,len(left)+1):
    for c in combinations(left,i):
        leftS.append(sum(c))
for i in range(1,len(right)+1):
    for c in combinations(right,i):
        rightS.append(sum(c))
leftS.sort()
rightS.sort(reverse=True)
l=r=0
ans=0
while l<len(leftS) and r<len(rightS):
    total=leftS[l]+rightS[r]
    if total==s:
        tmpL=leftS[l]
        tmpR=rightS[r]
        cntL=1
        cntR=1
        l+=1
        r+=1
        while l<len(leftS) and tmpL==leftS[l]:
            l+=1
            cntL+=1
        while r<len(rightS) and tmpR==rightS[r]:
            r+=1
            cntR+=1
        ans+=cntL*cntR
    elif total<s:
        l+=1
    else:
        r+=1
if s==0:
    ans-=1
print(ans)