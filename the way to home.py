def solve(nd, s):
    n = nd[0]
    d = nd[1]

    i = count = 0
    j = d

    while i != n-1:
        if j<n and s[j] == '1':
            i = j
            j = i+d
            count += 1
        else:
            j -= 1

        if j == i:
            return '-1'
        
    return count


nd = list(map(int,input().strip().split()))[:2]
s = input()
print(solve(nd, s))
