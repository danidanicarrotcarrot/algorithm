# 내 풀이

def solution(park, routes):
    x, y = 0, 0                         # 시작 지점 설정
    
    for i in range(len(park)):          # 'S'가 있으면 해당 좌표를 찾아서 x, y에 저장
        if 'S' in park[i]:
            x = i
            y = park[i].find('S')       # '문자열'.find('s') -> s가 있는 인덱스를 반환
            break
    
    for route in routes:                # 'E 2' -> s = E, n = 2로 저장
        r = route.split()
        s = r[0]
        n = int(r[1])
        
        if s == 'E':                    # E면 y좌표만 탐색 -> X 만나면 break
            for i in range(1, n+1):
                if y+n >= len(park) or park[x][y+i] == 'X':
                    break
            else:                       # break 안 걸리면 y좌표에 n 더해줌
                y += n
                
        if s == 'S':                    # S면 x좌표만 탐색 -> X 만나면 break
            for i in range(1, n+1):
                if x+n >= len(park) or park[x+i][y] == 'X':
                    break
            else:
                x += n                  # x 좌표에 n 더해줌
        
        if s == 'W':                    
            for i in range(1, n+1):
                if y-n < 0 or park[x][y-i] == 'X':
                    break
            else:
                y -= n                  # E와 마찬가지로 y좌표 탐색, n 빼줌
        
        if s == 'N':
            for i in range(1, n+1):
                if x-n < 0 or park[x-i][y] == 'X':
                    break
            else:
                x -= n                  # S와 마찬가지로 x좌표 탐색, n 빼줌
                
    return [x, y]                       # 최종 좌표 출력

'''
음 무식하게 푼 것 같당..
'''