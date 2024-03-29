# 내 풀이
def solution(s, skip, index):
    atoz = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    
    for i in skip:
        atoz.remove(i)
    
    ans = ''
    for i in s:
        ans += atoz[(atoz.index(i)+index)%len(atoz)]

    return ans

'''
테스트 1 〉	통과 (0.02ms, 10.2MB)
테스트 2 〉	통과 (0.01ms, 10MB)
테스트 3 〉	통과 (0.04ms, 10.1MB)
테스트 4 〉	통과 (0.01ms, 10.2MB)
테스트 5 〉	통과 (0.04ms, 10.1MB)
테스트 6 〉	통과 (0.03ms, 10.1MB)
테스트 7 〉	통과 (0.04ms, 10.2MB)
테스트 8 〉	통과 (0.02ms, 10MB)
테스트 9 〉	통과 (0.02ms, 10.1MB)
테스트 10 〉	통과 (0.02ms, 10.3MB)
테스트 11 〉	통과 (0.03ms, 10.2MB)
테스트 12 〉	통과 (0.04ms, 10.2MB)
테스트 13 〉	통과 (0.02ms, 10.2MB)
테스트 14 〉	통과 (0.01ms, 10.1MB)
테스트 15 〉	통과 (0.01ms, 10.2MB)
테스트 16 〉	통과 (0.01ms, 9.95MB)
테스트 17 〉	통과 (0.02ms, 10.2MB)
테스트 18 〉	통과 (0.03ms, 10.2MB)
테스트 19 〉	통과 (0.02ms, 10.1MB)

쉬웠당
'''