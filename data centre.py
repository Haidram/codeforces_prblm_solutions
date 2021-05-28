import math

def solve(n):
    check = int(math.sqrt(n))
    factor = []
    for i in range(1,check + 1):
        temp = n//i
        if temp*i == n:
            factor.append(i)
            factor.append(n//i)

    factor = list(set(factor))
    factor.sort()
    num_len = len(factor)
    print(factor)

    if num_len%2 == 1:
        num = factor[num_len//2]
        return 4*num
    else:
        num1 = factor[num_len//2]
        num2 = factor[num_len//2 - 1]
        return 2*(num1 + num2)
    

n = int(input())
print(solve(n))
