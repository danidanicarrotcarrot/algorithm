# 큐
import sys
from collections import deque

input = sys.stdin.readline
queue = deque()

for _ in range(int(input())):
    x = input().split()

    if 'push' in x:
        queue.append(int(x[1]))

    if 'size' in x:
        print(len(queue))

    if 'pop' in x:
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.popleft())

    if 'empty' in x:
        if len(queue) == 0:
            print(1)
        else:
            print(0)

    if 'front' in x:
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])

    if 'back' in x:
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])