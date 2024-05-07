import re

x = input()
y = list(map(int, re.split("[+-]", x)))

idx = 0
flag = False
for i in range(len(x)):
    if x[i] == "+":
        idx += 1
    elif x[i] == "-":
        flag = True
        break
if flag:
    ans = sum(y[: idx + 1]) - sum(y[idx + 1 :])
else:
    ans = sum(y)
print(ans)
