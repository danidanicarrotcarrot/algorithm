# 다현 풀이
def solution(s):
    words = s.split(' ')    # 공백 기준으로 단어 쪼개기 (리스트)
    ans = ''                # 빈 문자열 생성
    for word in words:                      # 단어 하나씩 돌면서
        for i in range(len(word)):          # 단어 길이만큼 다시
            if i % 2 == 0:                  # 단어 인덱스가 짝수?
                ans += word[i].upper()      # 대문자로 변환해서 추가
            else:
                ans += word[i].lower()      # 홀수면 소문자
        ans += ' '                          # 단어 사이사이 공백 추가해주고
    return ans[:-1]         # 마지막 공백 제외하고 리턴

# 다른 사람 풀이
def toWeirdCase(s):
    return " ".join(map(lambda x: "".join([a.lower() if i % 2 else a.upper() for i, a in enumerate(x)]), s.split(" ")))

'''
한줄 ㄷ ㄷ 
'''