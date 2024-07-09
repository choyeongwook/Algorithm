def solution(s):
    answer = []
    array = list(map(lambda x: list(map(int, x.split(','))), s.strip('{}').split('},{')))
    
    array.sort(key=lambda x: len(x))
    
    dic = dict()
    # [2,3]
    for arr in array:
        for element in arr:
            if dic.get(element) is None:
                answer.append(element)
                dic[element] = True
    
    return answer