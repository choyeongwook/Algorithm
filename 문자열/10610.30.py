# 어느 날, 미르코는 우연히 길거리에서 양수 N을 보았다. 미르코는 30이란 수를 존경하기 때문에, 그는 길거리에서 찾은 수에 포함된 숫자들을 섞어 30의 배수가 되는 가장 큰 수를 만들고 싶어한다.

# 미르코를 도와 그가 만들고 싶어하는 수를 계산하는 프로그램을 작성하라.

array_n = list(input())

if '0' in array_n and sum(map(int, array_n)) % 3 == 0:
    result = int(''.join(sorted(array_n, reverse=True)))

    if result > 0:
        print(result)
    else:
        print(-1)
else:
    print(-1)


