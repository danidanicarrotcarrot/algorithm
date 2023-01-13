def solution(s):
    cnt = 0 # 반복횟수
    zero = 0 # 제거된 0 개수

    while True:
        if s == '1':
            break
        zero += s.count('0')
        s = s.replace('0', '')
        s = len(s)
        res = str()
        while s:
            res += str(s%2)
            s = s//2
        s = res[::-1]
        cnt += 1

    return cnt, zero