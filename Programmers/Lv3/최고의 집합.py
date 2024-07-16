def solution(n, s):
    a, b = divmod(s, n)
    
    if a < 1:
        return [-1]
    
    answer = [a] * n
    
    for i in range(n-1, n-b-1, -1):
        answer[i] += 1
    
    return sorted(answer)
