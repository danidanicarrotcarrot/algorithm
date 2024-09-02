# 좌표 정렬하기


## 내 풀이
import sys # 엄청 오래걸리므로 sys 추가
input = sys.stdin.readline

N = int(input())
lst = [list(map(int, input().split())) for i in range(N)] # 숫자로 받기
srt = sorted(lst, key = lambda x: (x[0], x[1]))
for s in srt:
	print(*s) # list unzip


## 다른 풀이 > 간단하네/.. 머쓱
N = int(input())
dots = [list(map(int, input().split())) for _ in range(N)]

dots = sorted(dots)

for x, y in dots:
	print(x, y)