def solution(n,a,b):
    result = 0
    temp_n = n
    while temp_n != 1:
        temp_n //= 2
        result += 1
    
    
    while True:
        n //= 2
        if (a <= n and b > n) or (a > n and b <= n):
            return result
        else:
            result -= 1
            if a > n:
                a -= n
                b -= n 