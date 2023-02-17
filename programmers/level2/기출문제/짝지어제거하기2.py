# 내 풀이
def solution(s):
    stack = []
    
    for i in s:                       # 문자열에서 하나씩 꺼내서 스택 마지막 원소랑 비교
        if stack and stack[-1] == i:  # 같으면 짝이니까 제거 / 다르면 스택에 추가
            stack.pop()
        else:
            stack.append(i)
            
    return 1 if not stack else 0      # 스택이 다 비었으면 1 출력 아니면 0 출력

'''
스택 문제는 다 풀이법이 비슷한 것 같다
'''