n,k=map(int,input().split())

i=1
while k>=i*9*(10**(i-1)):
    k-=i*9*(10**(i-1))
    i+=1
if k==0:
    print(9)
else:
    a=str(10**(i-1)-1+(k+i-1)//i)
    if int(a)>n:
        print(-1)
    else:
        print(a[(k+i-1)%i])