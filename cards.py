def findAns(s):
    no_0 = 0
    no_1 = 0
    for i in s:
        if i is 'z':
            no_0 += 1
        elif i is 'n':
            no_1 += 1
    a = [str(1)]*(no_1)
    b = [str(0)]*(no_0)
    arr = a+b
    return " ".join(arr)

n = int(input())
s = input()
result = findAns(s)
print(result)
