import sys
input = sys.stdin.readline

for _ in range(int(input())):
    h, w, n = map(int, input().split())
    if not n%h:
        print(h*100 + n//h)
    else:    
        print((n%h)*100 + n//h + 1)