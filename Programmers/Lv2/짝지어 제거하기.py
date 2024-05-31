def solution(s):
    stack = []
    
    for char in s:
        if len(stack) >= 1 and stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)
    
    if len(stack) == 0:
        return 1
    else:
        return 0