from re import L
import sys
input = sys.stdin.readline
n,l=map(int,input().split())
m = [list(map(int,input().split())) for _ in range(n)]

def road(r, u):
    for i in range(n-1):
        if abs(r[i]-r[i+1])>1:
            return False
        if r[i] > r[i+1]:
            for j in range(1,l+1):
                if i+j>=n or u[i+j] or r[i+1] != r[i+j]:
                    return False
                u[i+j]=True
        elif r[i] < r[i+1]:
            for j in range(l):
                if i-j<0 or u[i-j] or r[i] != r[i-j]:
                    return False
                u[i-j]=True
    return True

answer = 0
for i in range(n):
    u1 = [False for _ in range(n)]
    u2 = [False for _ in range(n)]
    if road(m[i],u1):
        answer += 1
    if road([m[j][i] for j in range(n)],u2):
        answer += 1
print(answer)