import bisect
from collections import deque

def solution(operations):
    array = deque()
             
    for operation in operations:
        operator, num = operation.split()
        
        if operator == 'I':
            array.insert(bisect.bisect_left(array, int(num)), int(num))
        else:
            if len(array) == 0:
                continue
            if num == '1': # 최댓값 삭제
                array.pop()
            elif num == '-1': # 최솟값 삭제
                array.popleft()
    
    print(array)
    
    if len(array) == 0:
        return [0, 0]
    else:
        return [array[-1], array[0]]