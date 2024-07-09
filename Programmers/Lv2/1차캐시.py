from collections import deque

def solution(cacheSize, cities):
    if cacheSize == 0:
        return 5*len(cities)
    answer = 0
    
    queue = deque()
    dic = dict()
    
    for city in cities:
        city = city.lower()
        if dic.get(city):
            answer += 1
            queue.remove(city)
        else:
            answer += 5
        
            if len(queue) == cacheSize:
                dic.pop(queue.popleft())
                # remove = queue.popleft()
                # if dic.get(remove):
                #     dic.pop(remove)

        queue.append(city)
        dic[city] = True
    return answer