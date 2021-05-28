def solve(n, a):
    ## First we check for no. of pos int
    ## We make all pos int equal to +1 and cal the cost
    ## We make all neg int equal to -1 and cal the cost
    ## If number of neg int are even then good or else,
    #  we will make -1 from one 1, but if there is 0 in
    #  the array then we don't to worry anything.

    count_neg_int = cost = 0
    flag = False
    for i in range(n):
        if a[i] >= 1:
            cost += (a[i]-1)             ## Cal cost for making +1
        elif a[i] <= -1:
            cost -= (1+a[i])             ## Cal cost for making -1
            count_neg_int += 1           ## Counting no. of neg int
        else:                            ## Checking if there is any zero present
            cost += 1
            flag = True

    if flag:
        return cost
    else:
        if count_neg_int%2 == 1:
            return cost + 2
        return cost
        


n = int(input())                                   ## taking inputs
a = list(map(int,input().strip().split()))[:n]     #  from the user
print(solve(n, a))
