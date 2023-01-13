# 내 풀이
from collections import deque

N, M = map(int, input().split())            # n, m 입력
idx = list(map(int, input().split()))       # m의 위치 각각 입력받아서 리스트로

q = deque(i for i in range(1, N+1))         # 1~N까지 큐 생성
cnt = 0                                     # 2, 3번 연산 횟수

for i in idx:                           # idx 에서 하나씩
    while idx :              
        if q[0] == i:                   # q의 첫번째 원소가 뽑아야 하는 원소면 그대로 없애고 스탑
            q.popleft()
            break
        elif q.index(i) <= len(q)//2:   # q길이//2 보다 i의 인덱스가 더 작으면 -1만큼 돌림 (2번연산)
            q.rotate(-1)
            cnt += 1
        else :
            q.rotate(1)                 # 더 크면 1만큼 rotate(3번연산)
            cnt += 1
print(cnt)

'''
문제 이해부터 어려웠다
rotate라는 기능이 있음 -> rotate(data, 1) data라는 리스트를 1만큼 회전시킬 수 있음
ex) [1,2,3,4] -> rotate(1) -> [4,1,2,3]
n을 넣으면 n만큼 넣는대로 순서를 회전시킬 수 있음 -도 가능
'''