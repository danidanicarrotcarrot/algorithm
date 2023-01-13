# 다현 풀이
def solution(s):
    return s.isdigit() and (len(s) == 4 or len(s) == 6)

# 다른 사람 풀이
def alpha_string46(s):
    return s.isdigit() and len(s) in (4, 6)

'''
isdigit은 숫자인지 확인해주는 함수
전에 한 번 써봐서 기억이 났당
len(s) in (4,6) 이라니,, in을 너무 for 문에서만 쓴 듯 이렇게도 쓰는구낭
'''