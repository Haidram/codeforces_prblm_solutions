def solve(n, s):
    r = '2020'
    i = j = 0
    flag = True
    
    while j < 4:
        if s[i] == r[j]:
            i += 1
            j += 1
        elif flag:
            i = (n-1) - (3-j)
            flag = False
        else:
            break

    if j == 4:
        return 'YES'
    return 'NO'


t = int(input())
for i in range(t):
    n = int(input())
    s = input()
    print(solve(n, s))
