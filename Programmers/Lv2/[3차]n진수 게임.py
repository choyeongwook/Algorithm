def solution(n, t, m, p):
    
    result = []
    num = 0
    current = 1
    while len(result) < t:
        for i in convert(num, n):
            if current == p:
                result.append(i)
            current += 1
            if current > m:
                current = 1
        num += 1
    
    return ''.join(result[:t])


digit = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
def convert(num, jinsu):
    n, mod = divmod(num, jinsu)
    
    if n == 0:
        return digit[mod]
    else:
        return convert(n, jinsu) + digit[mod]