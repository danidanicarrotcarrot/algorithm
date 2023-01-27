# 내 풀이
import re

def solution(new_id):
    new = new_id.lower()                        # 1. 소문자로
    new = re.sub('[^\-\_\.0-9a-z]', '', new)    # 2. -_.와 문자숫자 제외 공백처리
    new = re.sub('[\.]+', '.', new)             # 3. 마침표 반복되는거 하나로
    new = new.strip('.')                        # 4. 양 옆 마침표 삭제
    new = new[0:15]                             # 5. 15까지만 슬라이싱
    new = new.strip('.')                        # 6. 양 옆 마침표 다시 삭제
    
    if not len(new):                            # 7. 문자열이 비었으면 a추가
        new = 'a'
    
    if len(new) < 3:                            # 8. 문자열 < 3 이면 마지막 문자 추가
        new += new[-1]*(3-len(new))
    
    return new

'''
보자마자 정규표현식을 써봐야겠다 하고 요리조리 찾아서 열심히 적용해봤당
힘들었다,,, 
'''

# 다른 사람 풀이
def solution2(new_id):
    st = new_id
    st = st.lower()
    st = re.sub('[^a-z0-9\-_.]', '', st)
    st = re.sub('\.+', '.', st)
    st = re.sub('^[.]|[.]$', '', st)               # or 이렇게 쓰면 되는구나;;; 이거 못해서 두줄로 하다가 결국 strip 사용
    st = 'a' if len(st) == 0 else st[:15]
    st = re.sub('^[.]|[.]$', '', st)
    st = st if len(st) > 2 else st + "".join([st[-1] for i in range(3-len(st))])
    return st

'''
더 깔끔한 것 같당
정규표현식도 잘 공부해두어야겠음 ㅠㅠ
'''