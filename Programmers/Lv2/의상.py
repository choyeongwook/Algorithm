def solution(clothes):
    index_dic = {}
    array = []
    for cloth in clothes:
        if index_dic.get(cloth[1]) is None:
            array.append(1)
            index_dic[cloth[1]] = len(array)-1
        else:
            array[index_dic[cloth[1]]] += 1
    
    answer = 1
    for n in array:
        answer *= n+1
    answer -= 1
    
    return answer