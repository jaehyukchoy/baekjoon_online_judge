n=int(input())
star=[[' ']*2*n for _ in range(n)]

def sol(x,y,k):
    if k==3:
        star[x][y]='*'
        star[x+1][y-1]='*'
        star[x+1][y+1]='*'
        star[x+2][y-2]='*'
        star[x+2][y-1]='*'
        star[x+2][y]='*'
        star[x+2][y+1]='*'
        star[x+2][y+2]='*'
    else:
        sol(x,y,k//2)
        sol(x+k//2,y-k//2,k//2)
        sol(x+k//2,y+k//2,k//2)

sol(0,n-1,n)
for s in star:
    print(''.join(s))