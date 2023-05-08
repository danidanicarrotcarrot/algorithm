import sys
input = sys.stdin.readline

while True:
    string = input().rstrip()
    if string == '.':
        break
    
    stack = []
    for s in string:
        if s in {'(', '['}:
            stack.append(s)
        if s in {')', ']'}:
            if s == ')'and len(stack) and stack[-1] == '(':
                stack.pop()
            elif s == ']' and len(stack) and stack[-1] == '[':
                stack.pop()
            else:
                stack.append(s)
                
    if len(stack):
        print('no')
    else:
        print('yes')