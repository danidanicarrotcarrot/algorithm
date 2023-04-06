# 내 풀이 44ms

import sys
input = sys.stdin.readline

from itertools import combinations
n, m, k = map(int, input().split())

a ,b = 0, 0
for i in combinations(range(1, n+1), m):
    for j in combinations(range(1, n+1), m):
        if len(set(i)&set(j)) >= k:
            a += 1
        b += 1

print(a/b)

'''
브루트포스로 2중 for문 써서 일일히 카운트를 해 주고
같은 수를 뽑은 경우의 수/모든 경우의 수 출력
'''