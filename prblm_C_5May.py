def solve(n):
    if n == 2:
        return "-1"
    else:
        arr = []
        start = 1
        curr = start
        end = n**2
        incr = 2
        for i in range(1,n**2+1):
            if curr <= end:
                arr.append(str(curr))
                curr += incr
            else:
                curr = start + 1
                arr.append(str(curr))
                curr += incr
        return arr

t = int(input())
for i in range(t):
    n = int(input())
    result = solve(n)
    start = 1
    if result == "-1":
        print(result)
    else:
        for i in range(n):
            char = result[(start-1)*n:start*n]
            start += 1
            print(" ".join(char))
            
