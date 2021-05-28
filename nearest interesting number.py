def checkNum(m):
    count = 0
    for k in str(m):
        count += int(k)
    if count%4 == 0:
        return True
    else:
        return False

def findNumber(n):
    i = -1
    stop = False
    while not stop:
        i += 1
        stop = checkNum(n+i)
    return n+i

n = int(input())
result = findNumber(n)
print(result)
