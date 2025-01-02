x = input()
answer = ''

cal1 = {'*', '/'}
cal2 = {'+', '-'}

s = []
for e in x:
    if e.isalpha():
        answer += e
    elif e == '(':
        s.append(e)
    elif e in cal1:
        while s and s[-1] in cal1:
            answer += s.pop()
        s.append(e)
    elif e in cal2:
        while s and s[-1] != '(':
            answer += s.pop()
        s.append(e)
    else:
        while s and s[-1] != '(':
            answer += s.pop()
        s.pop()
                

while s:
    answer += s.pop()

print(answer)