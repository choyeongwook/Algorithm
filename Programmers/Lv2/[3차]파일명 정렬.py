def solution(files):
    splited_array = []
    for index, file in enumerate(files):
        head, number = split_file(file)
        splited_array.append([head, number, index])
    
    splited_array.sort(key = lambda x: (x[0].lower(), int(x[1])))
        
    print(splited_array)
    answer = []
    for element in splited_array:
        answer.append(files[element[2]])
    
    return answer

def split_file(file_name):
    str_numbers = ['0','1','2','3','4','5','6','7','8','9']
    head_stack = []
    number_stack = []
    
    process = 0
    for char in file_name:
        if process == 0:
            if char not in str_numbers:
                head_stack.append(char)
            else:
                process = 1
                number_stack.append(char)
        elif process == 1:
            if char in str_numbers and len(number_stack) < 5:
                number_stack.append(char)
            else:
                break
        else:
            break
    
    return [''.join(head_stack), ''.join(number_stack)]