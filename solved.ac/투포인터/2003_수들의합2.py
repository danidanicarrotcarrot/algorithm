# 내 풀이 504ms

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
n = list(map(int, input().split()))

left, right, cnt = 0, 1, 0

while left <= right and right <= N :

    res = sum(n[left:right])   # left, right까지 슬라이싱해서 sum
    
    if res < M:                # M보다 작으면 right + 1
        right += 1     
    elif res > M:              # M보다 크면 left + 1
        left += 1
    else:                      # M이랑 같으면 카운트, left + 1
        cnt += 1
        left += 1
        
print(cnt)

'''
left, right로 리스트의 인덱스를 옮겨주면서 sum한 값이 M과 같아지면 카운트+1
'''