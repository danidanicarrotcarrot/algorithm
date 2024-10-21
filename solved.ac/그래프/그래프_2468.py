# 그래프_2468.py
# 안전 영역 / 실버 1

import sys
input = sys.stdin.readline
sys.setrecursionlimit(int(1e6))


def dfs(y, x, h):
	global dy, dx, N, matrix, visited

	# base case
	if not (0 <= y < N and 0 <= x < N):
		return
	if visited[y][x] or matrix[y][x] <= h:
		return
	visited[y][x] = True

	# recursive case
	for i in range(4):
		ny = y + dy[i]
		nx = x + dx[i]
		dfs(ny, nx, h)


def get_num(height): # 높이가 height일 때, 안전 영역의 개수를 반환
	global dy, dx, N, matrix, visited

	visited = [[False] * N for _ in range(N)]

	num = 0
	for y in range(N):
		for x in range(N):
			if (not visited[y][x]) and (matrix[y][x] > height):
				dfs(y, x, height)
				num += 1

	return num


dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

# input
N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]

# solve
ans = 0
for height in range(101):
	ans = max(ans, get_num(height))

print(ans)