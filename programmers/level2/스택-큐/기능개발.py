import math
def solution(progresses, speeds):
    
    done = []
    for p, s in zip(progresses, speeds):
        p = 100-p
        done.append(math.ceil(p/s))
    
    ans = []
    while done:
        max = done[0]
        cnt  = 0
        
        while done:
            if done[0] > max:
                break
        
            cnt += 1
            done.pop(0)
            
        ans.append(cnt)
        
    return ans