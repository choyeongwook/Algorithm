def solution(n):
    if n==1:
        return 1
    elif n==2:
        return 2
    
    d = [0] * (n+1)
    
    d[1] = 1
    d[2] = 2
    
    # 이전 칸에서 그냥 한 칸 뛴거,
    # 2칸전에서 두칸 뛴 거
    for i in range(3, n+1):
        d[i] = (d[i-1] % 1234567 + d[i-2] % 1234567) % 1234567
    
    return d[n]