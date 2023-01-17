# 스택
import sys
input = sys.stdin.readline

stack = []

for _ in range(int(input())):
    x = input().split()
    
    if 'push' in x:
        stack.append(int(x[1]))

    if 'size' in x:
        print(len(stack))
        
    if 'pop' in x:
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())

    if 'empty' in x:
        if len(stack) == 0:
            print(1)
        else :
            print(0)
    
    if 'top' in x:
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])