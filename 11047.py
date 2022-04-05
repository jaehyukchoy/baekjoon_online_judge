n, k = input().split()
n = int(n)
k = int(k)
coin = []
answer = 0
for i in range(n):
    coin.append(int(input()))
coin.reverse()
for c in coin:
    if c <= k:
        answer += k // c
        k = k % c
print(answer)