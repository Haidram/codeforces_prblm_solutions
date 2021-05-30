def solve(n, a):
## Initializing count of drink and health
    count = health = 0

    i = 0
    while i < len(a):
        health += a[i]
        count += 1

## If the health goes below 0, then check for another drink whose value
#  is more negative than this one, and leave the most negative one.
        if health < 0:
            min_dam = min(a[:i+1])
            a.remove(min_dam)
            health -= min_dam
            count -= 1
            continue
        i += 1

    return count



## Taking inputs
n = int(input())
a = list(map(int,input().strip().split()))[:n]
print(solve(n, a))
