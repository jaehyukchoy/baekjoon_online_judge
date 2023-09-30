n=int(input())
s=[int(input()) for _ in range(n)]
a=[0]*n
for i in range(n):
    if i==0:
        a[i]=s[i]
    elif i==1:
        a[i]=s[i]+s[i-1]
    elif i==2:
        a[i]=max(s[i]+s[i-2],s[i]+s[i-1])
    else:
        a[i]=max(s[i]+a[i-2],s[i]+s[i-1]+a[i-3])
print(a[n-1])