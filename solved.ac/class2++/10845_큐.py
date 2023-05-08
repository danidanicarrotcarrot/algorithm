from collections import deque
import sys
input = sys.stdin.readline

q = deque()
for i in range(int(input())):
    cmd = input().strip()

    if 'push' in cmd:
        x, y = cmd.split()
        q.append(y)

    if cmd == 'size':
        print(len(q))

    if cmd == 'pop':
        if len(q):
            print(q.popleft())
        else:
            print(-1)

    if cmd == 'empty':
        if len(q):
            print(0)
        else:
            print(1)

    if cmd == 'front':
        if len(q):
            print(q[0])
        else:
            print(-1)

    if cmd == 'back':
        if len(q):
            print(q[-1])
        else:
            print(-1)