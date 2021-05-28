import math

def gcd(a, b):
    if a == 0:
        return b
    elif b == 0:
        return a
    else:
        if a < b:
            temp = b//a
            b -= temp*a
            ans = gcd(a, b)
            return ans
        elif b < a:
            temp = a//b
            a -= temp*b
            ans = gcd(a, b)
            return ans
        else:
            return a

def solve(arr, n):
    flag = True
    for i in range(n-1):
        if gcd(arr[i], arr[i+1]) != 1:
            flag = False
            break
    if flag:
        return 0
    
    min_num = min(arr)
    i_ind = arr.index(min_num)
    count = 0
    out_arr = []
    
    if i_ind%2 == 0:
        j_ind = 1
        repl = 10**9 + 7
        while j_ind < n:
            out = str(i_ind+1)+" "+str(j_ind+1)+" "+str(min_num)+" "+str(repl)
            out_arr.append(out)
            j_ind += 2
            count += 1
        out_arr.append(count)
        return out_arr
    else:
        j_ind = 0
        repl = 10**9 + 7
        while j_ind < n:
            out = str(i_ind+1)+" "+str(j_ind+1)+" "+str(min_num)+" "+str(repl)
            out_arr.append(out)
            j_ind += 2
            count += 1
        out_arr.append(count)
        return out_arr

t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int,input().strip().split()))[:n]
    result = solve(arr,n)
    if result == 0:
        print(result)
    else:
        print(result[-1])
        for value in range(len(result)-1):
            print(result[value])
