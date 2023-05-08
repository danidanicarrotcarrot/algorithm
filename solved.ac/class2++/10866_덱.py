from collections import deque
import sys
input = sys.stdin.readline

dq = deque()

for i in range(int(input())):
    cmd = input().strip()
    if cmd =='size':
        print(len(dq))
    
    if 'push' in cmd:
        x, y = cmd.split()
        if x == 'push_front':
            dq.appendleft(y)
        if x == 'push_back':
            dq.append(y)
    
    if cmd == 'pop_front':
        if len(dq):
            print(dq.popleft())
        else:
            print(-1)
    
    if cmd == 'pop_back':
        if len(dq):
            print(dq.pop())
        else:
            print(-1)

    if cmd =='empty':
        if len(dq):
            print(0)
        else:
            print(1)
    
    if cmd == 'front':
        if len(dq):
            print(dq[0])
        else:
            print(-1)
    
    if cmd == 'back':
        if len(dq):
            print(dq[-1])
        else:
            print(-1)