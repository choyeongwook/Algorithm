def solution(prices):
    stack = []
    answer = [i for i in range(len(prices)-1, -1, -1)]
    
    for i in range(len(prices)):
        while stack and prices[stack[-1]] > prices[i]:
            prev_index = stack.pop()
            answer[prev_index] = i-prev_index
            
        stack.append(i)
        
    return answer