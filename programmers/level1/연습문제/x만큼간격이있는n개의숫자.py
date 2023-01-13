# 다현쓰 풀이
def solution(x, n):
    sol = []
    for i in range(n):
        sol.append(x+(i*x))       # x에 i*x를 더해준 다음 sol에 추가
    return sol

# 다른 사람 풀이
def number_generator(x, n):
    return [i * x + x for i in range(n)]

'''
한줄로..
'''