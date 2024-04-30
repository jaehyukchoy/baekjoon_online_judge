d0 = [0] * 41
d1 = [0] * 41
for i in range(41):
    if i == 0:
        d0[i] = 1
    elif i == 1:
        d1[i] = 1
    else:
        d0[i] = d0[i - 1] + d0[i - 2]
        d1[i] = d1[i - 1] + d1[i - 2]

for _ in range(int(input())):
    n = int(input())
    print(d0[n], d1[n])
