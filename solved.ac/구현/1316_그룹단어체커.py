# 그룹 단어 체커

# 다현쓰 풀이 (72ms)

words = [input() for _ in range(int(input()))] # input 받아서 단어 리스트 생성
cnt = 0                                        # 그룹 단어 체크용 cnt

for word in words:                             # 리스트에서 word 하나씩 꺼냄
    group = ''                                 # group 이라는 빈 str 변수 생성
    for w in word:                             # word 에서 또 단어 하나씩 꺼냄
        if w not in group or group[-1] == w:   # w 가 group에 없음 or 마지막으로 추가된 단어가 같을 때만
            group += w                         # group에 w 추가
    if word == group:                          # group과 기존 단어 word를 비교해서 같으면 그룹 단어니까
        cnt += 1                               # cnt + 1

print(cnt)

-------------------------------------------------------------

# 다른 사람 풀이 (72ms)

num = int(input())
result = num                        # 답을 일단 num 개수와 동일하게 설정하고 시작

for i in range(num):                # num 만큼 반복
    word = input()                  # 단어 받아와서
    for j in range(0, len(word)-1): # 단어 길이만큼 for문 반복
        if word[j] == word[j+1]:    # j번째 문제가 j+1과 같은 경우면 패스, 달라도 상관 없음,
            pass
        elif word[j] in word[j+1:]: # 현재 알파벳이 뒤에 나온다면 그룹문자에서 제외
            result -= 1             
            break
print(result)

'''
이게 왜 되지 22
걍 무지성으로 했는데 돼서 당황했따.. 
str도 list랑 비슷하게 not in 이 되고 인덱스로 접근하는거랑 + 하면 합쳐지는 것도 편하당

다 풀고 다른 사람풀이 보다가 재현님이 가져오신거랑 창민님 가져오신거 보고 헉 함
저런 방법이 ㄷ 
'''