import sys
input = sys.stdin.readline

x, y = map(int, input().split())
n = x*y
while y:
    x, y = y, x%y

print(x, n//x)