import sys
input=sys.stdin.readline
n,k=map(int,input().split())
a=set()
time=0
a.add(n)
if n==k:
    print(0)
else:
    flag=False
    while k<=500000:
        time+=1
        k+=time
        if time%2==1:
            b=set()
            for z in a:
                for zz in [z-1, z+1, z*2]:
                    if k==zz:
                        print(time)
                        exit()
                    if 0<=zz<=500000:
                        b.add(zz)
        else:
            a=set()
            for z in b:
                for zz in [z-1, z+1, z*2]:
                    if k==zz:
                        print(time)
                        exit()
                    if 0<=zz<=500000:    
                        a.add(zz)    
    print(-1)