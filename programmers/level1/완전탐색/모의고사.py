# 내 풀이
def solution(answers):
    people = [[1, 2, 3, 4, 5]*2000, [2, 1, 2, 3, 2, 4, 2, 5]*1250, [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]*1000]
    count = [0, 0, 0]                           # 어차피 문제 수는 최대 10,000문제, 갯수 맞춰놓고 시작
                                                # 수포자 1, 2, 3 각각 정답 갯수 리스트
    for i in people:                            # 한 명씩 비교
        for j in range(len(answers)):
            if answers[j] == i[j]:
                count[people.index(i)] += 1     # 맞췄으면 count[i] + 1
    
    res = []                                    
    for idx, cnt in enumerate(count):
        if cnt == max(count):                         # max 값이랑 정답 수가 같은 수포자만 res에 담아주고 출력
            res.append(idx+1)
    
    return res

# 다른 사람 풀이
def solution2(answers):
    pattern1 = [1,2,3,4,5]
    pattern2 = [2,1,2,3,2,4,2,5]
    pattern3 = [3,3,1,1,2,2,4,4,5,5]
    score = [0, 0, 0]
    result = []

    for idx, answer in enumerate(answers):
        if answer == pattern1[idx%len(pattern1)]:
            score[0] += 1
        if answer == pattern2[idx%len(pattern2)]:
            score[1] += 1
        if answer == pattern3[idx%len(pattern3)]:
            score[2] += 1

    for idx, s in enumerate(score):
        if s == max(score):
            result.append(idx+1)

    return result

'''
전체 로직은 비슷한 것 같아용?
'''