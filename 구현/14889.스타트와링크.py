import sys
from itertools import combinations
from itertools import permutations

input = sys.stdin.readline

n = int(input())

array = [list(map(int, input().split())) for _ in range(n)]

# print(array)

# 1. 팀을 나눌 경우의 수 구하기 (조합)
# 2. 팀대로 나눴을 때 차이 구하기
# 3. 가장 작은거 저장하기

combi = list(combinations(range(n), n//2))

result = 10**9

for i in range(len(combi)//2):
    team1 = list(permutations(combi[i], 2))
    team2 = list(permutations(combi[-1-i], 2))
    
    team1_score = 0
    team2_score = 0
    
    for j, k in team1:
        team1_score += array[j][k]
    for j, k in team2:
        team2_score += array[j][k]
    
    result = min(result, abs(team1_score - team2_score))

print(result)