def solution(arr):
    
    for _ in range(len(arr)-1):
        a = arr.pop()
        b = arr.pop()   
        arr.append(a * b / uch(a, b))

    answer = arr[0]
    return answer


def uch(a, b):
    if a < b:
        a, b = b ,a

    while b != 0:
        a, b = b, a%b
    return a