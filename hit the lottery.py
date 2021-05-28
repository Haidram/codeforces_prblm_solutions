n = int(input())
count = 0
if n >= 100:
    count += int(n/100)
    n = n%100
if n >= 20:
    count += int(n/20)
    n = n%20
if n >= 10:
    count += int(n/10)
    n = n%10
if n >= 5:
    count += int(n/5)
    n = n%5
if n > 0:
    count += n
print(count)
