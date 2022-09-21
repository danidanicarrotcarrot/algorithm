# 부녀회장이 될테야

t = int(input())

for _ in range(t):
    k = int(input())
    n = int(input())
    klist = [[] for _ in range(k+1)]
    
    for i in range(n): 
        klist[0].append(i+1) # 0층 먼저 만들고
        
    for j in range(k):
        klist[j+1].append(1) # 각 층의 1호는 1명
        for l in range(n-1): 
            klist[j+1].append(klist[j+1][l]+klist[j][l+1])
            
    print(klist[k][n-1])
        
    