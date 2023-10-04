n=int(input())
k=6
m=10**k
p=15*10**(k-1)
f=[0,1]
for i in range(2,n%p+1):
    f.append(f[i-2]+f[i-1])
    f[i]%=m
print(f[n%p])