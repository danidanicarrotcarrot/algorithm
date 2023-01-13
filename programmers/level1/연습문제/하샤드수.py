# 다현쓰 풀이 (지이이이난번에 푼거)
def solution(x):
    arr = [int(i) for i in str(x)]
    return x%sum(arr) == 0

# 다현쓰 풀이 (이번에 푼거)
def solution2(x):
    return True if x % sum(map(int, str(x))) == 0 else False 

'''
양의 정수 x 를 각 자릿수 합으로 나눈 나머지가 0이면 True 아니면 False 반환
'''

# 다른 사람 풀이
def Harshad(n):
    return n % sum([int(c) for c in str(n)]) == 0

'''
뭐.. 다 비슷하게 푸는 것 같다
'''