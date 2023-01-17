# 단어 정렬

words = [input() for _ in range(int(input()))] # 단어 받아서 리스트로

words.sort() # 알파벳순으로 정렬

dicts = {}
for i in words:
    dicts[i] = len(i)

d = sorted(dicts.items(), key=lambda x: x[1]) # 길이순으로 정렬

for i in d:
    print(i[0])