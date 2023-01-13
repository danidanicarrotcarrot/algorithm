# 풀이 40ms -> 답지참고

import sys
for i in sys.stdin:                   # 여러줄 입력 받을 때 사용, ^Z를 입력받으면 종료, 개행문자까지 입력됨
    temp = '-'
    for j in range(int(i)):
        temp = temp+' '*len(temp)+temp
    print(temp)

'''
맨 아래부터 시작해서 점차 위로 올라가는 방식
첨에 - - 입력되고 그다음 temp개수만큼 공백이 들어가고 뒤에 - -이 붙고
그 다음 temp만큼 공백 들어가고 앞뒤로 temp 들어감
처음에는 나눌려고만 했어서 어떻게 풀어야할지 막막했는데 답지보고 오,,,
딴 건 어케 풀지... 어렵다..
'''