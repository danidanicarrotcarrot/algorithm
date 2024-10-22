# 트리_1991.py
# 트리 순회 / 실버 1

def pre_order(node):				# 전위 순회
	global tree

	# base case
	if node == -18:
		return

	print(chr(node+64), end='')
	pre_order(tree[node][0])
	pre_order(tree[node][1])

def in_order(node):					# 중위 순회
	global tree

	# base case
	if node == -18:
		return

	in_order(tree[node][0])
	print(chr(node+64), end='')
	in_order(tree[node][1])

def post_order(node):				# 후위 순회
	global tree

	# base case
	if node == -18:
		return

	post_order(tree[node][0])
	post_order(tree[node][1])
	print(chr(node+64), end='')

# input
N = int(input())
tree = [['.', '.'] for _ in range(N+1)]

for _ in range(N):
	a, b, c = input().split()
	tree[ord(a)-64] = [ord(b)-64, ord(c)-64]

pre_order(1)
print()
in_order(1)
print()
post_order(1)