def solve(nv):
    km_drive = nv[0] - 1
    fuel_capacity = nv[1]

    if fuel_capacity >= km_drive:
        return km_drive

    cost = fuel_capacity
    rem_km = km_drive - fuel_capacity + 1
    cost += ((rem_km * (rem_km + 1)//2) - 1)
    return cost
        


nv = list(map(int,input().strip().split()))[:2]
print(solve(nv))
