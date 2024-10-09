# 백트레킹_2580.py
# 스도쿠 / 골드 5

def is_possible(y, x, n):
	global matrix

	for c in range(9):			# 같은 열 확인 (세로, col)
		if matrix[y][c] == n:
			return False
	for r in range(9):			# 같은 행 확인 (가로, row)
		if matrix[r][x] == n:
			return False
	for r in range(3):			# 같은 사각형 확인
		for c in range(3):
			if matrix[3*(y//3)+r][3*(x//3)+c] == n:
				return False

	return True

def search(lev):
	global matrix, pos

	# base case
	if lev == len(pos): # 스도쿠 완성
		for i in range(9):
			for j in range(9):
				print(matrix[i][j], end=' ')
			print()
		exit(0)
		return

	y, x = pos[lev]

	# recursive case
	for n in range(1, 10):
		if is_possible(y, x, n): 	# 1~9까지 해당 좌표에 가능한지 확인
			matrix[y][x] = n 		# 가능하면 해당 좌표를 채워주고
			search(lev+1)			# 다음 좌표 탐색시키기
			matrix[y][x] = 0

# input
matrix = [list(map(int, input().split())) for _ in range(9)]

# solve
pos = []			# 값이 0인 좌표만 담아줌
for i in range(9):
	for j in range(9):
		if matrix[i][j] == 0:
			pos.append((i, j))

search(0)