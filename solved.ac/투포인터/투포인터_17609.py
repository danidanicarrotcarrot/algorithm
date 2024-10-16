# 투포인터_17609.py
# 회문 / 골드 5
# 회문이면 0 유사회문이면 1 그 외 2

import sys
input = sys.stdin.readline

def is_possible(s):
	if s == s[::-1]:
		return 0
	
	i = 0
	while i < len(s):
		x = s[:i]+s[i+1:]
		if x == x[::-1]:
			return 1
		i += 1

	return 2

# input
T = int(input())

# solve
for _ in range(T):
	s = input().strip()
	print(is_possible(s))

# 답은 나오는데 시간 초과남.. 때려치겟슴