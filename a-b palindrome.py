def change(s, ind, repl):
    return s[:ind]+repl+s[ind+1:]

def is_palin(s):
    return s == "".join(reversed(s))

def solve(ab, s):
    a = ab[0]
    b = ab[1]
    n = a+b
    c = 0

    if n%2 == 0:
        if a%2 == 1:
            return '-1'

    for i in s:
        if i == '0':
            a -= 1
        if i == '1':
            b -= 1
        if i == '?':
            c += 1
    
    ind = 0
    while ind < n//2 and c>=0:
        if s[ind] == '?' and s[n-1-ind] != '?':
            if s[n-1-ind] == '1':
                s = change(s,ind,s[n-1-ind])
                b -= 1
            else:
                s = change(s,ind,s[n-1-ind])
                a -= 1
            c -= 1
        elif s[ind] != '?' and s[n-1-ind] == '?':
            if s[ind] == '1':
                s = change(s,n-1-ind,s[ind])
                b -= 1
            else:
                s = change(s,n-1-ind,s[ind])
                a -= 1
            c -= 1
        elif s[ind] == '?' and s[n-1-ind] == '?':
            if a>=b:
                s = change(s,ind,'0')
                s = change(s,n-1-ind,'0')
                a -= 2
            else:
                s = change(s,ind,'1')
                s = change(s,n-1-ind,'1')
                b -= 2
            c -= 2
        ind += 1
        
    if not is_palin(s):
        return '-1'
    
    if a == 1:
        s = change(s,n//2,'0')
        a -= 1
        c -= 1

    if b == 1:
        s = change(s,n//2,'1')
        b -= 1
        c -= 1

    if is_palin(s) and a == 0 and b == 0 and c == 0:
        return s
    return '-1'

t = int(input())
for i in range(t):
    ab = list(map(int,input().strip().split()))[:2]
    s = input()
    result = solve(ab, s)
    print(result) 
