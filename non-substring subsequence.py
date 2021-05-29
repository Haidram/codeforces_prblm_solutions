def solve(nq, s, lr):
    ## String s = abcdEFGHIjklm
    ## Substring = EFGHI

    ## We will check if we can find 'E' at the left side of 'E' or
    #  if we can find 'I' at the right side of 'I', so that we can
    #  make a good subsequence with easiest way possible

    ## Checking 'E' at the left side
    if lr[0] > 1:
        for i in range(lr[0]-1):
            if s[i] == s[lr[0]-1]:
                return "YES"

    ## Checking 'I' at the right side
    if lr[1] < nq[0]:
        for i in range(lr[1],nq[0]):
            if s[i] == s[lr[1]-1]:
                return "YES"

    ## If not find any then not possible
    return "NO"
    
    

t = int(input())                                            ## Taking input t
for i in range(t):
    nq = list(map(int,input().strip().split()))[:2]         ## Taking input n and q in nq = [n, q]
    s = input()                                             ## Taking s
    for j in range(nq[1]):
        lr = list(map(int,input().strip().split()))[:2]     ## Taking queries for string s, lr = [l, r]
        print(solve(nq, s, lr))
