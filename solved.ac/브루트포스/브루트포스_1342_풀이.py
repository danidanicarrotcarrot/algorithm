# 브루트포스_1342_풀이.py
# 행운의 문자열 / 실버 1

from itertools import permutations

def fact(x):  # 팩토리얼 함수 구현
	if x == 0:
		return 1
	return fact(x - 1) * x

S = input()
ans = 0

for perm in permutations(S): # 모든 순열에 대해 살펴봄
	ok = True
	for i in range(0, len(S) - 1):
		if perm[i] == perm[i + 1]: # 앞뒤가 같으면 ok 를 false로 변경
			ok = False
			break
	ans += ok # 다 돌아가면 ans 에 ok를 더해줌 (True:1)

for i in range(ord('a'), ord('z') + 1):
	ans //= fact(S.count(chr(i)))

print(ans)