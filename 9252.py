a=input()
b=input()
al=len(a)
bl=len(b)
dp=[[0]*(bl+1) for _ in range(al+1)]
for ai in range(1,al+1):
    for bi in range(1,bl+1):
        if a[ai-1]==b[bi-1]:
            dp[ai][bi]=dp[ai-1][bi-1]+1
        else:
            dp[ai][bi]=max(dp[ai-1][bi],dp[ai][bi-1])
x=al
y=bl
seq=[]
while dp[x][y]!=0:
    if dp[x-1][y]==dp[x][y]:
        x-=1
    elif dp[x][y-1]==dp[x][y]:
        y-=1
    else:
        seq.append(a[x-1])
        x-=1
        y-=1

print(dp[al][bl])
if dp[al][bl]!=0:
    print(''.join(seq[::-1]))