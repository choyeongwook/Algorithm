d = [0] * 100001

d[1] = 1

for i in range(2, 100001):
    d[i] = (d[i-1]%1234567 + d[i-2]%1234567)%1234567

def solution(n):
    return d[n]