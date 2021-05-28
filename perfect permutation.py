def findAns(n):
    if n%2 == 1:
        return "-1"
    else:
        a = [0]*n
        for i in range(n):
            if i%2 == 0:
                a[i] = str(i+2)
            else:
                a[i] = str(i)
    return " ".join(a)

n = int(input())
result = findAns(n)
print(result)
