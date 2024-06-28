n = list(map(int,input().split()))
print(sum(map(lambda x:x**2, n))%10)