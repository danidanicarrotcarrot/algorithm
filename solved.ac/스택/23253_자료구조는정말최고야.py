# 내 풀이 292ms

import sys
input = sys.stdin.readline

N, M = map(int, input().split())

answer = 'Yes'
for i in range(M):
    _ = int(input())
    nums = list(map(int, input().split()))

    if nums != sorted(nums, reverse=True):  # 입력받은 값이 내림차순으로 정렬되어있지 않으면 불가능하므로
        answer = 'No'                       # answer를 No로 세팅
        continue

print(answer)

'''
모든 입력받은 값이 내림차순으로 정렬되어있으면 무조건 됨 
'''