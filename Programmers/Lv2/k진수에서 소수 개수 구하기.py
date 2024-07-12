def solution(n, k):
    converted_num = convert(n, k)
    
    print(converted_num)
    
    array = converted_num.split('0')
    
    print(array)
    
    result = 0
    for num in array:
        if num != '' and isPrimeNumber(int(num)):
            result += 1
    
    return result

def convert(num, base):
    n, mod = divmod(num, base)
    
    if n == 0:
        return str(mod)
    else:
        return convert(n, base) + str(mod)

def isPrimeNumber(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    
    return True