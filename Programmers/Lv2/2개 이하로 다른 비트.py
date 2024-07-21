def solution(numbers):
    binary_answer = []
    for number in numbers:
        binary = format_binary(number)
        # print(binary)
        isAllOne = True
        for i in range(len(binary)-1, -1, -1):
            if binary[i] == '0':
                if i == len(binary)-1:
                    binary_answer.append(binary[:len(binary)-1]+'1')
                    isAllOne = False
                    break
                else:
                    binary_answer.append(binary[:i]+'10'+binary[i+2:])
                    isAllOne = False
                    break
        if isAllOne:
            binary_answer.append('10'+binary[1:])
            
    # print(binary_answer)
    answer = []
    for bn in binary_answer:
        answer.append(int(bn, 2))
        
    return answer

def format_binary(num):
    n, mod = divmod(num, 2)
    
    if n == 0:
        return str(mod)
    else:
        return format_binary(n) + str(mod)
