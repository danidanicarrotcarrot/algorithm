# 내풀이
def solution(sizes):
    max_ = []                     # [a,b] 중 큰 수를 담을 리스트
    min_ = []                     # 작은 수 리스트
    for i in sizes:         
        max_.append(max(i))
        min_.append(min(i))
        
    return max(max_) * max(min_)  # 큰 수 중 가장 큰 수 * 작은 수 중 젤 큰 수

# 다른 사람 풀이
def solution2(sizes):
    return max(max(x) for x in sizes) * max(min(x) for x in sizes)

'''
첨에 뭔말인지 몰라서 어려웠는데 
읽다보니 그냥 큰 거중에 젤 큰거랑 작은거 중에 젤 큰거 하면 명함 다들어가겠지 하고 한듯..
'''