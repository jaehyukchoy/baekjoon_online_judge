a = int(input())
b = int(input())
c = int(input())
s = a * b * c
arr = list(map(int, str(s)))
for i in range(10):
    print(arr.count(i))