

def solution(s):
    s2 = s * 2
    
    answer = 0
    
    for i in range(len(s)):
        if isRightForm(s2[i:i+len(s)]):
            answer += 1
        
    return answer

def isRightForm(str):
    stack = []
    
    for char in str:
        if char == '(':
            stack.append('(')
        elif char == '{':
            stack.append('{')
        elif char == '[':
            stack.append('[')
        else:
            if len(stack) <= 0:
                return False
            if char == ')' and stack.pop() != '(':
                return False
            elif char == '}' and stack.pop() != '{':
                return False
            elif char == ']' and stack.pop() != '[':
                return False
    if len(stack) == 0:
        return True
    else:
        return False