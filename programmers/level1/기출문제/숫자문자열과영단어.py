# 내 풀이
def solution(s):
    nums = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    for idx, num in enumerate(nums):
        s = s.replace(num, str(idx))      
    return int(s)

# 다른 사람 풀이
num_dic = {"zero":"0", "one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}

def solution(s):
    answer = s
    for key, value in num_dic.items():
        answer = answer.replace(key, value)
    return int(answer)

'''
딕셔너리 key, value로 푸는 방법도 알아두면 좋을 것 같다
'''