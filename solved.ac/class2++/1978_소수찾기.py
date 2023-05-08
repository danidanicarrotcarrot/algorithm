import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
ans = 0

for num in nums:
    if num == 1:
        continue
    for i in range(2, num):
        if not num%i:
            break
    else:
        ans += 1

print(ans)       