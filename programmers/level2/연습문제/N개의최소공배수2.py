# 내 풀이
def lcm(x, y):
    xy = x*y                # x y의 최소공배수 = x*y // x y 최대공약수
    while y:
        x, y = y, x%y
    return xy//x

def solution(arr):          
    x = arr.pop()           
    while len(arr):         # arr가 비워질 때까지 반복
        y = arr.pop()       
        x = lcm(x, y)       # 두 수의 최소공배수를 x에 대입
    return x                # 마지막 최소공배수 리턴

'''
두 수의 최소공배수로 나온 값을 또 다음 수와 최소공배수를 구해주는 식으로 반복
'''