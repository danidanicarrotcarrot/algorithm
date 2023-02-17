# 내 풀이 44ms
import sys
input = sys.stdin.readline

n = int(input())
r = list(map(int, input().split()))        # 링 리스트 [8, 4, 2]
first = r[0]                               # 8

def gcd(a, b):               # 최대공약수 구하는 함수
    while b:
        a, b = b, a%b
    return a
    
for i in range(1, n):                      # 링 리스트에서 두번째 원소부터
    g = gcd(r[0], r[i])                    # 최대공약수 구함
    print(str(r[0]//g)+'/'+str(r[i]//g))   # 첫번째 링, i번째 링을 각각 최대공약수로 나눠서 기약분수 형태로 출력

''' 
a, b -> a//a,b의 최대공약수 + / + b//a,b의 최대공약수길래 그대로 구현
'''