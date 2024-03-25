# 수를 처리하는 것은 통계학에서 상당히 중요한 일이다. 통계학에서 N개의 수를 대표하는 기본 통계값에는 다음과 같은 것들이 있다. 단, N은 홀수라고 가정하자.

# 산술평균 : N개의 수들의 합을 N으로 나눈 값
# 중앙값 : N개의 수들을 증가하는 순서로 나열했을 경우 그 중앙에 위치하는 값
# 최빈값 : N개의 수들 중 가장 많이 나타나는 값
# 범위 : N개의 수들 중 최댓값과 최솟값의 차이
# N개의 수가 주어졌을 때, 네 가지 기본 통계값을 구하는 프로그램을 작성하시오.
import sys
from collections import Counter

N = int(input())

array = [int(sys.stdin.readline()) for _ in range(N)]
array.sort()

# 산술평균
print(round(sum(array) / N))

# 중앙값
print(array[N//2])

# 최빈값
counter = Counter(array).most_common()
if  N == 1:
    print(array[0])
elif counter[0][1] == counter[1][1]:
    print(counter[1][0])
else:
    print(counter[0][0])

# 범위
print(max(array) - min(array))