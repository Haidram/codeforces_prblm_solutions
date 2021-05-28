n = int(input())
a = []
passengers = 0
maxCapacity = 0
for i in range(n):
    a = list(map(int,input().strip().split()))[:2]
    passengers += a[1]-a[0]
    if passengers > maxCapacity:
        maxCapacity = passengers

print(maxCapacity)
