def is_palin(s):
    return "".join(reversed(s)) == s

def if_palin(n,s):
    if n%2 == 0:
        return 'BOB'
    else:
        count = 0
        for j in s:
            if j == '0':
                count += 1

        if count == 1:
            return 'BOB'
        elif count == 2 and s[n//2] == '0':
            return 'DRAW'
        elif count > 2 and s[n//2] == '0':
            return 'ALICE'
        elif count >= 2 and s[n//2] == '1':
            return 'BOB'

def if_not_palin(n, s):
    if n%2 == 0:
        return 'ALICE'

    count = 0
    for i in s:
        if i == '0':
            count += 1
        if count > 2:
            return 'ALICE'

    if count == 2 and s[n//2] == '0':
        return 'DRAW'

    return 'ALICE'
        

def solve(n, s):
    if is_palin(s):
        ans = if_palin(n, s)
    else:
        ans = if_not_palin(n, s)

    return ans

t = int(input())
for i in range(t):
    n = int(input())
    s = input()
    result = solve(n,s)
    print(result)
