from math import comb
MOD = 10007
n = int(input())
answer = 0
for i in range(1, n//4+1):
    tmp = comb(13,i) * comb(52-(4*i), n-(4*i))
    if i%2:
        answer += tmp % MOD
    else:
        answer -= tmp % MOD
print(answer % MOD)
