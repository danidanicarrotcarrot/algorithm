# 내 풀이 (36ms)

N = int(input())                

ans = []
for i in range(1, N+1):                        
    if len(str(i)) == 1 or len(str(i)) == 2:    # 한자리수, 두자리수는 모조리 append
        ans.append(i)
    else:                                       # 세자리수부터
        n = list(map(int, str(i)))              # 123 -> [1, 2, 3]
        for i in range(1, len(n)):            
            if n[i-1]-n[i] != n[0]-n[1] :       # 등차수열이 아니면 break
                break
        else:                                   # for문에서 걸리지 않으면 append
            ans.append(n)
print(len(ans))

'''
range(1, len(n)) 이거를 안하고 range(len(n[1:])) 이렇게 했더니 계속
잘못 나와서 하나하나 출력해보면서 답을 찾았다 ㅠㅡㅠㅠ
힘들었다..
'''