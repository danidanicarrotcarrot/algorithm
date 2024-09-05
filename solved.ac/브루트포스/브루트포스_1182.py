# 부분수열의 합 / 실버 2

## 내 풀이
from itertools import combinations

N, S = map(int, input().split())
nums = list(map(int, input().split()))

ans = 0

for i in range(1, N+1):
	for comb in combinations(nums, i):
		if sum(comb)==S:
			ans += 1

print(ans)