n = int(input())
for i in range(n):
    a = int(input())
    if a == 1 or a == 2:
        print(0)
    else:
        b = int(a/2)
        print(a-b-1)
