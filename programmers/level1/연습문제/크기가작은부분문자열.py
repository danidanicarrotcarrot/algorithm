# 내 풀이
def solution(t, p):
    nums = [t[i:i+len(p)] for i in range(len(t)-(len(p)-1))]  # ['314', '141', '415', '159', '592']
    return len([num for num in nums if num <= p])             # p보다 작은 부분만 리턴

# 다른 사람 풀이
def solution2(t, p):
    return len([1 for i in range(len(t)-len(p)+1) if t[i:i+len(p)] <= p]) # 더 간결

'''
범위 지정이나 슬라이싱은 비슷하지만 밑에 풀이는 바로 대소비교해서 담아줬음
그리고 어차피 리스트 길이 구하는거니까 원소를 1로 담넹.. 오 .. 나도 담엔 이렇게 해야겠다
''' 