# 내 풀이

import heapq

def solution(scoville, K):

    heapq.heapify(scoville)                     # 리스트 -> 힙

    cnt = 0                                     # 섞은 횟수 카운트
    fst = heapq.heappop(scoville)               # 제일 작은 스코빌 지수 fst

    while fst < K:                              # 최소 힙이 K보다 작을 때만
        scd = heapq.heappop(scoville)           # 두번째로 작은 스코빌 지수 scd
        heapq.heappush(scoville, fst+(scd*2))   # fst와 scd를 섞어서 heap에 넣어줌
        cnt += 1                                # 카운트 + 1
        fst = heapq.heappop(scoville)           # 다시 제일 작은 스코빌 지수 꺼내주고
        
        if fst < K and len(scoville) == 0:      # fst가 k보다 작고 남은 스코빌 지수가 없으면 -1 리턴
            return -1
        
    return cnt                                  # 섞은 횟수 리턴

'''
while문 안에 if 조건 안 넣어줬을 때 자꾸 테스트케이스 4개가 런타임 에러가 났다
-1 리턴 조건을 잘 생각해보고 추가해줌으로써 해결 !
heap은 정말 유용한 것 같다
'''