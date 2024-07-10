def solution(phone_book):
    phone_book.sort(key=lambda x: len(x))
    dic = dict()
    
    for phone in phone_book:
        for i in range(1,len(phone)+1):            
            if dic.get(phone[0:i]):
                return False
        
        dic[phone] = True
        
    return True