# 내 풀이
def solution(n):
    f = [0, 1]
    for i in range(2, n+1):
        f.append(f[i-2]+f[i-1])
    return f[-1]%1234567

# 다른 사람 풀이
def fibonacci(num):
    a,b = 0,1
    for i in range(num):
        a,b = b,a+b
    return a

'''
다들 비슷하게 푼 것 같다
'''