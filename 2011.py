n=input()
nl=len(n)
dp=[0]*nl
for i in range(nl):
    if i==0 and 1<=int(n[i])<=26:
        dp[i]=1
    else:
        if 1<=int(n[i])<=26:
            dp[i]=dp[i-1]
        if n[i-1]!='0' and 1<=int(n[i-1]+n[i])<=26:
            if i==1:
                dp[i]+=1
            else:    
                dp[i]+=dp[i-2]
if 0 in dp:
    print(0)
else:
    print(dp[nl-1]%1000000)