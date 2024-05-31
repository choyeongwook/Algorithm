def solution(s):
    
    stack = []
    
    for char in s:
        open = char == "("
        
        # 스택이 비어있을 때 닫으면 false
        if len(stack) == 0 and not open:
            return False
        
        if open:
            stack.append("(")
        else:
            if stack.pop() != "(":
                return False
        
    if len(stack) != 0:
        return False

    answer = True

    return True