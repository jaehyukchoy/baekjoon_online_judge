import sys
from itertools import combinations
from collections import defaultdict
input=sys.stdin.readline
t=int(input())
n=int(input())
a=list(map(int,input().split()))
m=int(input())
b=list(map(int,input().split()))
dpa=[0]*(n+1)
dpb=[0]*(m+1)
for i in range(1,n+1):
    dpa[i]=dpa[i-1]+a[i-1]
for i in range(1,m+1):
    dpb[i]=dpb[i-1]+b[i-1]

suma=defaultdict(int)
sumb=defaultdict(int)
for al,ar in combinations(list(range(n+1)),2):
    suma[dpa[ar]-dpa[al]]+=1
for bl,br in combinations(list(range(m+1)),2):
    sumb[dpb[br]-dpb[bl]]+=1

ans=0
for a_val,a_cnt in suma.items():
    if t-a_val in sumb:
        ans+=a_cnt*sumb[t-a_val]

print(ans)