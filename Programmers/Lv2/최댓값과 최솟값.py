def solution(s):
    array = list(map(int, s.split()))
    
    minimum = min(array)
    maximum = max(array)
    answer = f'{minimum} {maximum}'
    
    return answer