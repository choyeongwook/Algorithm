def solution(n):
    d = [0] * (n+1)
    
    d[0] = 1
    d[1] = 1
    
    for i in range(2, n+1):
        d[i] = d[i-1] % 1000000007 + d[i-2] % 1000000007
    
    return d[n] % 1000000007