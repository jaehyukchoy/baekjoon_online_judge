import sys
input = sys.stdin.readline
n = int(input())
a = list(map(int,input().split()))
b,c = map(int,input().split())
answer = 0
for aa in a:
    answer += 1
    if aa > b:
        if (aa-b)%c == 0:
            answer += (aa-b)//c
        else:
            answer += (aa-b)//c + 1
print(answer)