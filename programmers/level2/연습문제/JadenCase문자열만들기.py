# 내 풀이
def solution(s):
    words = s.lower().split(' ')                       # ["3people","unfollowed","me"]
    
    res = []
    for w in words:
        if w and w[0].isalpha():                       # 맨 첫글자 : 알파벳 -> 첫 글자 대문자로 해서 res에 추가
            res.append(w[0].upper() + w[1:])
        else :
            res.append(w)                              # 숫자 or 공백이면 그냥 바로 추가

    return ' '.join(res)

'''
테스트 케이스 실패 떠서 질문하기 봤는데 
연속공백도 답에 넣어줘야 한다고 하길래 그 부분 수정해서 해결 !
'''

# 내 풀이 2 -> 저번에 푼 거
def solution2(s):
    jc = s.split(' ')

    for i in range(len(jc)):
        jc[i] = jc[i].capitalize()

    return ' '.join(jc)

'''
capitalize() -> 문자열의 첫글자는 대문자로, 나머지는 소문자로 변환한다.
title() -> 문자열 내 띄어쓰기 기준으로 각 단어의 첫글자는 대문자로, 나머지는 소문자로 변환한다.
'''