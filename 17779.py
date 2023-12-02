n=int(input())
city=[list(map(int,input().split())) for _ in range(n)]

s=sum(map(sum,city))

ans=s
for x in range(1,n+1):
    for y in range(1,n+1):
        for d1 in range(1,n):
            for d2 in range(1,n):
                if x+d1+d2>n or y-d1<1 or y+d2>n:
                    continue
                g1=g2=g3=g4=0
                for r in range(1,x+d1):
                    for c in range(1,y+1):
                        if r+c<x+y:
                            g1+=city[r-1][c-1]
                            
                for r in range(1,x+d2+1):
                    for c in range(y+1,n+1):
                        if c-r>y-x:
                            g2+=city[r-1][c-1]
                            
                for r in range(x+d1,n+1):
                    for c in range(1,y-d1+d2):
                        if c-r<(y-d1)-(x+d1):
                            g3+=city[r-1][c-1]
                            
                for r in range(x+d2+1,n+1):
                    for c in range(y-d1+d2,n+1):
                        if r+c>(y+d2)+(x+d2):
                            g4+=city[r-1][c-1]
                            
                g5=s-g1-g2-g3-g4
                ans=min(ans,max(g1,g2,g3,g4,g5)-min(g1,g2,g3,g4,g5))
print(ans)