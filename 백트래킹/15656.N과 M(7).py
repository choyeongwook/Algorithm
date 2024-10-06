n, m = map(int, input().split())

array = list(map(int, input().split()))

array.sort()

stack = []
def dfs():
    if len(stack) == m:
        print(*stack)
        return
    
    for i in range(n):
        stack.append(array[i])
        dfs()
        stack.pop()

dfs()