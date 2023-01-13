def solution(arr):
    ans = []
    for i in arr:
        print(i)
        if len(ans) != 0 and ans[-1] == i:
            continue
        else:
            ans.append(i)
    return ans
    
arr = [1,1,3,3,0,1,1]
solution(arr)