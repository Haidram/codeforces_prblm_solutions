def getPrint(num):
    count = 0
    num = str(num)
    outStr = []
    zeroes = []
    sizeNum = len(num)
    j = 0
    for i in num:
        if i != '0':
            outStr.append(int(i))
            count += 1
            zeroes.append(sizeNum-1-j)
        j += 1
    print(count)
    for k in range(len(outStr)):
        print(str(outStr[k]) + "".join(['0']*zeroes[k]), end = " ")
    print()

n = int(input())
a = [0]*n
for i in range(n):
    a[i] = int(input())
for j in range(n):
    getPrint(a[j])
