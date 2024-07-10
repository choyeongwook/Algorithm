from itertools import permutations
def solution(k, dungeons):
    permu = permutations(range(len(dungeons)), len(dungeons))
    
    answer = 0
    # (0,1,2,3,4,5,6,7)
    for order in permu:
        temp_k = k
        temp_res = 0
        for i in order:
            if dungeons[i][0] <= temp_k:
                temp_res += 1
                temp_k -= dungeons[i][1]
        answer = max(answer, temp_res)
    
    return answer