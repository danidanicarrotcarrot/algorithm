from collections import Counter
import sys
input = sys.stdin.readline

n = int(input())
nums = []
for i in range(n):
    nums.append(int(input()))
nums.sort()

res = []

res.append(int(round(sum(nums)/n, 0))) # 산술평균
res.append(nums[n//2])                 # 중앙값

cnt_nums = Counter(nums)               # 최빈값
max_cnt = max(cnt_nums.values())
most_com = sorted([x for x, y in cnt_nums.items() if y == max_cnt])
if len(most_com) > 1:
    res.append(most_com[1])
else:
    res.append(most_com[0])
    
res.append(nums[-1]-nums[0])           # 범위

print(*res, sep = '\n')