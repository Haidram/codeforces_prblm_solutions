def get_ans(n):
    if n < 31:       ##If n is less than 30 then not possible
        return "NO"
    else:
        rem1 = 6         ##Getting the min
        rem2 = 10        ##value of the sum
        rem3 = 14        ##of n and rem send 
        rem4 = n - 30    ##to the last number
        if rem4 == rem1 or rem4 == rem2 or rem4 == rem3:  ##To confirm that all 4
            rem3 = 15                                     ##numbers are different
            rem4 -= 1
        return "{} {} {} {}".format(rem1, rem2, rem3, rem4)

t = int(input())     ##No of test cases
for i in range(t):
    n = int(input())    ##Getting the input for n
    result = get_ans(n) ##Getting the result
    if not result is "NO":
        print("YES")
    print(result)
