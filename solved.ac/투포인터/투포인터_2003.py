# 투포인터_2003.py
# 수들의 합 2 / 실버4

# input
N, M = map(int, input().split())
arr = list(map(int, input().split()))

# solve (two pointer)
left, right, cnt = 0, 1, 0

while left <= right and right <= N:
	res = sum(arr[left:right])

	if res < M:
		right += 1

	elif res > M:
		left += 1

	else:
		cnt += 1
		left += 1

print(cnt)