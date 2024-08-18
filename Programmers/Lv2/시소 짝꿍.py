def solution(weights):
    array = [0] * 2002
    
    for w in weights:
        array[w] += 1
    
    result = 0
    
    weights.sort()
    
    for w in weights:
        if w % 2 == 0:
            result += array[w//2 * 3]
        if w % 3 == 0:
            result += array[w//3 * 4]
        result += array[w] - 1
        result += array[w*2]
        array[w] -= 1
    
    return result