def solution(msg):
    answer = []
    dic = dict()
    for i in range(26):
        dic[chr(ord('A')+i)] = i+1
    dic_len = 26
    i = 0
    while i < len(msg):
        word = msg[i]
        
        while i+1 < len(msg):
            next_word = word + msg[i+1]
            if dic.get(next_word) is None:
                dic_len += 1
                dic[next_word] = dic_len
                break
            else:
                i += 1
                word = next_word
        answer.append(dic[word])
        i += 1
        
    return answer