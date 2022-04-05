n = int(input())
w = []
for i in range(n):
    w.append(int(input()))
w.sort()
for i in range(n):
    w[i] = w[i] * (n - i)
print(max(w))