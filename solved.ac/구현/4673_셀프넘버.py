# 다현쓰 풀이 (76ms)

n = [0] * 10001                   # 10000개 짜리 리스트 생성

for i in range(len(n)):           # 리스트 n 길이만큼 for문 돌면서
    num = i+sum(map(int, str(i))) # 양의 정수 i + i 각 자릿수의 합 = d(n)
    if num < 10001:               # d(n)이 10000 보다 작을때만
        n[num] = 1                # 리스트 n의 자리를 1로 바꿔줌 = 셀프 넘버 아닌 수

for i in range(1, 10001):         # for문 만들어주고       
    if n[i] == 0:                 # 리스트에서 0인 값만, 즉 셀프 넘버만
        print(i)                  # 출력해주세용

---------------------------------------------------------------------------

# 다른 사람 풀이

numbers = set(range(1, 10000))
remove_set = set()                # d(n)결과 set
for num in numbers :              # set에서 하나씩 가져와서
    for n in str(num):            # num을 문자열로 변환해서 하나씩 가져온다음
        num += int(n)             # int로 변환해서 num에 ㄷㅓ해줌
    remove_set.add(num)           # add로 d(n) 추가

self_numbers = numbers - remove_set    # set의 '-' 연산자로 차집합을 구함
for self_num in sorted(self_numbers):  # sorted 함수로 정렬
    print(self_num)

'''
뭔가 난 왜 이렇게 풀었나 싶긴한데 
답 나왔으니 됐다.. 사실 될 줄 몰랐는데 갑자기 와라락 하고 출력돼서 오 이게 되네 하고 제출
set 자료형을 쓴 답이 많던데,, 이렇게 하는거구나 ㅎ
음 어려워보였는데 생각보다 금방 풀어서 기분 좋았다 
다음에 비슷한 문제 나오면 set을 떠올려야겠음
'''