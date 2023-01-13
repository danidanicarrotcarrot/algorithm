# 내 풀이
def solution(n):
    return [int(i) for i in str(n)[::-1]]


'''
str은 슬라이싱이 가능하니까 str로 [::-1]로 뒤집어주고 (ex 12345 -> 54321)
그대로 하나씩 int 변환해서 리스트에 담고 반환
'''


# 다른 사람 풀이
def digit_reverse(n):
    return list(map(int, reversed(str(n))))


'''
reversed 함수 사용해서 뒤집어줌
'''
