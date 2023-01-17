# 내 풀이 49352	112ms
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

name = {}
for _ in range(N):
    name[input().strip()] = 1

for _ in range(M):
    m = input().strip()        # 딕셔너리에 'kwon':1 이런식으로 추가
    if m in name:              # 이미 있으면 값을 2로 변경
        name[m] = 2
    else:
        name[m] = 1

ans = []
for k, v in sorted(name.items()):    # 정렬 후 값이 2인것만 답에 추가
    if v == 2:
        ans.append(k)

print(len(ans))
for i in ans:
    print(i)

# 다른 풀이 (답지 참고) 43456	80ms
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

n = {input().strip() for i in range(N)}
m = {input().strip() for i in range(M)}

ans = sorted(n&m) # 교집합 연산
print(len(ans))

for i in ans:
    print(i)

'''
아까 이다솜 풀어서 그런가 딕셔너리에 꽂혀서 계속 저거로만 생각했당
걍 간단하게 set으로 풀면 되는데... 암튼.. 교집합 연산 신기했당
그리고 set이랑 dict에도 컴프리헨션 많이 적용해봐야게따
'''