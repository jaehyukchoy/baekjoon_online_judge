s = input()
p = s[0]
ans = 0
flag = False
for i in range(1, len(s)):
    if s[i] != p and not flag:
        ans += 1
        flag = True
    if s[i] == p:
        flag = False
print(ans)
