# 브루트포스_1342.py
# 행운의 문자열 / 실버 1

## 내 풀이 (488276/4236ms)
from itertools import permutations
S = list(input())

ans = 0
perm = list(map(''.join, permutations(S, len(S))))

if len(perm) == len(set(perm)): # 완전 다른 문자들만 있는 경우 ex.abcdefghij
	ans = len(perm)

else:							# 그 외의 경우 인접한 두 문자가 같으면 break, 다 돌아가면 ans+1
	for com in set(perm):
		for i in range(len(S)-1):
			if com[i] == com[i+1]:
				break
		else:
			ans+=1

print(ans)