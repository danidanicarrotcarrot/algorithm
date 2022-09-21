# 수 정렬하기 3

import sys
input = sys.stdin.readline

count = [0] * 10001

for _ in range(int(input())):
    count[int(input())] += 1

for i in range(10001):
        for j in range(count[i]):
            print(i)      