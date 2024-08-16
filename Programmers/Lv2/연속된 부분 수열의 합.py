def solution(sequence, k):
    cur_sum = 0
    index = len(sequence)-1
    for i in range(len(sequence)-1, -1, -1):
        for j in range(index, -1, -1):
            cur_sum += sequence[j]
            
            if cur_sum == k:
                if sequence[i] != sequence[j]:
                    return [j,i]
                else:
                    for k in range(0, j+1):
                        if sequence[j] == sequence[k]:
                            return [k, k+(i-j)]
            elif cur_sum > k:
                cur_sum -= sequence[i]
                index = j-1
                break