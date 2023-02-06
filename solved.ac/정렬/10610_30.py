# 내 풀이 104ms
n = ''.join(sorted(list(input()), reverse=True))
print(n) if not int(n) % 30 else print(-1)

'''
내림차순으로 정렬
30으로 나누어 떨어지면 해당 수 출력
아니면 -1 출력
'''