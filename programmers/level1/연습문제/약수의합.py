# 이전에 풀었던 거 ~
def solution(n):
    ans = []  # 리스트 만들고
    for i in range(1, n + 1):  # 1부터 n 까지
        if n % i == 0:  # 0으로 나누어떨어지면 i는 n의 약수
            ans.append(i)
    return sum(ans)


# 똑같네 ㅎㅅㅎ
def solution(n):
    _sum = 0
    for i in range(1, n + 1):
        if n % i == 0:
            sum += i
    return sum


# 다른 사람 풀이
def sumDivisor(num):
    return sum(filter(lambda x: num % x == 0, range(1, num + 1)))


#filter 함수?
# filter(조건 함수, 순회 가능한 데이터)
'''
람다로 조건 함수를 만들어주고, 1부터 num + 1 만큼 순회시킴
조건에 맞는 수만 걸러짐
그걸 sum 해서 return
'''
'''
#filter 함수?
filter(조건 함수, 순회 가능한 데이터)
'''
