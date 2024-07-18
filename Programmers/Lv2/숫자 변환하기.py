from collections import deque

def solution(x, y, n):
    if x == y:
        return 0
    visited = [False] * y
    queue = deque([(x, 0)])
    visited[x] = True
    while queue:
        current, count = queue.popleft()
        
        for i in range(1, 4):
            if i == 1:
                next = current+n
            else:
                next = current*i
            
            if next == y:
                return count+1
            elif next > y or visited[next]:
                continue
            visited[next] = True
            queue.append((next, count+1))

    return -1