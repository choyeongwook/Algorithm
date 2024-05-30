def solution(s):
    s_lower = s.lower()
    
    answer_stack = []
    answer_stack.append(s_lower[0].upper())
    
    is_after_blank = False
    for i in range(1, len(s)):
        if is_after_blank:
            answer_stack.append(s[i].upper())
        else:
            answer_stack.append(s_lower[i])
        
        if s_lower[i] == ' ':
            is_after_blank = True
        else:
            is_after_blank = False
    
    answer = "".join(answer_stack)

    return answer