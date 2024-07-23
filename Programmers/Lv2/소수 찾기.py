def solution(numbers):
    result = set()
    stack = []
    visited = [False] * len(numbers)
    permu(numbers, result, stack, visited)
    
    # print(result)
    
    answer = 0
    for num in result:
        if num <= 1:
            continue
        isPrimary = True
        for i in range(2, int(num**0.5)+1):
            if num % i == 0:
                isPrimary = False
                break
        if isPrimary:
            # print(num)
            answer += 1
        
    
    return answer

def permu(number, result, stack, visited):
    if stack:
        result.add(int(''.join(stack)))
    
    if len(stack) == len(number):
        return
    
    for i in range(len(number)):
        if not visited[i]:
            visited[i] = True
            stack.append(number[i])
            permu(number, result, stack, visited)
            visited[i] = False
            stack.pop()