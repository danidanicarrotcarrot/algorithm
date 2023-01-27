# 내 풀이
def solution(k, m, score):
    score = sorted(score, reverse=True)                         # 내림차순으로 정렬
    score = [score[i:i+m] for i in range(0, len(score), m)]     # [[4, 4, 4], [4, 4, 4], [2, 2, 2], [2, 1, 1]]
		return sum([min(s)*m for s in score if len(s) == m])    # 사과개수가 m이랑 같은 것만 계산해서 담고 다 더해서 출력

# 다른 사람 풀이
solution = lambda _, m, s: sum(sorted(s)[-m::-m]) * m           # [1, 1, 2, 2, 2, 2, 4, 4, 4, 4, 4, 4]
																# [-m::-m] 슬라이싱하면 [4, 4, 2, 1]만 나옴 sum해서 m 곱해줌~

'''
정렬하고, 높은 점수부터 담아서 사과개수 모자란 상자만 빼고 계산해서 더해주면 된다
easy~

a[start:stop:step] 항목은 지정된 지점에서 시작하여 제공된 단계 크기로 stop -1까지 잘라줌
'''