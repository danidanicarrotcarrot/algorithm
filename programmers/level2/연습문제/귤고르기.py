# 내 풀이

from collections import Counter

def solution(k, tangerine):
    tgr = Counter(tangerine).most_common() # most_common -> 값이 가장 많은 순으로 정렬됨
    i = 0                                  # [[3,2],[2,2],[5,2],[1,1],[4,1]]
    
    while k > 0:    
        k -= tgr[i][1]       # k에서 값을 빼주다가 0보다 작아지면 break
        i += 1        
        
    return i

'''
counter의 most_common을 활용해서 풀이
'''