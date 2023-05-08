import sys
input = sys.stdin.readline

n = int(input())
ans = [0]*10001

for i in range(n):
    a = int(input())
    ans[a] += 1
    
for i in range(10001):
    if ans[i] >= 1:
        for j in range(ans[i]):
            print(i)