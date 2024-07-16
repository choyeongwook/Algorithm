from copy import deepcopy

def solution(land):
    d = deepcopy(land[0])
    
    for i in range(1, len(land)):
        temp_d = [0,0,0,0]
        
        for j in range(4):
            temp_d[j] = land[i][j] + max(d[j-1], d[j-2], d[j-3])
        
        d = deepcopy(temp_d)
    
    print(d)
    return max(d)