n=int(input())
s=set(input())
lower=['r','o','y','g','b','i','v']
upper=['R','O','Y','G','B','I','V']
lFlag=uFlag=True
for l in lower:
    if l not in s:
        lFlag=False
        break
for u in upper:
    if u not in s:
        uFlag=False
        break
if lFlag and uFlag:
    print('YeS')
elif lFlag:
    print('yes')
elif uFlag:
    print('YES')
else:
    print('NO!')