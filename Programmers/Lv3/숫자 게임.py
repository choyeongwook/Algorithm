from bisect import bisect_right

def solution(A, B):
    B.sort()
    result = 0
    for element in A:
        index = bisect_right(B, element)
        
        if index < len(B):
            B.pop(index)
            result += 1
        else:
            B.pop(0)
        
    return result