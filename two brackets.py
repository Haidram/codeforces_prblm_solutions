

def find_max_ways(s):
    count = c1 = c2 = 0
    for i in s:
        if i == '(':
            c1 += 1
        elif i == '[':
            c2 += 1
        
        if i == ')':
            if c1>0:
                count += 1
                c1 -= 1
        elif i == ']':
            if c2 > 0:
                count += 1
                c2 -= 1
    return count
            

t = int(input())
for i in range(t):
    s = input()
    print(find_max_ways(s))
