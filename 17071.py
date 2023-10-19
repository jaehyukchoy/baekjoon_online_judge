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
        if time%2==0:
            b=set()
            for z in a:
                for zz in [z-1, z+1, z*2]:
                    if 0<=zz<=500000:
                        b.add(zz)    
        else:
            a=set()
            for z in b:
                for zz in [z-1, z+1, z*2]:
                    if 0<=zz<=500000:
                        a.add(zz)    
        time+=1
        k+=time
        if time%2==0:
            if k in a:
                flag=True
                print(time)
                break
        else:
            if k in b:
                flag=True
                print(time)
                break
            
    if not flag:
        print(-1)