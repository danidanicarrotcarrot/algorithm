# dp_11048.py
# 이동하기 / 실버2


## bottom up 방식 : dp테이블 전체를 전부 채울 시 유리 / 재귀보다 for문이 빨라서라고 함
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [[0]+list(map(int, input().split())) for _ in range(N)] # [1,2,3,4] -> [0,1,2,3,4]
arr = [[0]*(M+1)] + arr # [0, 0, 0, 0, 0] + 원래 배열

dp = [[0 for _ in range(M+1)] for _ in range(N+1)] # 초기값 0

for i in range(1, N+1):
	for j in range(1, M+1):
		dp[i][j] = arr[i][j]
		dp[i][j] += max(dp[i-1][j], dp[i-1][j-1], dp[i][j-1])

print(dp[N][M])