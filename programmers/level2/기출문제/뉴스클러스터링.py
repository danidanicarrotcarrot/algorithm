# 내 풀이

from collections import Counter

def strtocounter(str0):        # 문자열 2개씩 끊어서 카운터로 바꾸는 함수 (알파벳만)
    res = [str0[i:i+2] for i in range(len(str0)-1) if str0[i:i+2].isalpha()]
    return Counter(res)

def solution(str1, str2):
    fst = strtocounter(str1.upper()+'0') # 대문자로 바꾼 다음 문자열에 0추가(슬라이싱 인덱스 에러 방지)->카운터로 바꿔줌
    scd = strtocounter(str2.upper()+'0')

    a = len(list((fst&scd).elements()))  # 교집합 원소 개수
    b = len(list((fst|scd).elements()))  # 합집합 원소 개수
    
    if a or b:                           # 교집합과 합집합 중 하나라도 공집합이 아니면 교/합*65536
        return int(a/b*65536)
    else:                                # 둘 다 공집합이면 1*65536
        return 1*65536

'''
처음에 set으로 했다가 틀리길래 중복이 제거가 되면 안되는구나 싶어서 Counter로 함
[aa, aa] 를 set으로 바꾸면 [aa] 가 됨 -> 실패

문자열 2개씩 슬라이싱으로 끊고 해당 원소가 알파벳으로 이루어져있으면 리스트에 추가
리스트를 카운터로 변경
두 카운터의 교집합, 합집합을 구하고 elements()로 개수 확인, 교집합/합집합*65536으로 리턴
'''