def solve(n,sheeps):
    result = count = index = 0
    for i in sheeps:
        if i == '*':
            count += 1

    count = (count+1)//2
    for i in range(n):
        if sheeps[i] == '*':
             count -= 1
        if count == 0:
            index = i
            break

    step = temp = 0
    j = i - 1
    while j >= 0:
        if sheeps[j] == '.':
            temp += 1
        else:
            step += temp
        j -= 1

    result += step
    step = temp = 0
    j = i + 1
    while j < n:
        if sheeps[j] == '.':
            temp += 1
        else:
            step += temp
        j += 1

    result += step
    return result
    
t = int(input())
for i in range(t):
    n = int(input())
    sheeps = input()
    print(solve(n,sheeps))
