from collections import deque

def solution(bridge_length, weight, truck_weights):
    queue = deque()
    all_weights = sum(truck_weights)
    current_sum = 0
    answer = 0
    index = 0
    current_weight = 0
    queue_length = 0
    while current_sum != all_weights:
        if queue_length >= bridge_length:
            qpop = queue.popleft()
            current_sum += qpop
            current_weight -= qpop
        
        if index < len(truck_weights) and weight-current_weight >= truck_weights[index]:
            queue.append(truck_weights[index])
            current_weight += truck_weights[index]
            index += 1
        else:
            queue.append(0)
        queue_length += 1
            
        answer += 1
    
    return answer