# 로또 / 실버 2

## 내 풀이 > 31120 / 36ms
from itertools import combinations

while True:
	nums = list(map(int, input().split())) # [7, 1, 2, 3, 4, 5, 6, 7]
	k = nums[0]
	s = nums[1:] # s에서 6개의 수를 고르는 모든 방법 print
	combi = list(combinations(s, 6))
	for com in combi:
		for c in com:
			print(c, end=' ')
		print('')
	print('')
	if k == 0: # 종료조건
		break