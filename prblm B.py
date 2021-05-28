import math
def result(n):
    if n%2 == 1:
        return 'NO'

    m = n//2
    sr1 = int(math.sqrt(m))
    if sr1*sr1 == m:
        return 'YES'
    if m%2 == 1:
        return 'NO'

    k = m//2
    sr2 = int(math.sqrt(k))
    if sr2*sr2 == k:
        return 'YES'

    return 'NO'
    
t = int(input())
for i in range(t):
    n = int(input())
    print(result(n))
