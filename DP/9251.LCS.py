# LCS(Longest Common Subsequence, 최장 공통 부분 수열)문제는 두 수열이 주어졌을 때, 모두의 부분 수열이 되는 수열 중 가장 긴 것을 찾는 문제이다.

# 예를 들어, ACAYKP와 CAPCAK의 LCS는 ACAK가 된다.

import sys
input = sys.stdin.readline

str1 = input().rstrip()
str2 = input().rstrip()

d = [[0] * (len(str2)+1) for _ in range(len(str1)+1)]

for i in range(len(str1)):
    for j in range(len(str2)):
        if str1[i] != str2[j]:
            d[i+1][j+1] = max(d[i][j+1], d[i+1][j])
        else:
            d[i+1][j+1] = d[i][j] + 1
print(d[-1][-1])