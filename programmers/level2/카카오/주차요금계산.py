# 내 풀이

from collections import defaultdict                    # defaultdict(int) -> value가 0으로 세팅되어 있어서 값을 더해줄 수 있음
import math                                            # 나중에 값 올림해서 계산해야 함

def solution(fees, records):
    b_time, b_fee, o_time, o_fee = fees[0], fees[1], fees[2], fees[3] # 기본 시간, 기본 요금, 단위 시간, 단위 요금
    total_fee, in_, total_time = dict(), dict(), defaultdict(int)     # 최종 요금, 입차 확인, 입출차 시간 기록용 dict
    
    for record in records:                  
        r = record.split()
        time, car = r[0], r[1]                          # "05:34 5961 IN" -> time = 05:34, car = 5961, IN
        m, s = map(int, time.split(':'))                # m = 5, s = 34
    
        if car in in_:                                  # 입차 기록이 있으면 total_time에 (현재 시간-들어온 시간) 더해줌
            total_time[car] += (m*60+s)-(in_[car][0]*60+in_[car][1])
            in_.pop(car)                                # 해당 입차 기록 삭제
        else:                                  
            in_[car] = [m, s]                           # 입차 기록 / in에 키, 값 추가 
    
    if len(in_):                                        # 출차 기록이 없는 경우
        for k, v in in_.items():                        # 23:59를 출차로 간주해서 계산 후 total_time에 추가
            total_time[k] += (23*60+59)-(v[0]*60+v[1])
    
    
    for k, v in total_time.items():                     # 최종 요금 계산하기 / total_time에서 차 번호, 시간 get
        if v <= b_time:                                 # 기본 시간보다 적으면 total_fee에 기본요금 저장
            total_fee[k] = b_fee
        else:                                           # 기본 시간을 넘으면 단위 시간, 단위 요금으로 계산한 후 저장
            total_fee[k] = b_fee + math.ceil((v-b_time)/o_time)*o_fee
    
    return [v for k, v in sorted(total_fee.items())]    # 차 번호를 기준으로 오름차순 정렬 후 값만 리턴

'''
defaultdict을 잘 기억해두어야겠음 
그냥 dict은 값이 없으면 더해지지 않는데 defaultdict쓰면 간단히 해결된당
'''