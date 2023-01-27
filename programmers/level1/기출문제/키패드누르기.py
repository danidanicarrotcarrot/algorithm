# 내 풀이
def solution(numbers, hand):
    ans = ''
    key = {
        1: [0, 0],
        2: [0, 1],
        3: [0, 2],  # 좌표 - 키패드 dic으로 만들어두고
        4: [1, 0],
        5: [1, 1],
        6: [1, 2],
        7: [2, 0],
        8: [2, 1],
        9: [2, 2],
        '*': [3, 0],
        0: [3, 1],
        '#': [3, 2]
    }

    r, l = key['#'], key['*']  # right 시작점, left 시작점

    for i in numbers:

        if i in [1, 4, 7]:  # 1,4,7 이면 left
            ans += 'L'
            l = key[i]

        elif i in [3, 6, 9]:  # 3,6,9 면 right
            ans += 'R'
            r = key[i]

        else:  # 그 외 숫자면
            rd, ld = 0, 0  # 오른쪽, 왼쪽 각각 거리 체크
            for a, b, c in zip(r, l,
                               key[i]):  # zip으로 리스트를 묶어서 x, y 좌표 각각의 거리를 계산
                rd += abs(a - c)  # right/현재숫자 x좌표끼리 y좌표끼리 차를 구해서 절댒값 씌우고 더해줌
                ld += abs(b - c)  # left도 마찬가지

            if rd < ld:  # right거리가 더 가까우면 R
                ans += 'R'
                r = key[i]

            elif rd > ld:  # left거리가 더 가까우면 L
                ans += 'L'
                l = key[i]

            else:  # 같은경우 hand에 따라서 결정
                if hand == 'right':
                    ans += 'R'
                    r = key[i]
                else:
                    ans += 'L'
                    l = key[i]
    return ans


'''
모르겠어서 답지 조금 봤당
for 문을 써서 x, y좌표 각각의 차를 구해서 더해주면 된다는게 핵심인 것 같아서 그대로
구현했다 
딕셔너리로로 푸니까 생각보다는 간단하게 풀렸던 문제!
좌표가 정해져 있어서 이런 풀이가 가능했던둣,,,
'''


# 다른 사람 풀이
def solution2(numbers, hand):
    l = 10
    r = 11
    answer = ""
    p = [[0, 4, 3, 4, 3, 2, 3, 2, 1, 2], [4, 0, 1, 2, 0, 2, 3, 0, 3, 4],
         [3, 1, 0, 1, 2, 1, 2, 3, 2, 3], [4, 2, 1, 0, 3, 2, 1, 4, 3, 2],
         [3, 0, 2, 3, 0, 1, 2, 0, 2, 3], [2, 2, 1, 2, 1, 0, 1, 2, 1, 2],
         [3, 3, 2, 1, 2, 1, 0, 3, 2, 1], [2, 0, 3, 4, 0, 2, 3, 0, 1, 2],
         [1, 3, 2, 3, 2, 1, 2, 1, 0, 1], [2, 4, 3, 2, 3, 2, 1, 2, 1, 0],
         [1, 0, 4, 5, 0, 3, 4, 0, 2, 3], [1, 5, 4, 0, 4, 3, 0, 3, 2, 0]]
    for i in numbers:
        if i in [1, 4, 7]:
            l = i
            answer += "L"
        elif i in [3, 6, 9]:
            r = i
            answer += "R"
        else:
            if p[l][i] < p[r][i]:
                l = i
                answer += "L"
            elif p[l][i] > p[r][i]:
                r = i
                answer += "R"
            elif hand == "left":
                l = i
                answer += "L"
            else:
                r = i
                answer += "R"
    return answer


'''
이 사람은 아예 거리를 다 계산해놓고 풀어버림
'''
