# 내 풀이

def solution(arr1, arr2):
    ans = [[0] * len(arr2[0]) for _ in range(len(arr1))]
    
    for i in range(len(arr1)):
        for j in range(len(arr2[0])):
            for z in range(len(arr1[0])):
                ans[i][j] += arr1[i][z] * arr2[z][j]
    return ans

'''
append를 하는 걸로 하니까 자꾸 런타임에러가 나서 정답행렬을 미리 만든 후 넣어줌

테스트 1 〉	통과 (3.90ms, 10.2MB)
테스트 2 〉	통과 (79.55ms, 10.9MB)
테스트 3 〉	통과 (108.09ms, 10.9MB)
테스트 4 〉	통과 (1.83ms, 10MB)
테스트 5 〉	통과 (60.35ms, 10.8MB)
테스트 6 〉	통과 (34.14ms, 10.7MB)
테스트 7 〉	통과 (1.62ms, 10.1MB)
테스트 8 〉	통과 (0.66ms, 10.2MB)
테스트 9 〉	통과 (0.51ms, 10.2MB)
테스트 10 〉	통과 (58.29ms, 10.6MB)
테스트 11 〉	통과 (5.24ms, 10.3MB)
테스트 12 〉	통과 (1.38ms, 10.3MB)
테스트 13 〉	통과 (46.08ms, 10.8MB)
테스트 14 〉	통과 (88.10ms, 10.6MB)
테스트 15 〉	통과 (29.84ms, 10.5MB)
테스트 16 〉	통과 (8.17ms, 10.5MB)
'''