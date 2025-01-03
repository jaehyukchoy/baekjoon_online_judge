from collections import defaultdict, deque

n = int(input())
a =  list(map(int,input().split()))
m = int(input())
b =  list(map(int,input().split()))

ad = defaultdict(deque)
bd = defaultdict(deque)

for i in range(len(a)):
    ad[a[i]].append(i)

for i in range(len(b)):
    bd[b[i]].append(i)


k = []
flag = True
while flag:
    flag = False
    for i in range(100, 0, -1):
        if ad[i] and bd[i]:
            ai = ad[i].popleft()
            bi = bd[i].popleft()
            for key, items in ad.items():
                while items and ai > items[0]:
                    items.popleft()
            for key, items in bd.items():
                while items and bi > items[0]:
                    items.popleft()
            k.append(i)
            flag = True
            break
print(len(k))
if k:
    print(' '.join(map(str, k)))