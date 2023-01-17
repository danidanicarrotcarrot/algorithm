# 좌표 정렬하기 2
import sys
input = sys.stdin.readline

n = [list(map(int, input().split())) for _ in range(int(input()))]

n.sort(key=lambda x:(x[1], x[0]))

for i in n:
    print(i[0], i[1])