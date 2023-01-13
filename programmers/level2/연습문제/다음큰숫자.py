def solution(n):
    a = bin(n).count('1')
    while True:
        n += 1
        if bin(n).count('1') == a:
            return n
            break