def sideNo(m):
    if m[0] == 'T':
        face = 4
    elif m[0] == 'C':
        face = 6
    elif m[0] == 'O':
        face = 8
    elif m[0] == 'D':
        face = 12
    else:
        face = 20
    return face

n = int(input())
count = 0
for i in range(n):
    s = ""
    s = input()
    count += sideNo(s)
print(count)
