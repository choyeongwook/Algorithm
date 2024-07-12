def solution(triangle):
    d = []
    for i in range(len(triangle)):
        d.append([0] * (i+1))

    d[0][0] = triangle[0][0]
    
    for i in range(1, len(triangle)):
        for j in range(i+1):
            if j == 0:
                d[i][j] = d[i-1][j] + triangle[i][j]
            elif j == i:
                d[i][j] = d[i-1][j-1] + triangle[i][j]
            else:
                d[i][j] = max(d[i-1][j-1], d[i-1][j]) + triangle[i][j]
    
    return max(d[len(triangle)-1])