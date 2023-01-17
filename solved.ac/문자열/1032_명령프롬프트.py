# 내 풀이

data = [input() for _ in range(int(input()))]

ans = list(data[0])           # 첫번째 파일만 따로 저장
for i in data[1:]:
    for j in range(len(i)):   # 그 다음 파일이랑 한글자씩 비교해서 다르면 '?'로 바꿔줌
        if ans[j] != i[j]:
            ans[j] = '?'

print(''.join(ans))           # 합쳐서 출력

'''
replace에 꽂혀서 그거로만 계속 하다가 틀렸다고 나와서 빡쳤었당
아무래도 replace는 같은 문자가 뒤에도 나오면 걔도 바뀌거나 아니면 바뀌는 횟수를 지정해줘야 돼서
이런 경우에는 적합하지 않은 듯
'''