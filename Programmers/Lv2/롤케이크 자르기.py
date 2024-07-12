def solution(topping):
    dic_left, dic_right = {}, {}
    s = set()
    
    for t in topping:
        s.add(t)
        dic_left[t] = 0
        if dic_right.get(t) is None:
            dic_right[t] = 0
        dic_right[t] += 1
    
    left_count = 0
    right_count = len(s)
        
    result = 0
    for t in topping:
        if dic_left[t] == 0:
            left_count += 1
        if dic_right[t] == 1:
            right_count -= 1
            
        if left_count == right_count:
            result += 1
            
        dic_left[t] += 1
        dic_right[t] -= 1
    return result
