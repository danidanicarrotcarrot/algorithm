# 다현 풀ㅇㅣ 76ms

from math import factorial   # math 모듈의 factorial 함수 import

n = factorial(int(input()))  # n을 받아서 factorial 해주고
cnt = 0                      # 0 개수 카운트용

while True:
    if n % 10 != 0:          # n을 10으로 나눴을 때 0이 아니면 스탑
        break
    else:
        n //= 10             # 10으로 나눈 몫 ex)3628800 -> 362880
        cnt += 1             # 0 개수 + 1
        
print(cnt)


# 다른 사람 풀이

N = int(input())
print(N//5 + N//25 + N//125)  # ??????


'''
팩토리얼한 다음 계속 10으로 나눠주면 0의 개수를 얻을 수 있다고 생각하고 문제를 풀었음
아니 근데 5의 배수 저거 난 절대로 저렇게 못 풀 것 같은데 ,, 대단하다..
'''