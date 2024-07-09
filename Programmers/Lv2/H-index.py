def solution(citations):
    citations.sort(reverse=True)
    print(citations)
    
    result = 0
    for i in range(len(citations)):
        if i+1 >= citations[i]:
            result = max(result, citations[i])
        else:
            result = max(result, i+1)
    return result