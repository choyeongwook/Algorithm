# 어떤 극장의 좌석은 한 줄로 되어 있으며 왼쪽부터 차례대로 1번부터 N번까지 번호가 매겨져 있다. 공연을 보러 온 사람들은 자기의 입장권에 표시되어 있는 좌석에 앉아야 한다. 예를 들어서, 입장권에 5번이 쓰여 있으면 5번 좌석에 앉아야 한다. 단, 자기의 바로 왼쪽 좌석 또는 바로 오른쪽 좌석으로는 자리를 옮길 수 있다. 예를 들어서, 7번 입장권을 가진 사람은 7번 좌석은 물론이고, 6번 좌석이나 8번 좌석에도 앉을 수 있다. 그러나 5번 좌석이나 9번 좌석에는 앉을 수 없다.

# 그런데 이 극장에는 “VIP 회원”들이 있다. 이 사람들은 반드시 자기 좌석에만 앉아야 하며 옆 좌석으로 자리를 옮길 수 없다.

# 오늘 공연은 입장권이 매진되어 1번 좌석부터 N번 좌석까지 모든 좌석이 다 팔렸다. VIP 회원들의 좌석 번호들이 주어졌을 때, 사람들이 좌석에 앉는 서로 다른 방법의 가짓수를 구하는 프로그램을 작성하시오.

# 예를 들어서, 그림과 같이 좌석이 9개이고, 4번 좌석과 7번 좌석이 VIP석인 경우에 <123456789>는 물론 가능한 배치이다. 또한 <213465789> 와 <132465798> 도 가능한 배치이다. 그러나 <312456789> 와 <123546789> 는 허용되지 않는 배치 방법이다.

import sys

input = sys.stdin.readline

n = int(input())
m = int(input())
vip_list = []
for _ in range(m):
    vip_list.append(int(input())-1) # index와 맞추기 위한 -1


fibo = [0] * 42
fibo[1] = 1
for i in range(2, 42):
    fibo[i] = fibo[i-1] + fibo[i-2]


# vip 좌석을 기준으로 몇자리씩 나뉘어졌는지
seat = [] # [3, 2, 2]
cnt = 0
for i in range(n):
    if i in vip_list:
        if cnt > 1: # 2보다 크거나 같아야 의미 있음
            seat.append(cnt)
        cnt = 0
        continue
    cnt += 1
if cnt > 1:
    seat.append(cnt)

result = 1
for count in seat:
    result *= fibo[count+1]

print(result)

