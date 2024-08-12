from collections import deque

def solution(queue1, queue2):
    q1 = deque(queue1)
    q2 = deque(queue2)
    
    sum1 = sum(q1)
    sum2 = sum(q2)
    length = len(q1)
    
    count = 0
    while sum1 != sum2:
        if sum1 > sum2:
            cur = q1.popleft()
            q2.append(cur)
            sum1 -= cur
            sum2 += cur
        else:
            cur = q2.popleft()
            q1.append(cur)
            sum2 -= cur
            sum1 += cur
        
        count += 1
        
        if count >= length*3:
            return -1
    
    
    return count