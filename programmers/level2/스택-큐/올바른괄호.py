def solution(s):
    ans = []
    
    for i in s:
        if i == '(':
            ans.append(i)
        elif i == ')':
            if len(ans) != 0 and ans[-1] == '(':
                ans.pop()
            else:
                ans.append('(')
                break
    
    print('true') if len(ans) == 0 else print('false')

solution('(())')