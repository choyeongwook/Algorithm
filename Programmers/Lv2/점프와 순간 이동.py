def solution(n):
    cost = 0
    while n > 0:
        # 2로 나누어 떨어지면 나눈다
        if n % 2 == 0:
            n /= 2
        # 홀수라면 1 뺀다
        else:
            n -= 1
            cost += 1

    return cost