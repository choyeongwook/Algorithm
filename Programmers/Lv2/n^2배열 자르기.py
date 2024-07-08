def solution(n, left, right):
    array = []
    start_line = left // n
    end_line = right // n
    
    start_index = left % n
    end_index = right % n
    
    for i in range(start_line, end_line+1):
        for j in range(n):
            if i == start_line and j < start_index:
                continue
            if i == end_line and j > end_index:
                continue
            
            if i < j:
                array.append(j+1)
            else:
                array.append(i+1)
    return(array)

# 1234 1
# 2234 2
# 3334 3
# 4444 4