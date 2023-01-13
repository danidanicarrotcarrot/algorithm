# 다현 풀이
for _ in range(int(input())):
    data = list(map(int, input().split()))     # 리스트로 하나씩 받아서 ex) 5 50 50 70 80 100
    avg = sum(data[1:])//data[0]               # [1:]로 사람 수 제외하고 점수만 sum 하고 사람수로 나눠줌 -> 평균
    ratio = 0
    for i in data[1:]:                         # data 다시 [1:]부터 돌면서 평균이랑 비교
        if i > avg :
            ratio += 1                         # i가 평균보다 클 때만 ratio 에 1 추가
    print('{:.3f}%'.format(ratio/data[0]*100)) # 비율 산출해서 출력 ~

'''
round(float, 3) + '%' 하니까 안 되길랭 {}.format 사용 !
소숫점 표현하는데도 여러가지 방식이 있던데 자기한테 익숙한걸로 하나 외워놓는게 좋을 것 같당 
ㅇㅅㅇ 문제는 비교적 쉬웠당
'''