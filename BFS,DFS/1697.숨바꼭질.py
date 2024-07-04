from collections import deque
n, k = map(int, input().split())

queue = deque()
queue.append((n, 0))

visited = [False] * 200002
visited[n] = True

while queue:
    current, time = queue.popleft()
    visited[current] = True
    
    if current == k:
        print(time)
        break
    
    # 가 본 곳이면 패스
    
    if current < k:
        if not visited[current*2]:
            queue.append((current*2, time+1))
        if not visited[current+1]:
            queue.append((current+1, time+1))
    if current > 0 and not visited[current-1]:
        queue.append((current-1, time+1))
    