# 다현 풀이
def solution(A) :
    a = A[::-1]  # 뒤집고
    ans = ''     # 빈 문자열 생성
    for i in range(len(a)) :    # 길이만큼 for 문
        if i < 4 :              # 뒤에서 4개만 ans에 추가
            ans += a[i] 
        else :                  # 그 외에는 *넣기
            ans += '*'
    return ans[::-1]            # 다시 뒤집어서 리턴

# 다른 사람 풀이
def hide_numbers(s):
    return "*"*(len(s)-4) + s[-4:]

'''
않이 ;;;;;;;;;;; 곱셈이 되네요 
'''