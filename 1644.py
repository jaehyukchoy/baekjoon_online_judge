import sys
input=sys.stdin.readline

def make_prime(n):
    if n<2:
        return []
    else:
        prime=[True]*(n+1)
        for i in range(2,int(n**0.5)+1):
            for j in range(i+i,n+1,i):
                prime[j]=False
        return [i for i in range(2,n+1) if prime[i]]

n=int(input())
p=make_prime(n)
ans=0
l=0
r=0
while r<len(p):
    s=sum(p[l:r+1])
    if s==n:
        ans+=1
        r+=1
    elif s<n:
        r+=1
    else:
        l+=1
print(ans)