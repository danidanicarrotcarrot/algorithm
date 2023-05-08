import sys
input = sys.stdin.readline

k, n = map(int, input().split())
nums = [int(input()) for _ in range(k)]

start, end = 1, sum(nums)//n
while start <= end:
    mid = (start+end)//2
    cnt = 0
    for num in nums:
        cnt += num//mid

    if cnt < n:
        end = mid - 1
    else:
        start = mid + 1

print(end)