import sys
input = sys.stdin.readline

n = int(input())
a, b, c = 0, 0, 0

for i in range(n):
    num = int(input())
    x, y, z = max(b, c), a+num, b+num
    a, b, c = x, y, z

print(max(b, c))