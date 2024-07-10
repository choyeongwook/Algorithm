def solution(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    s1 = set()
    s2 = set()
    
    dic1 = dict()
    dic2 = dict()
    
    
    for i in range(len(str1)-1):
        if ord(str1[i]) < 97 or ord(str1[i]) > 122:
            continue
        if ord(str1[i+1]) < 97 or ord(str1[i+1]) > 122:
            continue
        element = str1[i]+str1[i+1]
        if dic1.get(element):
            dic1[element] += 1
        else:
            dic1[element] = 1
        
    print(dic1)
    for i in range(len(str2)-1):
        if ord(str2[i]) < 97 or ord(str2[i]) > 122:
            continue
        if ord(str2[i+1]) < 97 or ord(str2[i+1]) > 122:
            continue
        element = str2[i]+str2[i+1]
        if dic2.get(element):
            dic2[element] += 1
        else:
            dic2[element] = 1
    print(dic2)
    
    gyo = 0
    hap = 0
    
    for key in dic1:
        num1 = dic1.get(key)
        num2 = 0
        if dic2.get(key):
            num2 = dic2.pop(key)
        gyo += min(num1, num2)
        hap += max(num1, num2)
        
    for key in dic2:
        hap += dic2.get(key)
    
    if hap == 0:
        return 65536
    return int((gyo/hap) * 65536)
    
    