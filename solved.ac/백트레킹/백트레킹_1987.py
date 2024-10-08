# 백트레킹_1987.py
# 알파벳 / 골드 5

def search(y, x):
	global dy, dx, R, C, board, check, cur_len, ans

	# base case
	if y < 0 or x < 0 or y >= R or x >= C: 	# 좌표를 벗어나면 return
		return
	if check[ord(board[y][x])-ord('A')]:	# 이미 지나간 알파벳이면 return
		return
	check[ord(board[y][x])-ord('A')] = True	# 둘 다 아니면 check 표시해주고
	cur_len += 1

	ans = max(ans, cur_len)

	# recursive case
	for i in range(4):
		ny = dy[i] + y
		nx = dx[i] + x
		search(ny, nx)

	cur_len -= 1
	check[ord(board[y][x]) - ord('A')] = False


import sys
input = sys.stdin.readline

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

R, C = map(int, input().split())
board = [input().strip() for _ in range(R)]

check = [False] * 26
cur_len = 0
ans = 0

search(0, 0)

print(ans)