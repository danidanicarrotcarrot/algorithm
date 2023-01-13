# 단어 공부

word = input().upper() # 대문자로 입력받음
word_list = []
num_list = []

for i in range(len(word)): # 단어만큼 반복
    if word[i] not in word_list: 
        num = word.count(word[i])
        num_list.append(num)
        word_list.append(word[i])

max_num = max(num_list)

if num_list.count(max_num) > 1 : # 숫자가 여러개면 ? 출력
    print('?')
else :
    idx = num_list.index(max_num)
    print(word_list[idx])