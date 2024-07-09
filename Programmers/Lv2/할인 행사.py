def solution(want, number, discount):
    answer = 0
    dict = {}
    for i, element in enumerate(want):
        dict[element] = number[i]
    
    for i in range(len(discount)):
        if dict.get(discount[i]) is not None:
            dict[discount[i]] -= 1
        if i >= 10 and dict.get(discount[i-10]) is not None:
            dict[discount[i-10]] += 1
        
        answer += isResult(want, dict)

    return answer

def isResult(want, dict):
    for element in want:
        if dict[element] != 0:
            return 0
    return 1