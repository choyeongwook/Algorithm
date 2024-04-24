# 마법사 상어가 토네이도를 배웠고, 오늘은 토네이도를 크기가 N×N인 격자로 나누어진 모래밭에서 연습하려고 한다. 위치 (r, c)는 격자의 r행 c열을 의미하고, A[r][c]는 (r, c)에 있는 모래의 양을 의미한다.

# 토네이도를 시전하면 격자의 가운데 칸부터 토네이도의 이동이 시작된다. 토네이도는 한 번에 한 칸 이동한다. 다음은 N = 7인 경우 토네이도의 이동이다.

# 토네이도가 한 칸 이동할 때마다 모래는 다음과 같이 일정한 비율로 흩날리게 된다.

# 토네이도가 x에서 y로 이동하면, y의 모든 모래가 비율과 α가 적혀있는 칸으로 이동한다. 비율이 적혀있는 칸으로 이동하는 모래의 양은 y에 있는 모래의 해당 비율만큼이고, 계산에서 소수점 아래는 버린다. α로 이동하는 모래의 양은 비율이 적혀있는 칸으로 이동하지 않은 남은 모래의 양과 같다. 모래가 이미 있는 칸으로 모래가 이동하면, 모래의 양은 더해진다. 위의 그림은 토네이도가 왼쪽으로 이동할 때이고, 다른 방향으로 이동하는 경우는 위의 그림을 해당 방향으로 회전하면 된다.

# 토네이도는 (1, 1)까지 이동한 뒤 소멸한다. 모래가 격자의 밖으로 이동할 수도 있다. 토네이도가 소멸되었을 때, 격자의 밖으로 나간 모래의 양을 구해보자.

import sys

input = sys.stdin.readline

n = int(input())
array = []
for _ in range(n):
    array.append(list(map(int, input().split())))

# n = 7
# array = [[0,0,0,100,0,0,0],[0,0,0,0,0,0,0],[0,100,0,0,0,0,0],[0,0,100,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]]


# 시작 좌표
current = (n//2, n//2)

result = 0
# 격자의 밖으로 나간 모래의 양(result) 구하기

direction = 0
directions = ((0, -1), (1, 0), (0, 1), (-1, 0)) # left, down, right, up
distance = 1
update_direction_count = 0
result = 0

while (current[0] >= 0 and current[1] >= 0):
    
    # 토네이도 순회
    for i in range(distance):
        dx, dy = directions[direction]
        x, y = current
        nx, ny = x+dx, y+dy
        current = (nx, ny)
        if nx < 0 or ny < 0:
            break
        # print(current)

        before_sand_mount = array[nx][ny]

        array[nx][ny] = 0 # 현재 좌표 모래 없앰
        if before_sand_mount == 0:
            continue
        
        sand_except_alpha = 0
        # ==================== # left, down, right, up
        dx, dy = directions[direction -1] # 오른쪽 90도

        nnx, nny = nx+dx, ny+dy # 1칸 떨어짐
        add_sand = int(before_sand_mount / 100 * 7)
        sand_except_alpha += add_sand
        if 0 <= nnx < n and 0 <= nny < n:
            array[nnx][nny] += add_sand  # 7%
        else:
            result += add_sand

        # 2칸 떨어짐
        dx, dy = directions[direction -2] # 오른쪽의 오른쪽

        add_sand = int(before_sand_mount / 100 * 1)
        sand_except_alpha += add_sand
        if 0 <= nnx+dx < n and 0 <= nny+dy < n:
            array[nnx+dx][nny+dy] += add_sand  # 1%
        else:
            result += add_sand
        
        dx, dy = directions[direction -1] # 오른쪽의 직진

        add_sand = int(before_sand_mount / 100 * 2)
        sand_except_alpha += add_sand
        if 0 <= nnx+dx < n and 0 <= nny+dy < n:
            array[nnx+dx][nny+dy] += add_sand  # 2%
        else:
            result += add_sand
        
        dx, dy = directions[direction] # 오른쪽의 왼쪽

        add_sand = int(before_sand_mount / 100 * 10)
        sand_except_alpha += add_sand
        if 0 <= nnx+dx < n and 0 <= nny+dy < n:
            array[nnx+dx][nny+dy] += add_sand  # 10%
        else:
            result += add_sand
        
        
        # ====================# left, down, right, up
        dx, dy = directions[direction -3] # 왼쪽 90도

        nnx, nny = nx+dx, ny+dy # 1칸 떨어짐
    
        add_sand = int(before_sand_mount / 100 * 7)
        sand_except_alpha += add_sand
        if 0 <= nnx < n and 0 <= nny < n:
            array[nnx][nny] += add_sand  # 7%
        else:
            result += add_sand

        # 2칸 떨어짐
        dx, dy = directions[direction -2] # 왼쪽의 왼쪽

        add_sand = int(before_sand_mount / 100 * 1)
        sand_except_alpha += add_sand
        if 0 <= nnx+dx < n and 0 <= nny+dy < n:
            array[nnx+dx][nny+dy] += add_sand  # 1%
        else:
            result += add_sand
        
        dx, dy = directions[direction -3] # 오른쪽의 직진

        add_sand = int(before_sand_mount / 100 * 2)
        sand_except_alpha += add_sand
        if 0 <= nnx+dx < n and 0 <= nny+dy < n:
            array[nnx+dx][nny+dy] += add_sand  # 2%
        else:
            result += add_sand
        
        dx, dy = directions[direction] # 오른쪽의 왼쪽

        add_sand = int(before_sand_mount / 100 * 10)
        sand_except_alpha += add_sand
        if 0 <= nnx+dx < n and 0 <= nny+dy < n:
            array[nnx+dx][nny+dy] += add_sand  # 10%
        else:
            result += add_sand

        # ========
        # 현재 방향
        dx, dy = directions[direction]

        # 2칸 앞
        add_sand = int(before_sand_mount / 100 * 5)
        sand_except_alpha += add_sand
        if 0 <= nx+dx*2 < n and 0 <= ny+dy*2 < n:
            array[nx+dx*2][ny+dy*2] += add_sand  # 5%
        else:
            result += add_sand
        
         # 1칸 앞 (알파)
        add_sand = before_sand_mount - sand_except_alpha
        if 0 <= nx+dx < n and 0 <= ny+dy < n:
            array[nx+dx][ny+dy] += add_sand  # 나머지
        else:
            result += add_sand

        # for i in array:
        #     print(*i)
        # print(result)
        # print()
    
    update_direction_count += 1
    if update_direction_count % 2 == 0:
        distance += 1
        
    
    # 방향 재설정
    direction += 1
    if direction >= 4:
        direction = 0

# for i in array:
#     print(*i)
print(result)
