def solution(num):
    cnt = 0                   # 작업 반복 수
    while cnt <= 500 :        # 500번 이하일 때
        if num == 1:          # num = 1 이면 cnt 리턴
            return cnt
        elif num % 2 == 0:    # num이 짝수면
            num = num//2      # 2로 나눠주세요
        else:
            num = num*3 + 1   # 홀수면 3 곱하고 1 더해주세요 
        cnt += 1              # cnt 추가
    return -1                 # 500을 넘어가면 -1 리턴


# 다른 사람 풀이
def collatz(num):
    cnt = 0
    while num != 1 and cnt < 500:
        num = 3 * num + 1 if num % 2 else num // 2   # 한 줄로 조건문 ㄷ 
        cnt += 1

    return cnt if cnt < 500 else -1  # return 에도 조건문 ㄷ

'''
저도 짧게 쓰고 싶어요
'''