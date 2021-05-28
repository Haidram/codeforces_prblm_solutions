def solve(n,s):
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

t = int(input())
for i in range(t):
    n = int(input())
    s = input()
    result = solve(n,s)
    print(result)
