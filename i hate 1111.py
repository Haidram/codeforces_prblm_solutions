def solve(n):
    ## If you analyse then by looking closely,
    #     11 =   1 x 11
    #    111 =   1 x 111
    #   1111 =  11 x 101
    #  11111 =  11 x 1000 + 111
    #    therefore we require 
    #    A = a x 11 + b x 111
    
    if n%11 == 0 or n%111 == 0:         ## If a = 0 or b = 0
        return "YES"

    if n < 111 :                        ## If a = 0 didn't work but
        return "NO"                     #  the no. is less than 111

    num = n%111
    if num%11 == 0:
        return "YES"

    x = n//111                          ## Checking for all possible
    while x >= 1:                       #  values of b from b_max to 
        rem = n - (111*x)               #  b equal to 1.
        if rem%11 == 0:
            return "YES"
        x -= 1

    return "NO"


t = int(input())
for i in range(t):
    n = int(input())        ## Taking inputs
    print(solve(n))
