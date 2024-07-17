sentence = input()
bomb = input()
bomb_len = len(bomb)
stack = []

for i in range(len(sentence)):
    stack.append(sentence[i])
    if sentence[i] == bomb[-1] and ''.join(stack[-bomb_len:]) == bomb:
        for _ in range(bomb_len):
            stack.pop()
    
        

if stack:
    print(''.join(stack))
else:
    print("FRULA")
