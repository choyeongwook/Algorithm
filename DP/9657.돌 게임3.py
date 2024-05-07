# 돌 게임은 두 명이서 즐기는 재밌는 게임이다.

# 탁자 위에 돌 N개가 있다. 상근이와 창영이는 턴을 번갈아가면서 돌을 가져가며, 돌은 1개, 3개 또는 4개 가져갈 수 있다. 마지막 돌을 가져가는 사람이 게임을 이기게 된다.

# 두 사람이 완벽하게 게임을 했을 때, 이기는 사람을 구하는 프로그램을 작성하시오. 게임은 상근이가 먼저 시작한다.


n = int(input())

if n < 5:
    if n == 2:
        print("CY")
        exit(0)
    print("SK")
    exit(0)

d = [True] * (n+1)
d[2] = False

for i in range(5, n+1):
    # CY
    current = False
    # 1개, 3개, 4개 가져가서
    for j in (1, 3, 4):
        # 상대를 지게 할 수 있는 패를 하나라도 줄 수 있다면
        if d[i-j] == False:
            # SK
            current = True
            break
    d[i] = current

if d[-1]:
    print('SK')
else:
    print('CY')

