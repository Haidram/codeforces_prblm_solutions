def solve(rc, arr):
    r = rc[0]
    c = rc[1]
    for i in range(r):
        for j in range(c):
            if arr[i][j] == 'S':
                if j+1 < c:
                    if arr[i][j+1] == 'W':
                        return arr, 'No'
                if j-1 >= 0:
                    if arr[i][j-1] == 'W':
                        return arr, 'No'
                if i+1 < r:
                    if arr[i+1][j] == 'W':
                        return arr, 'No'
                if i-1 >= 0:
                    if arr[i-1][j] == 'W':
                        return arr, 'No'

    ans = []
    for i in range(r):
        s = ''
        for j in range(c):
            if arr[i][j] == '.':
                s = s + 'D'
            else:
                s = s + arr[i][j]
        ans.append(s)

    return ans, 'Yes'


rc = list(map(int,input().strip().split()))[:2]
arr = []
for i in range(rc[0]):
    num = input()
    arr.append(num)
result, flag = solve(rc, arr)
print(flag)
if flag == 'Yes':
    for j in result:
        print(j)
