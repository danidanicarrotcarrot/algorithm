# 내 풀이

def solution(phone_book):
    nums = {i:0 for i in phone_book}
    for n in nums:
        for i in range(len(n)):
            if n[:i] in nums:
                return False
    return True

'''
모든 원소를 dic안에 key값으로 넣고 value는 필요없어서 0으로 통일 
만약에 n이 1195524421이면 1, 11, 119, 1195 이런식으로 가다가
해당 값이 딕셔너리에 있으면 false 리턴
'''