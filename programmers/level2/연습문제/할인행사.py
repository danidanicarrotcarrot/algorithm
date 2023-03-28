# 내 풀이

from collections import Counter

def solution(want, number, discount):

    wn = Counter([w for w, n in zip(want, number) for _ in range(n)]) # 원하는 제품 목록 카운터
    cnt = 0                                 # 회원가입 가능한 일수
    
    for i in range(len(discount)-9):        # 10일 만큼만 회원 자격이 되니까 할인제품 길이 - 9로 range설정
        
		dc = Counter(discount[i:i+10])      # 10개씩 슬라이싱해서 할인 목록 카운터 생성
        
		if not len(wn-dc):                  # 차집합이 0이면 [원하는 제품 목록 = 할인 목록] 이므로 cnt + 1
            cnt += 1
    
    return cnt

'''
카운터로 차집합을 사용해보자 하고 구현
'''