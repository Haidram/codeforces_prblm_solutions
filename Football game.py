n = int(input())
hostTeam = []
guestTeam = []
count = 0
for i in range(n):
    a = list(map(int,input().strip().split()))[:2]
    hostTeam.append(a[0])
    guestTeam.append(a[1])
for dress in guestTeam:
    for uniform in hostTeam:
        if dress == uniform:
            count += 1
print(count)
