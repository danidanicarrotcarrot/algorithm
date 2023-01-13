# 내 풀이 1
def binary_(n, arr):
    return [str(format(arr[i],'b')).rjust(n, '0') for i in range(n)]
        
def solution_(n, arr1, arr2):
    arr1, arr2 = binary(n, arr1), binary(n, arr2)
    print(zip(arr1, arr2))
    nums = []
    for i in range(n):
        s = ''
        for j in range(n):
            s += str(int(arr1[i][j])+int(arr2[i][j]))
        nums.append(s)
        
    res = []
    for i in nums:
        s = ''
        for j in i:
            if j == '0':
                s += ' '
            else:
                s += '#'
        res.append(s)
    return res

'''
헤엑 옛날에 풀었던거 도대체 왜 저렇게 했을까
'''

# 내 풀이 2

def binary(n, arr):
    return [str(format(arr[i],'b')) for i in range(n)]       # 2진수 변환한 리스트 반환하는 함수
        
def solution(n, arr1, arr2):
    arr1, arr2 = binary(n, arr1), binary(n, arr2)            
    map = [str(int(x)+int(y)) for x, y in zip(arr1, arr2)]   # 각각 수 더해서 리스트로
    res = []                                                 # ex) 1101 + 0011 -> 1112
    for i in map:
        i = i.replace('0', ' ')       # 0빼고는 다 #으로 바꿔주고
        i = i.replace('1', '#')
        i = i.replace('2', '#')
        res.append(i.rjust(n, ' '))   # n길이에 맞춰서 오른쪽정렬, 빈 공간은 공백으로 
    return res

'''
길이 맞추는거 rjust쓰면 된당 ~
뭔가 더 효율적으로 해보고 싶었으나 흠.. 할 게 많아서 ㅠㅡㅠㅠㅠ흑
'''

# 다른 사람 풀이
def solution2(n, arr1, arr2):
    answer = []
    for i,j in zip(arr1,arr2):
        a12 = str(bin(i|j)[2:])
        a12=a12.rjust(n,'0')
        a12=a12.replace('1','#')
        a12=a12.replace('0',' ')
        answer.append(a12)
    return answer

'''
bin(i|j) 는 i랑 j를 이진변환 하고 같은 자리에 모두 0이 오면 0, 
하나라도 1이 있으면 1로 출력한다고 함
wow
'''