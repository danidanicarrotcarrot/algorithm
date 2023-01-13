# 내 풀이 (36ms)

n = int(input())

A = sorted(list(map(int, input().split())), reverse=True)  # 내림차순으로 정렬
B = sorted(list(map(int, input().split())))                # 오름차순으로 정렬

ans = 0

for x, y in zip(A, B):     # A, B 묶어서 차례대로 가져와서 곱한 다음 ans에 추가
    ans += x*y

print(ans)

'''
배열을 움직이지 말래서 음.. 근데 움직여도 답 출력하는거랑은 상관 없길래 걍 그렇게 했다
비교적 쉬웠당
'''