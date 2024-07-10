def solution(numbers, target):
    
    dic = dict()
    
    dic[numbers[0]] = 1
    dic[-numbers[0]] = 1
    
    for num in numbers[1:]:
        print(f'num: {num}')
        temp_dic = dict()
        for key in dic:
            if temp_dic.get(key+num) is None:
                temp_dic[key+num] = 0
            temp_dic[key+num] += dic[key]
            if temp_dic.get(key-num) is None:
                temp_dic[key-num] = 0
            temp_dic[key-num] += dic[key]
            
        dic = temp_dic
        
    
    if dic.get(target) is None:
        dic[target] = 0
    return dic[target]