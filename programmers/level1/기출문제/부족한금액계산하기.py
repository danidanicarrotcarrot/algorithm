# 다현 풀이
def solution(price, money, count):
    ans = 0
    for i in range(1, count+1):       # 1부터 count까지 돌면서 price에 곱해주고
        ans += price*i                # ans에 추가시켜줌
    return abs(ans - money) if ans > money else 0   # ans가 가진 돈보다 클 경우 차액의 절댓값, 아니면 0 리턴

# 다른 사람 풀이
def solution2(price, money, count):
    return max(0,price*(count+1)*count//2-money)

'''
ㄷ..  max 미쳤넹..
'''