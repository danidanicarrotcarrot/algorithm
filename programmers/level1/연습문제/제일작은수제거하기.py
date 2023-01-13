# 다현 풀이
def solution(arr):
    arr.pop(arr.index(min(arr)))      # 배열에서 가장 작은 수의 인덱스를 제거
    return arr or [-1]                # 그대로 리턴 혹은 -1 리턴

# 다른 사람 풀이
def rm_small(mylist):
    return [i for i in mylist if i > min(mylist)] # 가장 작은 수보다 큰 것만 리스트로 담아서 리턴

'''
ㅎㅎ 생각보다.. 간단했당..
'''