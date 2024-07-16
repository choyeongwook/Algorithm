import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    count = 0
    while True:
        food1 = heapq.heappop(scoville)
        if food1 >= K:
            return count
        if not scoville:
            return -1
        food2 = heapq.heappop(scoville)
        heapq.heappush(scoville, food1+food2*2)
        count += 1