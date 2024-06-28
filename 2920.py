s = list(map(int,input().split()))
asc = True
desc = True
for i in range(8):
    if s[i] != i+1:
        asc = False
    if s[i] != 8-i:
        desc = False

if asc:
    print("ascending")
elif desc:
    print("descending")
else:
    print("mixed")