import sys
input=sys.stdin.readline
n=int(input())
x=list(map(int,input().split()))
cards=[False]*1000001
for xx in x:
    cards[xx]=True

scores=[0]*1000001
for xx in x:
    for i in range(xx+xx,1000001,xx):
        if cards[i]:
            scores[xx]+=1
            scores[i]-=1

for i in range(n):
    print(scores[x[i]],end=' ')