a = input()
b = input()

d = [[0] * (len(b)+1) for _ in range(len(a)+1)]
d_str = [[''] * (len(b)+1) for _ in range(len(a)+1)]

for i in range(len(a)):
    for j in range(len(b)):
        if a[i] == b[j]:
            d[i+1][j+1] = d[i][j] + 1
            d_str[i+1][j+1] = d_str[i][j]+a[i]
        else:
            if d[i+1][j] > d[i][j+1]:
                d[i+1][j+1] = d[i+1][j]
                d_str[i+1][j+1] = d_str[i+1][j]
            else:
                d[i+1][j+1] = d[i][j+1]
                d_str[i+1][j+1] = d_str[i][j+1]

print(d[len(a)][len(b)])
if (d[len(a)][len(b)] != 0):
    print(d_str[len(a)][len(b)])
