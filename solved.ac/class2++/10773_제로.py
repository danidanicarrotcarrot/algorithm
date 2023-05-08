import sys
input = sys.stdin.readline

stack = []
for i in range(int(input())):
    n = int(input())
    if n:
        stack.append(n)
    else:
        stack.pop()
print(sum(stack))