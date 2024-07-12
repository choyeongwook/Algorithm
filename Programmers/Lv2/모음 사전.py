import sys
sys.setrecursionlimit(10**8)
tuple = ('A','E','I','O','U')
result = -1

def solution(word):
    dfs(word, '')
    return result

def dfs(target, current):
    global result
    result += 1
    if target == current:
        return False
    else:
        if len(current) == 5:
            return True
        for i in range(5):
            if not dfs(target, current+tuple[i]):
                return
    return True