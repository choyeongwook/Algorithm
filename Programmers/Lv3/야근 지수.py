def solution(n, works):
    array = [0] * 50001
    
    for work in works:
        array[work] += 1
    
    for i in range(50000, 0, -1):
        if array[i] > 0:
            minimal = min(array[i], n)
            array[i] -= minimal
            n -= minimal
            array[i-1] += minimal
            
            if n == 0:
                print(array[:i+1])
                result = 0
                for i in range(1, i+1):
                    if array[i] > 0:
                        result += (i**2) * array[i]
                return result
    
    
    
    return 0