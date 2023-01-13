# JadenCase 문자열 만들기
def solution(s):
    jc = s.split(' ')
    ans = ''
    
    for i in range(len(jc)):
        jc[i] = jc[i].capitalize()
    ans = ' '.join(jc)
    
    return ans