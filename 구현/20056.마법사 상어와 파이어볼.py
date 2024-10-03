import sys

input = sys.stdin.readline

n, m, k = map(int, input().split())

# 행 열 질량 속력 방향
fireballs = [list(map(int, input().split())) for _ in range(m)]

directions = ((-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1))

for _ in range(k):
    dic = dict()
    two_more = set()
    one = set()
    # 파이어볼 이동
    for fireball in fireballs:
        r,c,m,s,d = fireball
        
        dx, dy = directions[d]
        dx *= s
        dy *= s
        
        nx, ny = r+dx, c+dy
        
        # 맵은 연결되어있음
        if nx < 1: # nx가 0일때, n으로 보내야함. -1일때 n-1
            nx = n-(-nx)%n
        if ny < 1:
            ny = n-(-ny)%n
        if nx > n: # nx가 n+1일때 1로 보내야함. n+2일때 2
            nx = 1+((nx-1)%n)
        if ny > n:
            ny = 1+((ny-1)%n)
        
        if dic.get((nx, ny)):
            two_more.add((nx, ny))
            try:
                one.remove((nx, ny))
            except:
                pass
            dic[(nx,ny)].append(fireball)
        else:
            dic[(nx,ny)] = [fireball]
            one.add((nx, ny))
    
    # print(dic)
    # print(two_more)
    # 합쳐질 파이어볼 탐색
    # 파이어볼 합치기
    fireballs.clear()
    for x, y in two_more:
        m_sum = 0
        s_sum = 0
        count = 0
        is_all_odd = True
        is_all_even = True
        for r,c,m,s,d in dic[(x,y)]: # [[1, 1, 5, 2, 2], [1, 4, 7, 1, 6]]
            m_sum += m
            s_sum += s
            count += 1
            if d % 2 == 0:
                is_all_odd = False
            else:
                is_all_even = False

        new_m = m_sum//5
        # 질량 0인거 삭제
        if new_m == 0:
            # print('질량0이라소멸')ㄴ
            continue
        
        new_s = s_sum//count
        new_d_list = (1,3,5,7)
        if is_all_odd or is_all_even:
            new_d_list = (0,2,4,6)
        
        # r,c,m,s,d
        for new_d in new_d_list:
            fireballs.append((x,y,new_m,new_s,new_d))
        
    
    # 안 합쳐질 fireball
    for x, y in one:
        for r,c,m,s,d in dic[(x,y)]:
            fireballs.append((x,y,m,s,d))
    # 질량은 ⌊(합쳐진 파이어볼 질량의 합)/5⌋이다.
    # 속력은 ⌊(합쳐진 파이어볼 속력의 합)/(합쳐진 파이어볼의 개수)⌋이다.
    # 합쳐지는 파이어볼의 방향이 모두 홀수이거나 모두 짝수이면, 방향은 0, 2, 4, 6이 되고, 그렇지 않으면 1, 3, 5, 7이 된다.
    # 질량이 0인 파이어볼은 소멸되어 없어진다.
    
# print(fireballs)
result = 0
for r,c,m,s,d in fireballs:
    result += m
print(result)