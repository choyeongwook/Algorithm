# 행의 수가 N이고 열의 수가 M인 격자의 각 칸에 1부터 N×M까지의 번호가 첫 행부터 시작하여 차례로 부여되어 있다. 격자의 어떤 칸은 ○ 표시가 되어 있다. (단, 1번 칸과 N × M번 칸은 ○ 표시가 되어 있지 않다. 또한, ○ 표시가 되어 있는 칸은 최대 한 개이다. 즉, ○ 표시가 된 칸이 없을 수도 있다.) 

# 행의 수가 3이고 열의 수가 5인 격자에서 각 칸에 번호가 1부터 차례대로 부여된 예가 아래에 있다. 이 격자에서는 8번 칸에 ○ 표시가 되어 있다.

# 격자의 1번 칸에서 출발한 어떤 로봇이 아래의 두 조건을 만족하면서 N×M번 칸으로 가고자 한다. 

# 조건 1: 로봇은 한 번에 오른쪽에 인접한 칸 또는 아래에 인접한 칸으로만 이동할 수 있다. (즉, 대각선 방향으로는 이동할 수 없다.)
# 조건 2: 격자에 ○로 표시된 칸이 있는 경우엔 로봇은 그 칸을 반드시 지나가야 한다. 
# 위에서 보인 것과 같은 격자가 주어질 때, 로봇이 이동할 수 있는 서로 다른 경로의 두 가지 예가 아래에 있다.

# 1 → 2 → 3 → 8 → 9 → 10 → 15
# 1 → 2 → 3 → 8 → 13 → 14 → 15
# 격자에 관한 정보가 주어질 때 로봇이 앞에서 설명한 두 조건을 만족하면서 이동할 수 있는 서로 다른 경로가 총 몇 개나 되는지 찾는 프로그램을 작성하라. 

n,m,k = map(int, input().split())

array = [[0] * m for _ in range(n)]

d = [[0] * m for _ in range(n)]
d[0][0] = 1


if k > 0:
    x = (k-1) // m
    y = (k-1) % m

    for i in range(x+1):
        for j in range(y+1):
            if i > 0:
                d[i][j] += d[i-1][j]
            if j > 0:
                d[i][j] += d[i][j-1]
    
    for i in range(x, n):
        for j in range(y, m):
            if i > x:
                d[i][j] += d[i-1][j]
            if j > y:
                d[i][j] += d[i][j-1]

else: 
    for i in range(n):
        for j in range(m):
            if i > 0:
                d[i][j] += d[i-1][j]
            if j > 0:
                d[i][j] += d[i][j-1]

print(d[-1][-1])