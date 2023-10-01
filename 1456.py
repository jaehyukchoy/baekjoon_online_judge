def prime_list(n):
    sieve = [True] * n
    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i] == True:
            for j in range(i+i, n, i):
                sieve[j] = False
    return [i for i in range(2, n) if sieve[i] == True]

a,b=map(int,input().split())
prime=prime_list(int(b**0.5)+1)
ans=0
for i in range(len(prime)):
    n=2
    while True:
        t=prime[i]**n
        if t>b:
            break
        if a<=t<=b:
            ans+=1
        n+=1
print(ans)  