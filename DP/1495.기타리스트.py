# Day Of Mourning의 기타리스트 강토는 다가오는 공연에서 연주할 N개의 곡을 연주하고 있다. 지금까지 공연과는 다른 공연을 보여주기 위해서 이번 공연에서는 매번 곡이 시작하기 전에 볼륨을 바꾸고 연주하려고 한다.

# 먼저, 공연이 시작하기 전에 각각의 곡이 시작하기 전에 바꿀 수 있는 볼륨의 리스트를 만들었다. 이 리스트를 V라고 했을 때, V[i]는 i번째 곡을 연주하기 전에 바꿀 수 있는 볼륨을 의미한다. 항상 리스트에 적힌 차이로만 볼륨을 바꿀 수 있다. 즉, 현재 볼륨이 P이고 지금 i번째 곡을 연주하기 전이라면, i번 곡은 P+V[i]나 P-V[i] 로 연주해야 한다. 하지만, 0보다 작은 값으로 볼륨을 바꾸거나, M보다 큰 값으로 볼륨을 바꿀 수 없다.

# 곡의 개수 N과 시작 볼륨 S, 그리고 M이 주어졌을 때, 마지막 곡을 연주할 수 있는 볼륨 중 최댓값을 구하는 프로그램을 작성하시오. 모든 곡은 리스트에 적힌 순서대로 연주해야 한다.


# 단순히 n제곱으로 구현하기
# 반복문 진행할 수록 2배씩 커짐 => n이 50이므로 2^50

# 이전 값의 최댓값으로 현재 값을 구할 수 있는지?? x

# 값의 중복이 없다면 -> set 자료구조 사용

n, start, maximum = map(int, input().split())

array = list(map(int, input().split()))

s = {start}

for v in array:
    temp = set()
    for current in s:
        if 0 <= current - v <= maximum:
            temp.add(current - v)
        if 0 <= current + v <= maximum:
            temp.add(current + v)
    s = temp

if len(s) < 1:
    print(-1)
else:
    print(max(s))