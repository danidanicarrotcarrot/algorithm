# 내 풀이
from collections import deque

def solution(cacheSize, cities):
    cache  = deque(maxlen=cacheSize)     # maxlen으로 deque 최대 길이를 캐시크기로 설정
    hit, miss = 0, 0                     # hit : 참조할 도시 이름이 캐시에 존재 / miss : 캐시에 존재하지 않음
    
    for city in cities:
        city = city.lower()         # 도시 이름 소문자로 변경
        
        if city in cache:           # 도시 이름이 캐시에 있으면 해당 도시 삭제, hit 카운트
            cache.remove(city)
            hit += 1
        else:                       # 캐시에 없으면 miss 카운트
            miss += 1
        cache.appendleft(city)      # 현재 도시 캐시 맨 앞에 추가
    
    return hit + miss*5             # hit 실행시간 : 1 / miss 실행시간 : 5

'''
문제를 읽고 먼저 LRU 알고리즘에 대해 찾아봤다

	LRU 란?
	LRU(Least Recently Used)는 가장 오랫동안 참조되지 않은 페이지를 교체하는 방식
	
	LRU 의 원리
	페이지를 새로 참조할 때마다 해당 페이지번호를 맨 앞에 추가
	-> 맨 뒤에 있는 페이지번호가 가장 오랫동안 참조되지 않은 페이지번호가 된다
	정해진 캐시 크기를 초과하게 되면 맨 뒤 페이지 번호를 제거함
	
	hit -> 해당 페이지번호가 이미 캐시에 존재하는 경우/해당 노드를 맨 앞으로 가져옴
	miss -> 해당 페이지번호가 캐시에 존재하지 않는 경우/맨 앞에 페이지번호 추가

deque를 사용해야겠다고 생각했고, maxlen으로 최대길이를 캐시사이즈로 설정했음
문제에서 말하는 알고리즘에 대한 이해가 있으면 쉬웠던 문제인 것 같고
모르는 채로 만나면 멘붕올 것 같다..

테스트 1 〉	통과 (0.01ms, 10.2MB)
테스트 2 〉	통과 (0.01ms, 10.2MB)
테스트 3 〉	통과 (0.01ms, 10.2MB)
테스트 4 〉	통과 (0.01ms, 10.4MB)
테스트 5 〉	통과 (0.01ms, 10.2MB)
테스트 6 〉	통과 (0.01ms, 10.3MB)
테스트 7 〉	통과 (0.01ms, 10.2MB)
테스트 8 〉	통과 (0.01ms, 10.2MB)
테스트 9 〉	통과 (0.01ms, 10.2MB)
테스트 10 〉	통과 (0.04ms, 10.2MB)
테스트 11 〉	통과 (59.19ms, 17.5MB)
테스트 12 〉	통과 (0.04ms, 10.2MB)
테스트 13 〉	통과 (0.04ms, 10.3MB)
테스트 14 〉	통과 (0.06ms, 10.4MB)
테스트 15 〉	통과 (0.14ms, 10.2MB)
테스트 16 〉	통과 (0.16ms, 10.1MB)
테스트 17 〉	통과 (0.25ms, 10.3MB)
테스트 18 〉	통과 (0.29ms, 10.2MB)
테스트 19 〉	통과 (0.45ms, 10.2MB)
테스트 20 〉	통과 (0.59ms, 10.2MB)
'''