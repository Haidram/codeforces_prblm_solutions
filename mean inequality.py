def solve(n, a):
    ans = []                                            ## Array for returning the answer
    if n == 1:
        for i in a:
            ans.append(str(i))                          ## If array contain only 2 elements then
        return " ".join(ans)                            #  return it as it is

    a.sort()                                            ## Sort the array, and
    mid_ele = a[n-1]                                    #  find the middle element

    i = 0
    while i < n:
        ans.append(str(a[n-1-i]))                       ## First append one element present on the left
        ans.append(str(a[n+i]))                         #  side of middle element then one element from
        i += 1                                          #  right side and so on

    return " ".join(ans)                                ## Return the answer
    


t = int(input())
for i in range(t):
    n = int(input())                                       ## Taking input n
    a = list(map(int,input().strip().split()))[:2*n]       ## Taking input the array a
    print(solve(n, a))
