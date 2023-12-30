# 배열을 정렬하는 것은 쉽다. 수가 주어지면, 그 수의 각 자리수를 내림차순으로 정렬해보자.
# N <= 1,000,000,000

N = input()

number_array = list(N)

number_array.sort(reverse=True)

print(int(''.join(number_array)))