# 내 풀이
def solution(n):
    a_cnt = 0                         # 다음 큰 숫자 1 갯수
    n_cnt = bin(n)[2:].count('1')     # 현재 숫자 1 갯수
    
    while a_cnt != n_cnt:
        n += 1                        # n을 1씩 증가시킴
        a_cnt = bin(n)[2:].count('1') # 1 갯수가 같아지면 스탑
        
    return n

'''
간단했당..
'''