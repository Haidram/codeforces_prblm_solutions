t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int,input().strip().split()))[:n]
    a = list(set(a))
    print(len(a))
