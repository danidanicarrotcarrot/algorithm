# 다현쓰 풀이
def solution(a, b):
    a, b = min(a, b), max(a, b)             # 둘 중 작은 수가 a, 큰 수가 b
    return sum([i for i in range(a, b+1)])  # a, b 사이의 모든 수 sum

# 다른 사람 풀이
def adder(a, b):
    if a > b: a, b = b, a
    return sum(range(a,b+1))

'''
절댓값으로 푸는 법은 밑에 있길래 다른 풀이 가져왔당
range와 sum만으로 a, b사이의 모든 값을 더할 수 있음
'''