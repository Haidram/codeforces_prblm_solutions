def findnum(s):
    count = 0
    start = 0
    rem = 0
    for i in s:
        if i is '1':
            start = 1
            
        if i is '0' and start == 1:
            rem += 1
        elif i is '1' and start == 1:
            count += rem
            rem = 0
    return count
    

t = int(input())
for i in range(t):
    s = input()
    result = findnum(s)
    print(result)
