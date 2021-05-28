def solve(n):
    factor_2 = factor_3 = 0

    while n%2 == 0:
        n = n//2
        factor_2 += 1

    while n%3 == 0:
        n = n//3
        factor_3 += 1

    if n != 1 or factor_2 > factor_3:
        return '-1'
    else:
        count = 0
        count = factor_3 - factor_2
        count += factor_3
        return count

t = int(input())
for i in range(t):
    n = int(input())
    print(solve(n))
