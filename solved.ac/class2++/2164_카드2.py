from collections import deque

import sys
input = sys.stdin.readline

num = deque([i for i in range(1, int(input())+1)])

while len(num):
    x = num.popleft()
    if len(num):    
        num.append(num.popleft())

print(x)