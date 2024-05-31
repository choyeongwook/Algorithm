def solution(n):
    
    count_one = format(n, 'b').count('1')
    print(count_one)
    curr = n+1
    
    while True:
        if format(curr, 'b').count('1') == count_one:
            return curr
        curr += 1
    