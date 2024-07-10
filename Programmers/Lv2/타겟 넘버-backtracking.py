
def solution(numbers, target):
    
    stack = []
    return dfs(numbers, target, stack, 0)

def dfs(numbers, target, stack, index):
    result = 0
    if len(stack) == len(numbers):
        if sum(stack) == target:
            return 1
        else:
            return 0
    
    stack.append(numbers[index])
    result += dfs(numbers, target, stack, index+1)
    stack.pop()
    
    stack.append(-numbers[index])
    result += dfs(numbers, target, stack, index+1)
    stack.pop()
    
    return result