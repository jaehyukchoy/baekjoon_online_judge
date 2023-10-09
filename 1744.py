import sys
input=sys.stdin.readline
n=int(input())
num=[]
for _ in range(n):
    num.append(int(input()))
num.sort(reverse=True)
ans=[]
v=[False]*n
for i in range(0,n-1,2):
    if num[i+1]>1:
        ans.append(num[i]*num[i+1])
        v[i]=True
        v[i+1]=True
    else:
        break
for i in range(n-1,-1,-2):
    if i-1>=0 and num[i-1]<=0:
        ans.append(num[i]*num[i-1])
        v[i]=True
        v[i-1]=True
    else:
        break
a=0
for i in range(n):
    if not v[i]:
        a+=num[i]
print(sum(ans)+a)