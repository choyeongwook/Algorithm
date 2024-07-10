from collections import deque

def solution(priorities, location):
    sorted_array = sorted(priorities)
    
    queue = deque(priorities)
    
    result = 0
    while True:
        current = queue.popleft()
        
        # current가 현재 큐에서 가장 큰 proirity 이면
        if current == sorted_array[-1]:
            result += 1
            if location == 0:
                break
            else:
                sorted_array.pop()
                location -= 1
        else:
            queue.append(current)
            if location == 0:
                location = len(queue)-1
            else:
                location -= 1

    return result