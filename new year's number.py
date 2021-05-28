def solve(n):
    quo = n//2020
    rem = n%2020

    if quo >= rem:
        return "YES"
    else:
        return "NO"


t = int(input())
for i in range(t):
    n = int(input())
    print(solve(n))
