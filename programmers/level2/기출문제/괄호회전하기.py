# 내 풀이
def solution(s):
    d = {']':'[', ')':'(', '}':'{'}                 # key: 닫는 괄호/ value: 여는 괄호 
    o = 0                                           # 올바른 괄호 count
    
    for x in range(len(s)):                         # 문자열 길이만큼
        stack = []                                  
        
        for i in s[x:]+s[:x]:                       # 회전
            
            if i in {'[', '(', '{'}:                # 여는 괄호면 일단 추가
                stack.append(i)
            elif len(stack) and stack[-1] == d[i]:  # i : 닫는 괄호(]) + 스택 마지막 원소 : d[i]의 value([) -> pop
                stack.pop()
            else:                                   # 조건문에 걸리지 않으면 append
                stack.append(i)
            
        if not len(stack):          # 스택이 비어있으면 올바른 괄호이므로 + 1
            o += 1
            
    return o

'''
문자열을 계속 회전시켜서 올바른 괄호인지 검증하면 되는 문제였다

테스트 1 〉	통과 (97.77ms, 10.2MB)
테스트 2 〉	통과 (103.06ms, 10.1MB)
테스트 3 〉	통과 (113.74ms, 10.2MB)
테스트 4 〉	통과 (106.51ms, 10.2MB)
테스트 5 〉	통과 (104.93ms, 10.3MB)
테스트 6 〉	통과 (152.75ms, 10.2MB)
테스트 7 〉	통과 (154.45ms, 10.3MB)
테스트 8 〉	통과 (199.24ms, 10.3MB)
테스트 9 〉	통과 (118.29ms, 10.1MB)
테스트 10 〉	통과 (128.20ms, 10.2MB)
테스트 11 〉	통과 (109.64ms, 10.2MB)
테스트 12 〉	통과 (0.00ms, 10.1MB)
테스트 13 〉	통과 (0.01ms, 10.1MB)
테스트 14 〉	통과 (0.01ms, 10.2MB)
'''