# 내 풀이 44ms

s = input()
print(*sorted([s[i:] for i in range(len(s))]), sep='\n')

'''
슬라이싱 해서 정렬 후 출력
'''