# 내 풀이

from itertools import permutations

def solution(k, dungeons):
    ans = 0

    for permutation in permutations(dungeons, len(dungeons)):
        hp = k
        cnt = 0

        for p in permutation:
            if hp >= p[0]:       # 현재 남은 피가 최소필요피로도보다 많거나 같으면
                hp -= p[1]       # 피 깎고 카운트 + 1
                cnt += 1

        if cnt > ans:
            ans = cnt

    return ans

'''
던전 길이가 최대 8이라서 순열로 풀었당
모든 순열을 다 탐색해서 해당 순열에서 탐험 가능한 던전 수를 ans에 넣어줌
최대값을 리턴

테스트 1 〉	통과 (0.01ms, 10.3MB)
테스트 2 〉	통과 (0.01ms, 10MB)
테스트 3 〉	통과 (0.07ms, 10.1MB)
테스트 4 〉	통과 (0.07ms, 10MB)
테스트 5 〉	통과 (0.86ms, 10.1MB)
테스트 6 〉	통과 (5.22ms, 10.1MB)
테스트 7 〉	통과 (38.55ms, 9.98MB)
테스트 8 〉	통과 (49.10ms, 10.2MB)
테스트 9 〉	통과 (0.10ms, 10.4MB)
테스트 10 〉	통과 (3.04ms, 10.1MB)
테스트 11 〉	통과 (0.01ms, 10MB)
테스트 12 〉	통과 (32.62ms, 10.2MB)
테스트 13 〉	통과 (24.56ms, 10.2MB)
테스트 14 〉	통과 (31.67ms, 10.1MB)
테스트 15 〉	통과 (20.83ms, 10.3MB)
테스트 16 〉	통과 (2.39ms, 10.2MB)
테스트 17 〉	통과 (21.23ms, 10.2MB)
테스트 18 〉	통과 (0.02ms, 10.2MB)
테스트 19 〉	통과 (0.06ms, 10MB)
'''