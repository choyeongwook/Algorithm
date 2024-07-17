
def solution(m, n, puddles):
    maps = [[0] * m for _ in range(n)]
    maps[0][0] = 1
    
    for pud in puddles:
        if pud:
            maps[pud[1]-1][pud[0]-1] = -1
    
    for i in range(n):
        for j in range(m):
            if maps[i][j] == -1:
                continue
            if i > 0 and maps[i-1][j] != -1:
                maps[i][j] += maps[i-1][j] % 1000000007
            if j > 0 and maps[i][j-1] != -1:
                maps[i][j] += maps[i][j-1] % 1000000007
    
    # print(maps)
    return maps[n-1][m-1] % 1000000007
