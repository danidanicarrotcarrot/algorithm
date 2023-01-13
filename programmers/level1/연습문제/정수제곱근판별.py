# 내 풀이
def solution(n):
    for i in range(1, n+1):
        if i**2 == n:
            return (i+1)**2
    else:
        return -1

'''
걍 무지성으로 풀고나서 다른 답들을 보니까 나처럼 생각한 사람은 없네 싶어서 슬펐다
왜 난 제곱근을 만들 생각을 안했지 ? ㅎ 

1부터 n까지 돌리면서 i제곱이 n이면 i+1제곱 리턴
'''

# 다른 사람 풀이
def nextSqure(n):
    sqrt = n ** (1/2)

    if sqrt % 1 == 0:
        return (sqrt + 1) ** 2
    return -1

'''
1/2 제곱은 제곱근 !
sqrt을 1로 나누었을 때 나머지가 0인지 확인 == sqrt가 정수인지 확인
정수면 sqrt+1 의 제곱 반환
'''

# 다른 사람 풀이 2
def nextSqure2(n):
    sqrt = pow(n, 0.5)
    return pow(sqrt + 1, 2) if sqrt == int(sqrt) else -1

'''
pow(n, 0.5) -> n의 0.5승 즉 제곱근
int사용해서 제곱근이 정수인지 확인
pow(sqrt+1, 2)로 답 리턴
'''