from collections import Counter

def solution(k, tangerine):
    counter = Counter(tangerine)
    most_common = counter.most_common()
    
    answer = 0
    for common in most_common:
        answer += 1
        k -= common[1]
        if k <= 0:
            return answer