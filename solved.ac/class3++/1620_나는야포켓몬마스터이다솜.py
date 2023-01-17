# 도감에 수록된 포켓몬 개수 N, 맞춰야 하는 문제의 개수 M
# 1 <= N, M <= 100,000 자연수
# 포켓몬 번호 1~N 에 해당하는 포켓몬 이름이 들어온다 (첫 글자만 대문자)
                                            # 일부는 마지막 문자만 대문자
# 2 <= 이름 길이 <= 20

# M개의 줄에 맞춰야하는 문제가 들어온다
# 이름 -> 번호 출력
# 번호 -> 이름 출력

# 첫번째 풀이 -> 시간초과
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

name = [0]*N
for i in range(N):
    name[i] = input().strip()

for _ in range(M):
    i = input().strip()
    if i.isdigit():
        print(name[int(i)-1])
    else:
        print((name.index(i))+1)

# 두번째 풀이 53752kb	240ms  -> 답지참고
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
key_num, key_name = {}, {}

for i in range(N):
    n = input().strip()
    key_num[i+1] = n
    key_name[n] = i+1

for _ in range(M):
    m = input().strip()
    if m.isdigit():
        print(key_num[int(m)])
    else:
        print(key_name[m])

'''
시간초과떠서 왜지 하고 이것저것 해보다가 답지 참고 후 list가 문제라는 것을 깨달았다
dictionary 2개 만들어서 해결 ~
시간초과 화난ㄷ
확실히 풀던 것들보다 어렵당 ㅠㅠ힝
'''