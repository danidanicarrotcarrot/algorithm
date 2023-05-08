n, k = map(int, input().split())

x, y = 1, 1
for i in range(n, k, -1):
    x *= i

for i in range(n-k, 1, -1):
    y *= i
    
print(x//y)    