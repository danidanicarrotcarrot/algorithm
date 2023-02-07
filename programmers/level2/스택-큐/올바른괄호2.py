# 내 풀이
def solution(s):
    q = []
    
    for x in s:
        if len(q) and x == ')' and q[-1] == '(' : q.pop()
        else : q.append(x)

    return len(q) == 0

'''
q[-1] = '(' 이면서 x = ')' 일때만 pop 할 수 있도록 설정
그 외에는 모조리 append
'''