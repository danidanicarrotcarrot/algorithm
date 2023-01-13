# 괄호

for _ in range(int(input())):
    n = input()
    vps = []

    for i in n:
        if i == '(':
            vps.append(i)

        elif i == ')':
            if len(vps) != 0 and vps[-1] == '(':
                vps.pop()
            else:
                vps.append(')')
                break
    
    if len(vps) == 0:
        print('YES')
    else:
        print('NO')