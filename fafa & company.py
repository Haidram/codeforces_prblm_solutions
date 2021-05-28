import math
def findFactors(x):
    i = 1
    count = 0
    while i < math.sqrt(x):
        if x/i == x//i:
            count += 1
        i += 1
    if math.sqrt(x) == int(math.sqrt(x)):
        return 2*count + 1
    else:
        return 2*count

n = int(input())
n_factor = findFactors(n)
print(n_factor-1)
