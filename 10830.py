import sys
input=sys.stdin.readline
n,b=map(int,input().split())
matrix=[list(map(int,input().split())) for _ in range(n)]

def mul(ma,mb):
    m=[[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            tmp=0
            for k in range(n):
                tmp+=ma[i][k]*mb[k][j]
            m[i][j]=tmp%1000
    return m


def sol(m,b):
    if b==1:
        new=[[0]*n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                new[i][j]=m[i][j]%1000
        return new
    mm=sol(m,b//2)
    if b%2==0:
        return mul(mm,mm)   
    else:
        return mul(mul(mm,mm),m)
    
ans=sol(matrix,b)
for i in range(n):
    for j in range(n):
        print(ans[i][j],end=' ')
    print()