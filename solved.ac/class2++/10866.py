# 덱
import sys
from collections import deque

input = sys.stdin.readline
queue = deque()

for _ in range(int(input())):
    x = input().split()

    if 'push_front' in x:
        queue.appendleft(int(x[1]))
    if 'push_back' in x:
        queue.append(int(x[1]))
    
    if 'pop_front' in x:
        print(-1) if len(queue) == 0 else print(queue.popleft())
    if 'pop_back' in x:
        print(-1) if len(queue) == 0 else print(queue.pop())

    if 'size' in x:
        print(len(queue))
        
    if 'empty' in x:
        print(1) if len(queue) == 0 else print(0)

    if 'front' in x:
        print(-1) if len(queue) == 0 else print(queue[0])

    if 'back' in x:
        print(-1) if len(queue) == 0 else print(queue[-1])