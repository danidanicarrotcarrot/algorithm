# 내 풀이 -> 테스트 케이스는 틀린데 정확성 테스트는 다 맞음 ;; 문제가 이상한 듯
def solution(citations):
    c = sorted(citations, reverse = True)  # 내림차순 정렬
    for i in range(len(c)):                # 리스트 길이만큼
        h = c[i]                           # h -> 인용 횟수
        if len(c[:i+1]) >= h :             # h번 이상 인용 논문 수 >= 인용 횟수 -> 리턴
            return i
    else:
        return len(c)                      # ex)[4, 4, 4] -> 리스트 수 리턴
'''
테스트 1 〉	통과 (0.26ms, 10.1MB)
테스트 2 〉	통과 (0.68ms, 10.2MB)
테스트 3 〉	통과 (0.53ms, 10.1MB)
테스트 4 〉	통과 (0.39ms, 10.3MB)
테스트 5 〉	통과 (0.60ms, 10.2MB)
테스트 6 〉	통과 (0.76ms, 10.2MB)
테스트 7 〉	통과 (0.23ms, 10MB)
테스트 8 〉	통과 (0.02ms, 10MB)
테스트 9 〉	통과 (0.05ms, 10.2MB)
테스트 10 〉	통과 (0.21ms, 10.2MB)
테스트 11 〉	통과 (0.78ms, 10.3MB)
테스트 12 〉	통과 (0.06ms, 10.2MB)
테스트 13 〉	통과 (0.72ms, 10.1MB)
테스트 14 〉	통과 (0.65ms, 9.89MB)
테스트 15 〉	통과 (0.75ms, 10.4MB)
테스트 16 〉	통과 (0.01ms, 10MB)
'''

# 내 풀이 2 -> 테스트 케이스, 정확성 테스트 둘 다 통과
def solution(citations):
    c = sorted(citations, reverse = True)
    for i in range(len(c)):
        h = c[i]
        if i >= h :
            return i
    else:
        return len(c)
'''
테스트 1 〉	통과 (0.10ms, 10MB)
테스트 2 〉	통과 (0.16ms, 10.2MB)
테스트 3 〉	통과 (0.10ms, 10.2MB)
테스트 4 〉	통과 (0.09ms, 10.1MB)
테스트 5 〉	통과 (0.15ms, 10.2MB)
테스트 6 〉	통과 (0.13ms, 10.1MB)
테스트 7 〉	통과 (0.04ms, 10.1MB)
테스트 8 〉	통과 (0.01ms, 10.2MB)
테스트 9 〉	통과 (0.02ms, 10.2MB)
테스트 10 〉	통과 (0.07ms, 10.1MB)
테스트 11 〉	통과 (0.13ms, 10.3MB)
테스트 12 〉	통과 (0.02ms, 10.2MB)
테스트 13 〉	통과 (0.12ms, 10.1MB)
테스트 14 〉	통과 (0.16ms, 10.2MB)
테스트 15 〉	통과 (0.13ms, 10.2MB)
테스트 16 〉	통과 (0.00ms, 10.2MB)
'''

# 다른 사람 풀이
def solution2(citations):
    citations.sort(reverse=True)
    answer = max(map(min, enumerate(citations, start=1)))
    return answer

'''
enumerate(list, start=1) -> index가 0이 아닌 1부터 시작
유용할 것 같으니 기억해두자 !!
'''