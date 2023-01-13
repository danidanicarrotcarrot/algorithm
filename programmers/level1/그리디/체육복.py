# 내 풀이
def solution(n, lost, reserve):
    student = {i+1:1 for i in range(n)}  # {학생번호:1(체육복 수)} 로 초기화
    
    for r in reserve:                    # 여벌 있으면 +1
        student[r] += 1                  
    for l in lost:                       # 잃어버렸으면 -1
        student[l] -= 1                  # ex) {"1":1,"2":0,"3":2,"4":0,"5":1}
    
    for k, v in student.items():
        if v == 1 or v == 2:             # 체육복이 1개거나 2개면 패스
            continue
            
        elif v == 0 and k == 1 and student[k+1] == 2:  # 체육복이 없고 첫번째 번호 + 뒷사람이 2개면
            student[k+1], student[k] = 1, 1            # 해당학생, 뒷 학생 각각 1로 업뎃
        
        elif v == 0 and k == n and student[k-1] == 2:  # 체육복이 없고 마지막 번호 + 앞사람이 2개
            student[k-1], student[k] = 1, 1            # 해당학생, 앞 학생 각각 1로 업뎃
        
        elif v == 0 and  n > k > 1:                # 그 외에 체육복이 없으면    
            if student[k-1] == 2:                  # 앞사람이 2개거나 뒷사람이 2개인지 체크 
                student[k-1], student[k] = 1, 1    # 각각 1개로 업뎃
            elif student[k+1] == 2:               
                student[k+1], student[k] = 1, 1
    
    return len([1 for i in student.values() if i not in {0}])  # 값이 0이 아닌애들만 모아서 출력

'''
시키는대로.. 구현...했는데.. 
처음에 계속 마지막 학생이 체육복이 없는 경우를 체크를 안 해줬어서 80점이 떴다
1시간 걸렸네 휴..................
마지막에 테스트 케이스 3 1 추가해보고서야 아... 하고 수정수정..
딕셔너리에 꽂혀있는거 같긴 한데.. 하.. 다른사람들은 쉽게 풀었넹.. ㅠㅠ눈물
'''

# 다른 사람 풀이
def solution2(n, lost, reserve):
    _reserve = [r for r in reserve if r not in lost]
    _lost = [l for l in lost if l not in reserve]
    for r in _reserve:
        f = r - 1
        b = r + 1
        if f in _lost:
            _lost.remove(f)
        elif b in _lost:
            _lost.remove(b)
    return n - len(_lost)