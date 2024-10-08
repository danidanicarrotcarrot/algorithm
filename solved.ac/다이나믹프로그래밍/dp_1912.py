# dp_1912.py
# 연속합 / 실버 2

N = int(input())
arr = [0] + list(map(int, input().split()))

dp = [0 for _ in range(N+1)]

for n in range(1, N+1):
	dp[n] = max(arr[n], dp[n-1]+arr[n])

print(max(dp[1:]))