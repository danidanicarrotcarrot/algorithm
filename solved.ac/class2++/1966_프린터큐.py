import sys
input = sys.stdin.readline
from collections import deque

for _ in range(int(input())):
    n, m = map(int, input().split())
    txt = list(map(int, input().split()))
    idx = deque((i, txt[i]) for i in range(n))

    ans = []
    while True:
        x = idx.popleft()
        
        if len(idx) == 0:
            ans.append(x[0])
            break
            
        for y in idx:
            if x[1] >= y[1]:
                continue
            else:
                idx.append(x)
                break
        else:
            ans.append(x[0])

    print(list(ans).index(m)+1)