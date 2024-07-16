def solution(order):
    stack = []
    current = 0
    result = 0
    
    expected = 0
    actual = 1
    while True:
        
        if actual > len(order) or expected > len(order):
            break
        # print('actual: ', actual)
        # print('expected: ', order[expected])
        # print(stack)
        if actual == order[expected]:
            # print("result 증가")
            result += 1
            expected += 1
            actual += 1
        else:
            stack.append(actual)
            actual += 1
            
        while stack and expected <= len(order)-1 and stack[-1] == order[expected]:
            # print("result 증가(스택)")
            result += 1
            expected += 1
            stack.pop()
            # print(stack)
        
        
    
    return result