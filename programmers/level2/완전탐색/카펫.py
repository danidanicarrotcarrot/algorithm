# brown, yellow = 8, 1
# res = []
# x = brown + yellow
# for i in range(1, x+1):
#     if x%i == 0:
#         res.append(i)

# ans = len(res)//2
# if len(res)%2 == 0:
#     print(res[ans], res[ans-1])
# else:
#     print(res[ans], res[ans])

def solution(brown, yellow):
    x = brown + yellow
    
    for i in range(3, int(x**0.5)+1):
        if not x%i and (i-2) * ((x//i)-2) == yellow:
            return [x//i, i]