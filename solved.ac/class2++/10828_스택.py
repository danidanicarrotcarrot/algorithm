import sys
input = sys.stdin.readline

stack = []
for i in range(int(input())):
    cmd = input().rstrip()
    
    if 'push' in cmd:
        x, y = cmd.split()
        stack.append(y)
        
    if cmd == 'size':
        print(len(stack))
    
    if cmd == 'pop':
        if len(stack):
            print(stack.pop())
        else:
            print(-1)
    
    if cmd =='empty':
        if len(stack):
            print(0)
        else:
            print(1)
            
    if cmd == 'top':
        if len(stack):
            print(stack[-1])
        else:
            print(-1)