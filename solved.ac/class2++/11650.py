# 좌표 정렬하기
import sys
input = sys.stdin.readline

n = [list(map(int, input().split())) for _ in range(int(input()))]

n.sort(key=lambda x:(x[0], x[1]))

for i in n:
    print(i[0], i[1])