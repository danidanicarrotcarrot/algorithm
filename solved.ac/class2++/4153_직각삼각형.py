import sys
input = sys.stdin.readline

while True:
    t = sorted(map(int, input().split()))
    if t[0] == t[1] == t[2] == 0:
        break
    if t[0]**2 + t[1]**2 == t[2]**2:
        print('right')
    else:
        print('wrong')