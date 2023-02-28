# 내 풀이
def solution(clothes):
    closet = dict()
    
    for cn, ct in clothes:
        closet[ct] = closet.get(ct, 0) + 1  # get(key, 0) -> 딕셔너리 안에 찾으려는 Key가 없을 경우 0을 가져옴 
    
    ans = 1
    for v in closet.values():
        ans *= v+1
    
    return ans - 1

'''
이 문제는 각 옷을 종류별로 카운트한 후 + 1을 해서 다 곱해준 후 -1을 하면 된다
a:1, b:2, c:3 -> (1+1) * (2+1) * (3+1) - 1
공식 찾는게 어려워서 답지를 살짝 확인했다
그리고 딕셔너리를 활용해서 풀이.. 딕셔너리 쓸 때 get을 잘 이용하면 편리할 것 같다
'''