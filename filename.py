def findstr(s):
    no_x = 0
    drop_x = 0
    for i in s:
        if i is 'x':
            no_x += 1
        else:
            no_x = 0
        
        if no_x > 2 :
            drop_x += 1
    return drop_x

n = int(input())
s = input()
result = findstr(s)
print(result)
