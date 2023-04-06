# 내 풀이

def solution(wallpaper):
    
    res_x, res_y = [], []
    
    for x in range(len(wallpaper)):
        for y in range(len(wallpaper[0])):
            if wallpaper[x][y] == '#':        # 순회하면서 #이 나오면 x, y 각각 append
                res_x.append(x)
                res_y.append(y)
    
    return [min(res_x), min(res_y), max(res_x)+1, max(res_y)+1]

'''
거창한 문제설명 때문에 어려우려나 했는데 생각보다 쉬웠던 문제
x, y 따로 저장해서 보니까 규칙이 보였당
'''