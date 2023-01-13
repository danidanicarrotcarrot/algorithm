# 요세푸스 문제 0
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
idx = k
nums = [i for i in range(1, n+1)]
ans = []

while len(nums) != 0:
    idx = (idx-1) % len(nums)
    ans.append(nums[idx])
    del nums[idx]
    idx += k

print('<', end='')
for i in range(len(ans)):
    if i == len(ans)-1:
        print(ans[i], end='')
    else:
        print(ans[i], end=', ')
print('>') 