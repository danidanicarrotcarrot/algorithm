# 내 풀이
def solution(n):
    return sum([int(i) for i in str(n)]) # str 변환해서 각 자릿수 i를 리스트에 담은 후 sum

# 다른 사람 풀이
def sum_digit(number):
    return sum(map(int,str(number))) # str(number)각 인덱스에 int()함수를 수행해서 변환 후 sum()

'''
다들 비슷하게 풀었던데
한줄 코딩 얏호
'''