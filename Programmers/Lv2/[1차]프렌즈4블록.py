def solution(m, n, board):
    # m, n = n, m # n: 높이, m: 폭
    
    board_array = [[] for _ in range(len(board[0]))]
    
#     [5][0] -> [0][0]
#     [4][0] -> [0][1]
#     [3][0] -> [0][2]
#     ...
    
#     [5][1] -> [1][0]
#     [4][1] -> [1][1]
    for i in range(len(board[0])):
        for j in range(len(board)):
            board_array[i].append(board[len(board)-1-j][i])
            
    # print_board(board_array)
    result = 0
    while True:
        going_to_pop = set()
        for i in range(len(board_array)-1):
            m_length = min(len(board_array[i]), len(board_array[i+1]))
            for j in range(m_length-1):
                if board_array[i][j] == board_array[i+1][j] == board_array[i][j+1] == board_array[i+1][j+1]:
                    going_to_pop.add((i,j))
                    going_to_pop.add((i+1,j))
                    going_to_pop.add((i,j+1))
                    going_to_pop.add((i+1,j+1))
        
        if not going_to_pop:
            break
        for x, y in sorted(going_to_pop, key = lambda x: -x[1]):
            board_array[x].pop(y)
            result += 1

        # print_board(board_array)
    
    
    return result

def print_board(board):
    for b in board:
        print(*b)