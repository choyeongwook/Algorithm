from collections import deque

def solution(begin, target, words):
    words = [begin] + words
    words_length = len(words)
    graph = [[] for _ in range(words_length)]
    
    for i in range(words_length-1):
        for j in range(i+1, words_length):
            if is_one_char_diff(words[i], words[j]):
                graph[i].append(j)
                graph[j].append(i)
    
    visited = [False] * words_length

    return bfs(graph, visited, 0, target, words)

# 그래프화 시켜서 bfs
def bfs(graph, visited, start, target, words):
    queue = deque([(start, 0)])
    visited[start] = True
    
    while queue:
        current, count = queue.popleft()
        if words[current] == target:
            return count
        
        for next in graph[current]:
            if not visited[next]:
                visited[next] = True
                queue.append((next, count+1))
    return 0

def is_one_char_diff(word1, word2):
    diff_count = 0
    for i in range(len(word1)):
        if word1[i] != word2[i]:
            diff_count += 1
            if diff_count > 1:
                return False
    
    if diff_count == 1:
        return True
    else:
        return False