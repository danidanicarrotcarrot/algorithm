# 그리디_1931.py
# 회의실 배정 / 실버 1

import sys
input = sys.stdin.readline

# input
N = int(input())
times = [list(map(int, input().split())) for _ in range(N)]

# solve
times = sorted(times, key=lambda x:(x[1], x[0])) # 끝 점 기준으로 오름차순 정렬

ans = 0
end = 0 
for s, e in times:
	if s >= end:
		ans += 1
		end = e

print(ans)