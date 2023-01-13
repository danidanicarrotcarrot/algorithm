# 나이순 정렬
import sys
input = sys.stdin.readline

judge = [list(input().split()) for _ in range(int(input()))]

judge.sort(key=lambda x:int(x[0]))

for i in judge:
    print(int(i[0]), i[1])