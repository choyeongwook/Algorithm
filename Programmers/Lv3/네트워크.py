def solution(n, computers):
    visited = [False] * n
    answer = 0
    for i in range(n):
        if not visited[i]:
            dfs(computers, i, visited)
            print()
            answer += 1
    
    return answer

def dfs(graph, current, visited):
    visited[current] = True
    
    for next in range(len(graph[current])):
        if not visited[next] and graph[current][next] == 1:
            visited[next] = True
            dfs(graph, next, visited)