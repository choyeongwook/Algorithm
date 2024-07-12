import sys
input = sys.stdin.readline

n = int(input())
numbers = list(map(int, input().split()))
operators = list(map(int, input().split()))

opers = []
# 0 0 1 2 3
for i in range(4):
    opers += [i] * operators[i]

visited = [False] * len(opers)
results = []
def dfs(depth, value, operator):
    if operator == 0:
        value += numbers[depth]
    elif operator == 1:
        value -= numbers[depth]
    elif operator == 2:
        value *= numbers[depth]
    elif operator == 3:
        value = int(value/numbers[depth])

    if depth == n-1:
        results.append(value)
        return
    
    for i in range(len(opers)):
        if not visited[i]:
            visited[i] = True
            dfs(depth+1, value, opers[i])
            visited[i] = False
    

dfs(0, numbers[0], -1)

# print(results)
print(max(results))
print(min(results))