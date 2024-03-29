# 다현 풀이
def solution(n, m):
    x, y = n, m          # x, y에 각각 넣어주고
    while y:             # y가 0이 될 때까지
        x, y = y, x%y    # x, y에 y, x%y대입
    return x, n*m//x     # 이때 x가 최대공약수, 두 수 곱하고 최대공약수로 나눠준 게 최소공배수

'''
흠.. 역시 최대공약수 최소공배수는 유클리드 호제법만 확실히 알면 편한 것 같다
'''