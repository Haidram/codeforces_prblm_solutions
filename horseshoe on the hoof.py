a = list(map(int,input().strip().split()))[:4]
b = list(set(a))
print(4 - len(b))
