# 그리디_1026.py
# 보물 / 실버 4


## 내 풀이
N = int(input())
A = sorted(map(int, input().split()))
B = sorted(map(int, input().split()), reverse=True)

ab = [A[i]*B[i] for i in range(N)]

print(sum(ab))


## 예전 풀이
n = int(input())

A = sorted(list(map(int, input().split())), reverse=True)
B = sorted(list(map(int, input().split())))

ans = 0

for a, b in zip(A, B):
	ans += a*b

print(ans)