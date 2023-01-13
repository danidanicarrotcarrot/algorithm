# 내 풀이
def solution(array, commands):
    return [sorted(array[i-1:j])[k-1] for i, j, k in commands]

# 다른 사람 풀이
def solution2(array, commands):
    return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))

'''
히히 한줄 냠냠
'''