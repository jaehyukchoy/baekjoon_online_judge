# 미채점 코드임.
import sys
input=sys.stdin.readline
n=int(input())
h,d,k=map(int,input().split())
p=[]
for _ in range(n):
    p.append(int(input()))

def dfs(h,c):
    global d, flag, ans
    if c==n:
        ans=max(ans,h)
        return
    for i in range(3):
        if i==0:
            dfs(h-max(0,p[c]-d)//2,c+1)
        elif i==1:
            d+=k
            dfs(h-max(0,p[c]-d),c+1)
            d-=k
        else:
            if not flag:
                flag=True
                if c+1<n:
                    tmp=p[c+1]
                    p[c+1]=0
                dfs(h-max(0,p[c]-d),c+1)
                if c+1<n:
                    p[c+1]=tmp
                flag=False
flag=False            
ans=0
dfs(h,0)
if ans<=0:
    print(-1)
else:
    print(ans)