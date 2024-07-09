import math
def solution(progresses, speeds):
    if len(progresses) <= 0:
        return [0]
    answer = []
    array = []
    
    for i in range(len(progresses)):
        array.append(math.ceil((100-progresses[i])/speeds[i]))
    # print(array)
    
    count = 0
    temp_value = array[0]
    for i in range(len(array)):
        if array[i] <= temp_value:
            count += 1
        else:
            answer.append(count)
            count = 1
            temp_value = array[i]
    answer.append(count)
    return answer
