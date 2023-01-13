# 내 풀이
def solution(s):
    res = []
    
    for i in range(len(s)):        # s 길이만큼
        
        if s[i] not in s[:i]:      # 처음 나오는 글자면 -1 추가
            res.append(-1)
        
        else :                      # 나왔던 거면 
            cnt = 0
            for j in s[:i][::-1]:   # 반대로 돌리면서
                cnt += 1            # 개수 카운트
                if j == s[i] :      # 같은 알파벳 만나면 스탑
                    res.append(cnt)
                    break
    
    return res

# 다른 사람 풀이
def solution(s):
    answer = []
    dic = dict()                          # {'a':개수}
    for i in range(len(s)):
        if s[i] not in dic:               # 딕셔너리에 들어있지 않으면
            answer.append(-1)             # -1 추가
        else:                             # 들어있으면 i에서 해당 문자 개수 빼서 ans에 추가
            answer.append(i - dic[s[i]])
        dic[s[i]] = i                     # 있던 알파벳 만날때마다 인덱스로 업데이트

    return answer

'''
나는 문자열 슬라이싱을 이용했다 슬라이싱은 인덱스 설정 잘못하면 안 돌아가서 화남
다른 풀이는 딕셔너리를 이용한 풀이 ,, 좋은 듯
'''