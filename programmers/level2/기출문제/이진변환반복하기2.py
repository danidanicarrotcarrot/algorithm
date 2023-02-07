# 내 풀이
def solution(s):
    
    cnt = 0     # 변환 횟수
    z = 0       # 제거된 0 개수
    
    while s != '1':
        cnt += 1                         # 변환 횟수 + 1
        z += s.count('0')                # 0 개수 카운트해서 z에 추가
        s = bin(int(s.count('1')))[2:]   # 1개수 구해서 2진수로 변환, bin '0b110' -> '110'
    
    return [cnt, z]

'''
생각보다 간단했던 문제
다른 풀이도 비슷하다
'''