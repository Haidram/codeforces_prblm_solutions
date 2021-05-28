matrix = []
for i in range(5):
    a = []
    a = list(map(int,input().strip().split()))[:5]
    for j in range(5):
        if a[j] == 1:
            x_coord = i
            y_coord = j
    matrix.append(a)

num = abs(2 - x_coord) + abs(2 - y_coord)
print(num)
