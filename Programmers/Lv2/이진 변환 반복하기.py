# format(숫자, b) 10진수 to binary
# format(숫자, o) 10진수 to octet
# format(숫자, x) 10진수 to hex

# int('2|8|16진수', 2|8|16) -> 10진수로
def solution(s):
    count = 0
    deleted_zero = 0
    
    while s != "1":
        zero_count = s.count("0")
        deleted_zero += zero_count
        
        remain_one_length = len(s)-zero_count
        
        s = format(remain_one_length, "b")
        count += 1
    
    answer = [count, deleted_zero]
    return answer