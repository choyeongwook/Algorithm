def solution(number, k):
    stack = []
    pop_count = 0
    for num_char in number:
        num = int(num_char)
        
        while stack and int(stack[-1]) < num and pop_count < k:
            stack.pop()
            pop_count += 1
        
        stack.append(num_char)
    
    return ''.join(stack[:len(stack)-k+pop_count])