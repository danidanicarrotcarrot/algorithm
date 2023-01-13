# 수 정렬하기 2

import sys
input = sys.stdin.readline

nums = [int(input()) for _ in range(int(input()))]

nums.sort()

print(*nums, sep='\n')