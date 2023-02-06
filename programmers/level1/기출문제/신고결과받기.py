# 내 풀이
def solution(id_list, report, k):
    
    report = [i.split() for i in report]  # muzi frodo -> [muzi, frodo]
    rpt = {i:[] for i in id_list}         # ['muzi':[]]
    for x, y in report:
        if x not in rpt[y]:               # rpt['muzi'] 에 frodo가 없으면 frodo 추가
            rpt[y].append(x)              # {'muzi': ['apeach'], 'frodo': ['muzi', 'apeach'], 'apeach': [], 'neo': ['frodo', 'muzi']}
    
    mail = {i:0 for i in id_list}
    for key, val in rpt.items():          # 신고 유저 수가 k 이상 -> 해당 유저 메일 카운트 + 1
        if len(val) >= k:
            for v in val:
                mail[v] += 1
    
    return list(mail.values())             # mail의 values만 리스트로 반환

'''
테스트 1 〉	통과 (0.02ms, 10MB)
테스트 2 〉	통과 (0.03ms, 10.2MB)
테스트 3 〉	통과 (1955.39ms, 83.2MB)
테스트 4 〉	통과 (0.05ms, 10.3MB)
테스트 5 〉	통과 (0.05ms, 10.1MB)
테스트 6 〉	통과 (2.14ms, 10.5MB)
테스트 7 〉	통과 (6.13ms, 11.6MB)
테스트 8 〉	통과 (16.26ms, 13.4MB)
테스트 9 〉	통과 (487.00ms, 46.4MB)
테스트 10 〉	통과 (583.03ms, 46.2MB)
테스트 11 〉	통과 (1956.86ms, 83.5MB)
테스트 12 〉	통과 (0.33ms, 10.4MB)
테스트 13 〉	통과 (0.31ms, 10.3MB)
테스트 14 〉	통과 (345.05ms, 46.8MB)
테스트 15 〉	통과 (822.43ms, 83.7MB)
테스트 16 〉	통과 (0.22ms, 10.2MB)
테스트 17 〉	통과 (0.32ms, 10.2MB)
테스트 18 〉	통과 (0.53ms, 10.4MB)
테스트 19 〉	통과 (0.83ms, 10.3MB)
테스트 20 〉	통과 (171.78ms, 47MB)
테스트 21 〉	통과 (748.58ms, 82.8MB)
테스트 22 〉	통과 (0.01ms, 10.3MB)
테스트 23 〉	통과 (0.01ms, 10MB)
테스트 24 〉	통과 (0.01ms, 10.1MB)

다른 사람 풀이 보고 중복제거로 not in 말고 set을 쓸걸 싶었다
그래서 set(report)로 수정한 다음 시간 체크해봤음 궁금해서..
'''

# 수정된 코드
def solution(id_list, report, k):

    report = [i.split() for i in set(report)]  # muzi frodo -> [muzi, frodo]
    rpt = {i:[] for i in id_list}              # ['muzi':[]]
    for x, y in report:
        rpt[y].append(x)                       # {'muzi': ['apeach'], 'frodo': ['muzi', 'apeach'], 'apeach': [], 'neo': ['frodo', 'muzi']}
    
    mail = {i:0 for i in id_list}
    for key, val in rpt.items():          # 신고 유저 수가 k 이상 -> 해당 유저 메일 카운트 + 1
        if len(val) >= k:
            for v in val:
                mail[v] += 1
    
    return list(mail.values())             # mail의 values만 리스트로 반환

'''
테스트 1 〉	통과 (0.01ms, 10.1MB)
테스트 2 〉	통과 (0.03ms, 10.3MB)
테스트 3 〉	통과 (293.64ms, 85.1MB)
테스트 4 〉	통과 (0.03ms, 10.4MB)
테스트 5 〉	통과 (0.04ms, 9.98MB)
테스트 6 〉	통과 (0.95ms, 10.4MB)
테스트 7 〉	통과 (1.58ms, 10.9MB)
테스트 8 〉	통과 (2.06ms, 11.6MB)
테스트 9 〉	통과 (134.09ms, 44.7MB)
테스트 10 〉	통과 (114.80ms, 44.2MB)
테스트 11 〉	통과 (317.21ms, 85.3MB)
테스트 12 〉	통과 (0.36ms, 10.3MB)
테스트 13 〉	통과 (0.20ms, 10.1MB)
테스트 14 〉	통과 (73.61ms, 37.4MB)
테스트 15 〉	통과 (122.43ms, 54.8MB)
테스트 16 〉	통과 (0.21ms, 10.2MB)
테스트 17 〉	통과 (0.21ms, 10.4MB)
테스트 18 〉	통과 (0.54ms, 10.1MB)
테스트 19 〉	통과 (0.62ms, 10.5MB)
테스트 20 〉	통과 (80.22ms, 37.4MB)
테스트 21 〉	통과 (181.26ms, 54.9MB)
테스트 22 〉	통과 (0.01ms, 10.1MB)
테스트 23 〉	통과 (0.01ms, 10MB)
테스트 24 〉	통과 (0.01ms, 10MB)

시간이 많이 단축된 것을 볼 수 있었당 
set 쓰고 not in을 빼서 그런듯... 
'''