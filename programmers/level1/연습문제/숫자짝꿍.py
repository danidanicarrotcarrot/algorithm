# 내 풀이 1 -> 시간초과
def solution(X, Y):
    x, y = sorted(X), sorted(Y)

    res = []
    for i in x:
        if i in y:
            y.remove(i)
            res.append(i)

    return '-1' if not len(res) else (
        '0' if res[-1] == '0' else ''.join(res[::-1]))


# 내 풀이 2
def solution2(X, Y):
    ans = ''
    strnum = [str(i) for i in reversed(range(10))
              ]  # ['9', '8', '7', '6', '5', '4', '3', '2', '1', '0']

    for s in strnum:
        ans += s * min(X.count(s), Y.count(s))  # count값이 더 낮은 만큼만 곱해서 ans에 추가

    return '-1' if not ans else ('0' if ans[0] == '0' else ans
                                 )  # '00' -> 0, '' -> 1


'''
처음엔 각각 정렬해놓고 x에 있는 숫자를 y에서 찾은 다음 없애고 
ans에 append하는 식으로 해줬는데 시간초과가 났다
이후 삽질한 모든 풀이가 런타임 초과 or 시간초과 or 실패.. 좌절

포기하고 다음날 맑은 정신으로 풀었다 
질문하기 들어가서 보고 0-9 까지의 수니까 그걸 잘 이용하라고 나와있길래 열심히 생각
-> for문 안에 9-0 넣어준 다음 count함수로 세고 더 작은 수만큼 ans에 추가.. 이렇게 쉬운걸..

조건문 뭔가 줄여보고 싶어서 검색해보니 될 것 같길래 적용해봤다 히히

if not ans:
    return '-1'
elif ans[0] == '0'
    return '0'
else:
    return ans

===> return '-1' if not ans else ('0' if ans[0]=='0' else ans)

ans에 원소가 있는지 없는지 먼저 구분해서 if 나눠주고 
그 안에서 또 if랑 else로 나눠서 return 
elif는 안된다고 함
'''