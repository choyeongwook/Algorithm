def solution(n):
    array = []
    for i in range(n):
        array.append([0]*(i+1))
    answer = []
    directions = ((1,0), (0,1), (-1,-1))
    direction = 0
    x, y = 0, 0
    i = 1
    array[x][y] = i
    for i in range(2, sum(range(n+1))+1):
        dx, dy = directions[direction]
        nx, ny = x+dx, y+dy
        # print(nx, ny)
        if nx < 0 or nx >= n or ny < 0 or ny >= n or array[nx][ny] != 0:
            direction += 1
            if direction == 3:
                direction = 0

            dx, dy = directions[direction]
            nx, ny = x+dx, y+dy

        array[nx][ny] = i
        x, y = nx, ny
    # print(array)
    answer = []
    for arr in array:
        for i in arr:
            # print(i)
            answer.append(i)
    return answer