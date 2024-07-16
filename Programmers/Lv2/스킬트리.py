from collections import deque

def solution(skill, skill_trees):
    dic = {}
    for s in skill:
        dic[s] = True
    
    count = 0
    for skill_tree in skill_trees:
        isAnswer = True
        # [C, B, D]
        queue = deque(list(skill))
        for s in skill_tree:
            if not queue:
                break
            if dic.get(s) is not None and queue.popleft() != s:
                isAnswer = False
                break
        if isAnswer:
            print(skill_tree)
            count += 1
    
    return count