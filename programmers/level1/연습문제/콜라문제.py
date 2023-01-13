# ㄴㅍㅇ
def solution(a, b, n):
    total = 0

    while n >= a:                   # n이 a보다 클 때 (보유 중인 빈 병이 a개 미만이면 stop)
        mart = a*(n//a)             # 마트에 갖다줄 병
        bottle = n - mart           # 남은 빈 병
        coke = b*(mart//a)          # 마트에서 받은 콜라
        n = coke + bottle           # n = 콜라 + 남은 병
        total += coke               # 받은 콜라 카운트
    
    return total

# ㄷㄹ ㅅㄹ ㅍㅇ
def solution2(a, b, n):
    answer = 0

    num = n
    while num >= a:
        cnt = num // a
        num -= (cnt * a)
        num += (cnt * b)
        answer += (cnt * b)

    return answer

'''
비슷하다.. 고 생각한다..
처음엔 엄청 복잡하게 생각해서 이게 뭐지 하다가 천천히 다시 생각했음
좀 오래걸렸당
'''