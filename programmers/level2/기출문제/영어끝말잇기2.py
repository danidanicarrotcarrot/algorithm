# 내 풀이
def solution(n, words):
    end = [i[-1] for i in words[:-1]]   # ["k","k","w","l","d","m","r","t"] 단어의 끝 글자만 담아줌 / 맨 마지막 단어 제외
    repeat = [words[0]]                 # 반복 확인용, 첫번째 단어 미리 넣어줌
    ans = 1
    
    for w, e in zip(words[1:], end):    # 두번째 단어부터 확인
        ans += 1                        # 단어 순서 카운트

        if w[0] != e or w in repeat:    # 단어의 첫 글자와 end 리스트의 글자가 다르거나 / 단어 반복 시 스탑
            break
        else:
            repeat.append(w)            # 조건문에 걸리지 않으면 repeat에 넣어준다

    else:
        return [0, 0]                   # for문을 다 돌았으면 걸리는 게 없으므로 ans = 0, 0
    
    a = ans%n                           # 틀린 사람 번호
    b = ans//n                          # 차례
    
    return [n, b] if not a else [a, b+1]    # 나머지가 없으면 n이 번호, 몫이 차례이므로 n, b로 출력
                                            # 나머지가 있으면 나머지가 번호, 몫 + 1 이 차례이므로 a, b+1로 출력

# 다른 사람 풀이
def solution2(n, words):
    for p in range(1, len(words)):
        if words[p][0] != words[p-1][-1] or words[p] in words[:p]: return [(p%n)+1, (p//n)+1]
    else:
        return [0,0]

'''
열심히 풀어봤다,,
하지만 다른 사람 풀이를 보고 너무 놀랬다
'''