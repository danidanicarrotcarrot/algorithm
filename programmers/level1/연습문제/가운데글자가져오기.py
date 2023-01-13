# 다현 풀이
def solution(s):
    x = len(s)//2           # 길이를 반 잘라놓음
    if len(s)%2 == 0:       # 짝수면은
        return s[x-1]+s[x]  # x-1번째 글자 + x번째 글자
    else:
        return s[x]         # 홀수면 x번째ㅐ만

# 다른 사람 풀이
def string_middle(str):
    return str[(len(str)-1)//2:len(str)//2+1] 

'''
슬라이싱 안에도 len이런게 들어가넹 신기하다,,ㅎ
'''