# dp_11659.py
# 구간 합 구하기 4 / 실버 4 / 누적합 알고리즘

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [0] + list(map(int, input().split())) # [0, 5, 4, 3, 2, 1]

dp = [0] * (N+1)

# dp 테이블 갱신 / [0, 5, 9, 12, 14, 15]
for n in range(1, N+1):  
	dp[n] = dp[n-1] + arr[n]

# 구간 출력
for _ in range(M):
	a, b = map(int, input().split())
	print(dp[b]-dp[a-1])