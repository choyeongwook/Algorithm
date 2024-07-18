def solution(record):
    name_dic = {}
    result = []
    
    for r in record:
        splited = r.split()
        operator, uid = splited[0], splited[1]
        
        if operator == 'Enter':
            name = splited[2]
            name_dic[uid] = name
        elif operator == 'Leave':
            pass
        elif operator == 'Change':
            name = splited[2]
            name_dic[uid] = name
            
    for r in record:
        splited = r.split()
        operator, uid = splited[0], splited[1]
        
        if operator == 'Enter':
            result.append(f'{name_dic[uid]}님이 들어왔습니다.')
        elif operator == 'Leave':
            result.append(f'{name_dic[uid]}님이 나갔습니다.')
        elif operator == 'Change':
            pass
    
    return result