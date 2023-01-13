# 다른 사람 풀이
def solution(s, n):
    answer = ''
    for i in s:
        if i:
            if 'A' <= i <= 'Z':
                answer += chr((ord(i) - ord('A') + n) % 26 + ord('A'))
            elif 'a' <= i <= 'z':
                answer += chr((ord(i) - ord('a') + n) % 26 + ord('a'))
            else : answer += ' '
    return answer


# 다현 풀이 -> 테스트케이스 6/7/8/10/12 실패 -> 왜 ..? ㅠㅠㅠㅠ
def solution2(s, n):
    answer = ''
    for i in s:
        x = ord(i) + n                         # 알파벳 숫자로 바꾼다음 +n
        if i == ' ': 
            answer += ' '
        elif 65 <= x <= 90 or 97 <= x <= 122:  # 더해준 숫자가 저 안에 있으면 그대로 추가
            answer += chr(x)
        else:
            answer += chr(x-26)                # 저 범위안에 없으면 -26해서 추가
    return answer


'''
내 풀이가 잘못된 이유가 뭘까 한참 고민했는뎅.. n을 더해줬을 때 대문자 범위에 들어가버리면 그대로 변환을 해버리는 거였음....
그래서 대문자 소문자 구별해서 하는구나 ..! ㅎㅎ 결국 답지를 보고서야 알았다 ㅠㅡㅠㅠㅠ 어려웡
'''