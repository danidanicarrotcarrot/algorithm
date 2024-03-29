import sys
input = sys.stdin.readline

n, m = map(int, input().split())
trees = list(map(int, input().split()))

start, end = 1, max(trees)

while start <= end:
    mid = (start+end)//2
    cnt = 0

    for tree in trees:
        if tree >= mid:
            cnt += tree - mid

    if cnt < m:
        end = mid - 1
    else:
        start = mid + 1

print(end)