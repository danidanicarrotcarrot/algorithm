# 다현 풀이
def count(num):
    cnt = 0
    for i in range(1, num+1):
        if num%i == 0:             # i로 나눠서 나누어 떨어지면
            cnt += 1               # cnt + 1
    return cnt                     # 약수 개수 리턴

def solution(left, right):
    ans = 0
    for i in range(left, right+1):
        if count(i)%2 == 0:         # 약수 개수가 짝수면 + 1 아니면 -1
            ans += i
        else:
            ans -= i
    return ans


# 다른 사람 풀이
def solution(left, right):
    answer = 0
    for i in range(left,right+1):
        if int(i**0.5)==i**0.5:
            answer -= i
        else:
            answer += i
    return answer


'''
제곱수는 약수의 개수가 홀수
'''