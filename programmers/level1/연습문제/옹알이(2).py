# 내 풀이
def solution(babbling):
    result = []
    
    for b in babbling:
        for i, x in enumerate(['aya', 'ye', 'woo', 'ma']): 
            if not x*2 in b:                   # 연속 발음 아니면 해당 발음을 인덱스(0, 1, 2 ,3)로 변경
                b = b.replace(x, str(i))
        if b.isdigit():                        # 전부 숫자면 append ( ex. 1e -> 추가x / 12 -> 추가ㅇㅇ)
            result.append(b)
    
    return len(result)

'''
정규식으로 해보려고 한시간동안 삽질했지만 실패했음
다른 방식으로 구현 replace와 isdigit 활용

발음이 4개 밖에 없어서 간단했당
'''

# 다른 사람 풀이
def solution2(babbling):
    answer = 0
    for i in babbling:
        for j in ['aya','ye','woo','ma']:
            if j*2 not in i:
                i=i.replace(j,' ')         # 공백으로 변경
        if len(i.strip())==0:              # strip해서 안 나눠지면 전체 공백이니까 ans 1 추가
            answer +=1