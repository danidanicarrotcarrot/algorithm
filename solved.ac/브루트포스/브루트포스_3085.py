import sys
input = sys.stdin.readline

# 연속된 부분 중에서 긴 길이 구하기
def get_best(y, x):
	global N, matrix
	best = 0

	# one row
	bef = '-'					# before 값
	value = 0
	for j in range(N): 			# N만큼 탐색
		if bef == matrix[y][j]: # 이전 값과 같으면 +1
			value += 1
		else:					# 다르면 value 1로 초기화
			value = 1
		bef = matrix[y][j]
		best = max(best, value)	# max값을 best로 저장

	# one column
	bef = '-'
	value = 0
	for i in range(N):
		if bef == matrix[i][x]:
			value += 1
		else:
			value = 1
		bef = matrix[i][x]
		best = max(best, value) 

	return best

# 상하좌우 탐색
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

N = int(input())
matrix = [list(input().strip()) for _ in range(N)]

ans = 0 # 답

for y in range(N):
	for x in range(N):
		if y == x: # 대각선 방향에서 한 번 다 탐색을 해주기
			ans = max(ans, get_best(y, x))
		for i in range(4): 	# 상하좌우 확인
			ny = y+dy[i] 	# 바꿀 좌표
			nx = x+dx[i]
			if 0 <= ny < N and 0 <= nx < N: # 좌표가 매트릭스를 넘어가지 않을 때만
				if matrix[y][x] != matrix[ny][nx]: # 양 옆이 다르면 바꿔주고 get best
					matrix[y][x], matrix[ny][nx] = matrix[ny][nx], matrix[y][x]
					ans = max(ans, get_best(y, x))
					matrix[y][x], matrix[ny][nx] = matrix[ny][nx], matrix[y][x]

print(ans)
