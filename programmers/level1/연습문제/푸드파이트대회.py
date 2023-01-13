# 내 풀이
def solution(food):
    f = {i : food[i] for i in range(len(food))} # {음식 번호 : 음식 수} -> ex) {0: 1, 1: 7, 2: 1, 3: 2}
    
    ans = ''                                   
    for k, v in f.items():                      # 음식 수가 1보다 큰 것들의 key를 (value//2)만큼 곱해서 ans에 추가
        if int(v) > 1:                          # ex '1113'
            ans += (str(k) * (int(v)//2))
            
    return ans+'0'+ans[::-1]                    # 중간에는 물, 뒤에는 뒤집고 합쳐서 출력 '1113'+'0'+'3111'

# 다른 사람 풀이
def solution2(food):
    answer ="0"
    for i in range(len(food)-1, 0,-1):
        c = int(food[i]/2)
        while c>0:
            answer = str(i) + answer + str(i)
            c -= 1
    return answer

'''
대체로 비슷한 것 같다
나는 딕셔너리로 했다... ㅇ그냥 그렇게 하고 싶었다
딕셔너리도 컴프리헨션 된다고 했던거 봤어서 써보고 싶었나보다 ㅋㅋ
'''