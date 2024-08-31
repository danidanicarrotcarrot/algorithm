# 모든 순열 / 실버 3

## 내 풀이 > 36580 / 176ms
from itertools import permutations

nums = [i for i in range(1, int(input())+1)]
permu = list(permutations(nums))
for per in permu:
	for p in per:
		print(p, end=' ')
	print()


## 다른 풀이 > 31120 / 96ms
from itertools import permutations

N = int(input())

for permutation in permutations(range(1, N+1)):
	print(' '.join(map(str, permutation)))