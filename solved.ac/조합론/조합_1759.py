# 암호 만들기 / 골드 5

## 내 풀이 > 31120 / 32ms
from itertools import combinations

l, c = map(int, input().split())
s = sorted(list(input().split()))
combi = list(combinations(s, l))

for com in combi:
	if 2 <= len(set(com)-{'a', 'e', 'i', 'o', 'u'}) <= l-1: # 자음1/모음2 이상 조건
		for c in com:
			print(c, end='')
		print()
	else:
		continue