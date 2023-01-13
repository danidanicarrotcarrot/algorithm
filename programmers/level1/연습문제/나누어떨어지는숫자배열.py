# 다현 풀이
def solution(arr, divisor):
    ans = []                    # 리스트 생성
    for i in arr:               # 배열에서 하나씩 꺼내서
        if i%divisor == 0:      # 0으로 나누어 떨어지면 리스트에 담아줌
            ans.append(i)
    return sorted(ans) if ans else [-1] # 리스트 길이가 0이면 -1, 아니면 리스트 리턴

# 다른 사람 풀이
def solution2(arr, divisor): return sorted([n for n in arr if n%divisor == 0]) or [-1]

'''
같은 내용을 한줄로 ...!!!
'''