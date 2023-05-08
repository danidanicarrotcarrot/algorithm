import sys
input = sys.stdin.readline

for _ in range(int(input())):
    s = input()
    stack = []
    for i in s:
        if i == '(':
            stack.append(i)
        if i == ')':
            if len(stack) and stack[-1] =='(':
                stack.pop()
            else:
                stack.append(i)
    if len(stack):
        print('NO')
    else:
        print('YES')