sum_n = int(input())
n = 1
while True:
    temp = n*(n+1)*(n+2)
    if temp > 6*sum_n:
        break
    n += 1
print(n-1)
