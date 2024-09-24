# dp_11660.py
# 구간 합 구하기 5 / 실버 1 / 누적합 알고리즘

import sys
input = sys.stdin.readline

N, M = map(int, input().split())

arr = [[0]+list(map(int, input().split())) for _ in range(N)]
arr = [[0]*(N+1)] + arr # 어레이에도 0을 각각 채워줌

dp = [[0 for _ in range(N+1)] for _ in range(N+1)]

# 구간합 구하기
for x in range(1, N+1):
	for y in range(1, N+1):
		dp[x][y] = (dp[x-1][y] + dp[x][y-1] - dp[x-1][y-1]) + arr[x][y]

# 구간합 출력
for i in range(M):
	x1, y1, x2, y2 = map(int, input().split())
	print(dp[x2][y2] - (dp[x2][y1-1]+dp[x1-1][y2]-dp[x1-1][y1-1]))