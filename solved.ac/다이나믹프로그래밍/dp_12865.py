# dp_12865.py
# 평범한 배낭 / 골드 5

import sys
input = sys.stdin.readline

N, K = map(int, input().split())

W = [0] # 무게
V = [0] # 가치

for _ in range(N):
	w, v = map(int, input().split())
	W.append(w)
	V.append(v)

dp = [[0 for _ in range(K+1)] for _ in range(N+1)]

for n in range(1, N+1):
	for k in range(1, K+1):
		dp[n][k] = dp[n-1][k]
		if k - W[n] >= 0:
			dp[n][k] = max(dp[n][k], dp[n-1][k-W[n]]+V[n])

print(dp[N][K])