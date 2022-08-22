# 최대공약수, 최소공배수

def gcd(x, y) :
    while y : # y가 자연수일 때
        x, y = y, x%y
    return x

def lcm(x, y):
    return x*y//gcd(x, y)

x, y = map(int, input().split())
print(gcd(x, y),lcm(x, y), sep='\n')


# 유클리드 호제법 활용
# x, y 최대공약수 = y, x%y의 최대공약수
# 최소 공배수 = 두 수의 곱을 최대공약수로 나눈 몫