# 내 풀이
def date(x):                                   # date를 받아 전체 일수로 바꿔주는 함수
    year, month, day = map(int, x.split('.'))
    return (year*12*28) + (month*28) + day

def solution(today, terms, privacies):
    today = date(today)                    # 오늘 날짜 -> 일수로 변경
    
    term = {}
    for t in terms:                        # 약관 종류 -> key, 개월 수 -> values 
        x, y = t.split()                   # 개월 수를 일수로 변경해서 담아줌
        term[x] = int(y)*28
        
    res = []
    for idx, p in enumerate(privacies):    # 개인정보
        x, y = p.split()           
        if date(x)+term[y] <= today:       # 가입 일자 + 약관 개월 수 <= 오늘 날짜 -> 유효기간 지난 것으로 간주
            res.append(idx+1)              # 인덱스 + 1 을 res에 담아줌
    
    return res

'''
테스트 1 〉	통과 (0.03ms, 10.4MB)
테스트 2 〉	통과 (0.04ms, 10.4MB)
테스트 3 〉	통과 (0.03ms, 10.3MB)
테스트 4 〉	통과 (0.03ms, 10.4MB)
테스트 5 〉	통과 (0.03ms, 10.4MB)
테스트 6 〉	통과 (0.05ms, 10.4MB)
테스트 7 〉	통과 (0.06ms, 10.4MB)
테스트 8 〉	통과 (0.04ms, 10.5MB)
테스트 9 〉	통과 (0.07ms, 10.4MB)
테스트 10 〉	통과 (0.12ms, 10.2MB)
테스트 11 〉	통과 (0.12ms, 10.3MB)
테스트 12 〉	통과 (0.12ms, 10.3MB)
테스트 13 〉	통과 (0.12ms, 10.3MB)
테스트 14 〉	통과 (0.08ms, 10.3MB)
테스트 15 〉	통과 (0.07ms, 10.5MB)
테스트 16 〉	통과 (0.12ms, 10.4MB)
테스트 17 〉	통과 (0.12ms, 10.4MB)
테스트 18 〉	통과 (0.23ms, 10.4MB)
테스트 19 〉	통과 (0.12ms, 10.3MB)
테스트 20 〉	통과 (0.13ms, 10.3MB)

datetime을 써야하나 고민했지만
한달을 28일로 정해놔서 그냥 일수로 하는게 가장 편할 것 같았다
'''