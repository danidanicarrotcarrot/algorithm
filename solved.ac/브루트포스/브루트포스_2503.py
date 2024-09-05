# 숫자야구 / 실버 3

## 내 풀이 (31120/36ms)
from itertools import permutations
N = int(input()) # 질문 수 1<= N <= 100

lst = [list(map(int, input().split())) for i in range(N)]
lst.sort(key= lambda x : (-x[1], -x[2])) # [[327, 2, 0], [123, 1, 1], [356, 1, 0], [489, 0, 1]]

perm = list(permutations(range(1, 10), 3)) # 순열
nums = [''.join(list(map(str, i))) for i in perm]

ans = 0

for num in nums: # 123
	ok = True

	for q, s2, b2 in lst: # 327, 2, 0
		s1, b1 = 0, 0
		q = str(q)

		for i in range(3):
			if num[i] == q[i]: # 자리수가 같으면 s+1
				s1 += 1
			elif num[i] in q:  # 수가 같으면 b+1
				b1 += 1
		
		if s1 != s2 or b1 != b2:
			ok = False
			break
		
	if ok == True : 
		ans += 1

print(ans)