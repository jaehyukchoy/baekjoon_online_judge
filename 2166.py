import sys
input=sys.stdin.readline
n=int(input())
xy=[tuple(map(int,input().split())) for _ in range(n)]
tmp=0
for i in range(n-1):
    tmp+=xy[i][0]*xy[i+1][1]-xy[i+1][0]*xy[i][1]
tmp+=xy[n-1][0]*xy[0][1]-xy[0][0]*xy[n-1][1]
tmp=abs(tmp)/2
print(round(tmp,1))