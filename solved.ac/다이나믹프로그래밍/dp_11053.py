# dp_11053.py
# 가장 긴 증가하는 부분 수열 / 실버 2
# LIS(Longest Increasing Subsequence)

import sys
imput = sys.stdin.readline

N = int(input())
arr = [0] + list(map(int, input().split()))

dp = [0] * (N+1)

# 초기값 세팅
dp[1] = 1

# dp table 갱신
for n in range(2, N+1):
	add = 0
	for i in range(1, n):
		if arr[i] < arr[n]:
			add = max(add, dp[i])
	dp[n] = add + 1

print(max(dp))