arr = list(map(int,input().strip().split()))[:2]
a = arr[0]
b = arr[1]
temp = max(a,b)
c = 7 - temp
if c == 1:
    print("{}/{}".format(1,6))
elif c == 2:
    print("{}/{}".format(1,3))
elif c == 3:
    print("{}/{}".format(1,2))
elif c == 4:
    print("{}/{}".format(2,3))
elif c == 5:
    print("{}/{}".format(5,6))
elif c == 6:
    print("{}/{}".format(1,1))
