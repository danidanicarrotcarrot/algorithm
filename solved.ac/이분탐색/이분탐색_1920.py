# 이분탐색_1920.py
# 수 찾기 / 실버 4


# 이분탐색 풀이
def is_exist(arr, num):
	left = 0
	right = len(arr)-1

	while left <= right:
		mid = (left+right)//2

		if arr[mid] < num:
			left = mid+1
		if arr[mid] > num:
			right = mid-1
		if arr[mid] == num:
			return 1

	return 0

N = int(input())
arr = sorted(map(int, input().split()))
M = int(input())
num = list(map(int, input().split()))

for m in num:
	print(is_exist(arr, m))


# set을 이용한 풀이
N = int(input())
nlist = set(map(int, input().split()))

M = int(input())
mlist = list(map(int, input().split()))

for m in mlist:
	print(1 if m in nlist else 0)