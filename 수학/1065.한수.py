# 어떤 양의 정수 X의 각 자리가 등차수열을 이룬다면, 그 수를 한수라고 한다.
# 등차수열은 연속된 두 개의 수의 차이가 일정한 수열을 말한다.
# N이 주어졌을 때, 1보다 크거나 같고, N보다 작거나 같은 한수의 개수를 출력하는 프로그램을 작성하시오.
# 1 < N < 1000

N = int(input())

count = 0
for i in range(1, N + 1):
    if i < 100:
        count += 1
        continue
    elif i > 999:
        continue
    else:
        hundred = i//100 % 10
        ten = i//10 % 10
        one = i % 10

        if (hundred - ten) == (ten - one):
            count += 1

print(count)