# 내 풀이
def solution(s):
    s = s.lower()
    return True if s.count('p') == s.count('y') else False

'''
모두 소문자로 변환해서 p개수 = y개수 면 True 반환
다른 풀이도 비슷한 것 같아서 생략
'''