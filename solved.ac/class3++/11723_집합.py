# 내 풀이 (30616, 2948ms)
import sys
input = sys.stdin.readline

s = set()
for _ in range(int(input())):
    i = input().split()
    
    if i[0] == 'add' :
        if i[1] not in s:
            s.add(i[1])

    elif i[0] == 'remove':
        if i[1] in s:
            s.remove(i[1])

    elif i[0] == 'check':
        if i[1] in s:
            print(1)
        else:
            print(0)

    elif i[0] == 'toggle':
        if i[1] in s:
            s.remove(i[1])
        else:
            s.add(i[1])

    elif i[0] == 'all':
        s = {'1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20'}

    elif i[0] == 'empty':
        s.clear()

'''
처음에 add랑 remove 연산에 조건을 안 걸었더니 (if i[1] in s) 런타임 에러가 계속 났고
all 연산도 {str(i) for i in range(1, 21)} 로 했더니 시간초과
그 두가지 수정해서 겨우겨우 통과 ㅠㅠㅠ

밑에 두 분 거랑 비교해보니까 다들 list로 하셨던데 set이 시간이 조금 더 빠르다
set은 in, not in 연산이 O(1)이라 그런 것으로 추정된당..
'''