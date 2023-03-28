# 내 풀이

def convert(num, n):            # n진수 변환 함수
    atof = {'10':'A', '11':'B', '12':'C', '13':'D', '14':'E', '15':'F'}
    res = ''
    
    while num:                  
        m = str(num%n)
        num //= n
    
        if m in atof:           # 나머지 m이 10-15사이의 수 -> A-F로 변환
            m = atof[m]
        
        res += m                # 나머지를 계속 추가해준 다음 역순으로 리턴
    return res[::-1]


def solution(n, t, m, p):

    nums = '0'                  # 0 미리 추가해주고 i 1부터
    i = 1

    while len(nums) <= t*m :    # nums의 길이가 t*m을 넘으면 스탑

        nums += convert(i, n)   # nums에 변환한 진수를 차곡차곡 넣어준다
        i += 1
    
    return nums[p-1::m][:t]     # nums길이는 p-1부터 끝까지 m씩 건너뛰어서 담아준 다음, t만큼 잘라서 출력

'''
문제에서 10-15를 A-F로 바꾼다는 말을 처음에 이해를 못했다
구글에서 16진수표 보고 깨달아서 열심히 구현 
진수 변환할 때 나머지 확인하고 10-15면 바꿔주는게 포인트인 것 같다

그리고 최종 답 출력할 때, 슬라이싱으로 하고 싶었는데 잘 안돼서 처음엔 계속 실패뜨다가
저렇게 바꿔주니까 됐다 다행이다 힘들었다
'''