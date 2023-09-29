n=int(input())
u=[]
for _ in range(n):
    u.append(int(input()))
uu=set()
for i in u:
    for j in u:
        uu.add(i+j)
u.sort(reverse=True)
for i in u:
    for j in u:
        if i-j in uu:
            print(i)
            exit()