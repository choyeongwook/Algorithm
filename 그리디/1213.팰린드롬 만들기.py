name = list(input())

# 사전 순 정렬
name.sort()

dic = dict()
# 개수 세기
for char in name:
    if char in dic:
        dic[char] += 1
    else:
        dic[char] = 1


# 홀수가 하나까지만 가능
odd = False
for char in dic:
    if dic[char] % 2 != 0:
        if odd:
            print('I\'m Sorry Hansoo')
            exit(0)
        else:
            odd = char

array = []
for char in dic:
    array.append(char*(dic[char]//2))

result = ''.join(array)

if odd:
    result += odd
    
array.reverse()

result += ''.join(array)

print(result)