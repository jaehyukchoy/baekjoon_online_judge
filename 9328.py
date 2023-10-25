import sys
from collections import deque
input=sys.stdin.readline

def bfs(s):
    flag=False
    global ans
    v=[[False]*(h+2) for _ in range(w+2)]
    v[s[0]][s[1]]=True
    q=deque([s])
    while q:
        x,y=q.popleft()
        for dx,dy in [(1,0),(0,1),(-1,0),(0,-1)]:
            nx,ny=x+dx,y+dy
            if 0<=nx<w+2 and 0<=ny<h+2 and not v[nx][ny] and g[nx][ny]!='*':
                if 'A'<=g[nx][ny]<='Z':
                    if g[nx][ny].lower() in keys:
                        v[nx][ny]=True
                        q.append((nx,ny))
                else:
                    v[nx][ny]=True
                    q.append((nx,ny))
                    if g[nx][ny]=='$':
                        ans+=1
                        g[nx][ny]='.'
                    if 'a'<=g[nx][ny]<='z':
                        keys.add(g[nx][ny])
                        g[nx][ny]='.'
                        flag=True
    return flag

for _ in range(int(input())):
    w,h=map(int,input().split())
    g=[['.']*(h+2)]
    for _ in range(w):
        tmp=['.']
        tmp+=list(input().rstrip())
        tmp+=['.']
        g.append(tmp)
    g.append(['.']*(h+2))
    keys=input().rstrip()
    keys=set(keys) if keys!='0' else set()
    ans=0
    while bfs((0,0)):
        continue
    print(ans)