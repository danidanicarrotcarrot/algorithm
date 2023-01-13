# 다현쓰 풀이
def solution(n):
    return min([i for i in range(1, n) if n%i == 1])

# 다른 사람 풀이
def solution2(n):
    return [x for x in range(1,n+1) if n%x==1][0]

'''
뭐 그냥 비슷한둣 ..?
for 문으로 1부터 n까지 하나하나 넣어보고 조건에 해당하는 수만 리스트에 담아서 젤 작은 수를 return
'''