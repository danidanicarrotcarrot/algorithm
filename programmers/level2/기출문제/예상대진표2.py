# 내 풀이
def solution(n,a,b):
    cnt = 0
    while a != b:           # 서로 부여받을 번호가 같으면 stop
        cnt += 1            # 라운드 + 1
        a = a//2 + a%2      # 다음 라운드에서 A가 부여받을 번호
        b = b//2 + b%2      # 다음 라운드에서 B가 부여받을 번호
    return cnt

'''
A, B는 같은 라운드에서 만날때까지 항상 이긴다고 가정된다
A 가 3이든 4든 다음 라운드에서는 2번이 됨
B 도 7이든 8이든 다음 라운드에선 4번이 됨

1. 다음 라운드에서 a, b가 부여받을 번호를 반복적으로 구함
2. 두 수가 같아지는 순간 == a, b의 다음 라운드 번호 같음 == 지금 만났음!!
3. 해당 라운드 리턴
'''