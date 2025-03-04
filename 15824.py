n = int(input())
m = list(map(int, input().split()))
m.sort()

MOD = 1000000007
 
def pow(a, b):
    if b == 0:
        return 1
    if b == 1:
        return a
    half = pow(a, b//2)
    return half * half % MOD if b % 2 == 0 else half * half * a % MOD

ans = 0
for i in range(n):
    ans += m[i] * (pow(2,i) - pow(2,n-i-1))
    
print(ans%MOD)