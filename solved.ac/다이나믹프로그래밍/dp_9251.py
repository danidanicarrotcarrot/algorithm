# dp_9251.py
# LCS / 골드 5

# LCS(Longest Common Subsequence, 최장 공통 부분 수열)문제
# 두 수열이 주어졌을 때, 모두의 부분 수열이 되는 수열 중 가장 긴 것을 찾는 문제
# 예를 들어, ACAYKP와 CAPCAK의 LCS는 ACAK가 된다

s1 = ' ' + input()
s2 = ' ' + input()

N, M = len(s1), len(s2)

dp = [[0]*M for _ in range(N)]

for n in range(1, N):
	for m in range(1, M):
		if s1[n] == s2[m]:
			dp[n][m] = dp[n-1][m-1] + 1
		else:
			dp[n][m] = max(dp[n-1][m], dp[n][m-1])

print(dp[N-1][M-1])