import sys, heapq
input = sys.stdin.readline

K, N = map(int, input().split())
primes = list(map(int, input().split()))

q = []

for p in primes:
    heapq.heappush(q, p)

for _ in range(N):
    top = heapq.heappop(q)
    for p in primes:
        heapq.heappush(q, top*p)
        if top % p == 0:
            break

print(top)
