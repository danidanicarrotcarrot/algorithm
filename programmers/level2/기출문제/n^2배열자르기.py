# 내 풀이 -> 시간초과
def solution(n, left, right):
    s = ''
    for i in range(1, n+1):
        s += str(i)             # 1234
    
    for j in range(1, n):
        s += s[j]*j + s[j:n]    # 1234223433344444
        
    ans = list(map(int, s[left:right+1]))
    return ans

'''
문자열로 배열을 다 만들려고 했는데 어쨌든 되긴 했지만 수가 너무 커서 그런지 실패
ㅜㅡㅜ
'''

# 내 풀이 2
def solution(n, left, right):
    
    res = []
    
    for i in range(left, right+1):
        ans = max(i//n, i%n) + 1
        res.append(ans)
    
    return res

'''
몫, 나머지 중 큰 값에 + 1을 더해주면 해당 배열 숫자가 됨
'''