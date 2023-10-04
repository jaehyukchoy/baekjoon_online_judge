n=int(input())
f=[0,1]
if n>=2:
    for i in range(2,n+1):
        f.append(f[i-2]+f[i-1])
print(f[n])