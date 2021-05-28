def find_n(n):
    x = n-1
    t = 1
    i = 1
    while i < n:
        print("? "+str(t)+" "+str(i)+" "+str(i+1)+" "+str(x))
        temp = int(input())
        if temp == n:
            return i+1
        elif temp == n-1:
            print("? "+str(t)+" "+str(i+1)+" "+str(i)+" "+str(x))
            temp1 = int(input())
            if temp1 == n:
                return i
        i += 2
    return n

def solve(n):
    j = find_n(n)
    t = 2
    x = 1
    s = "!"
    
    for i in range(1,n+1):
        if i != j:
            print("? "+str(t)+" "+str(i)+" "+str(j)+" "+str(x))
        temp = input()
        s = s + " " + temp

    return s

t = int(input())
for i in range(t):
    n = int(input())
    result = solve(n)
    print(result)
