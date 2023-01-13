# 내 풀이
def solution(num):
    if num % 2 != 0:  # 2로 나누어떨어지지 않으면(홀수) odd 아니면(짝수) even
        return "Odd"
    else:
        return "Even"


# 다른 사람 풀이 1
def evenOrOdd(num):
    return "Even" if num % 2 == 0 else "Odd"  # return도 if가 껴짐


# 다른 사람 풀이 2
def evenOrOdd(num):
    return ["Even", "Odd"][num & 1]


'''
& 연산자로 비트 연산한 후 그 수가 ["Even", "Odd"] 배열의 인덱스가 된다고 함
예를 들어 num = 2면 비트가 10
10와 1의 and 연산을 하면 0이 되니까 
0번째 인덱스인 even이 나옴
'''
'''
파이썬의 세계는 무궁무진하다
이런 게 프로그래머스 푸는 재미.. ?
'''
