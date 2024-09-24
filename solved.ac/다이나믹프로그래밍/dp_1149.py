# dp_1149.py
# RGB거리 / 실버 1

import sys
imput = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
arr = [[0]*3] + arr

dp = [[0]*3 for _ in range(N+1)]

for i in range(1, N+1):
	for j in range(3):
		dp[i][j] = arr[i][j]
		dp[i][j] += min(dp[i-1][j+1:]+dp[i-1][:j]) # 해당 인덱스 제외 리스트를 생성해서 그 중 최솟값을 더해줌

print(min(dp[-1]))