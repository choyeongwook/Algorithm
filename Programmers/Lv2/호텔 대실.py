from heapq import heappop, heappush

def solution(book_time):
    array = []
    heap = []
    for i in range(len(book_time)):
        start = book_time[i][0].split(':')
        end = book_time[i][1].split(':')
        
        start = int(start[0])*60+int(start[1])
        end = int(end[0])*60+int(end[1])+10
        
        array.append([start, end])
    
    # start 기준으로 정렬
    array.sort(key=lambda x: x[0])
    
    result = 0
    for start, end in array:
        # 이미 진행한 것 중 끝난 게 있다면 그냥 heappop
        if heap and heap[0] <= start:
            heappop(heap)
        # 아니라면 result += 1
        else:
            result += 1
        heappush(heap, end)
    
    return result