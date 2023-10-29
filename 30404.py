n,k=map(int,input().split())
gg=list(map(int,input().split()))
ans=0
time=0
for i in range(n):
    if time>=gg[i]:
        continue
    time=gg[i]+k
    ans+=1
print(ans)