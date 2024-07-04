
def solution(elements):
    elements = elements * 2
    
    result = set()
    
    for i in range(len(elements)//2):
        for j in range(len(elements)//2):
            # temp = 0
            # for j in range(k, k-(i+1), -1):
            #     temp += elements[j]
            result.add(sum(elements[i:i+j+1]))
    
    return len(result)