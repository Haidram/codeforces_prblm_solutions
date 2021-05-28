def findStr(s):
    flag = 0
    arr = []
    for i in s:
        if i is '.' and flag == 0:
            arr.append('0')
        elif i is '-' and flag == 0:
            flag = 1
        elif i is '-' and flag == 1:
            arr.append('2')
            flag = 0
        elif i is '.' and flag == 1:
            arr.append('1')
            flag = 0
    return "".join(arr)

s = input()
result = findStr(s)
print(result)
