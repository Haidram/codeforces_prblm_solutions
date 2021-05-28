def findAns(a,b,x):
    a.sort()
    b.sort()
    b.reverse()
    for j in range(len(a)):
        if a[j] + b[j] > x:
            return "No"
    return "Yes"

flag = input("Want to continue(y/n): ")
if flag.lower() == "y":
    t = int(input("Enter t: "))
    for i in range(t):
        arr = list(map(int,input("Enter n and x: ").strip().split()))[:2]
        n = arr[0]
        x = arr[1]
        a = list(map(int,input("Enter a: ").strip().split()))[:n]
        b = list(map(int,input("Enter b: ").strip().split()))[:n]
        result = findAns(a,b,x)
        print(result)
        if i != t-1:
            empty_null = input()
else:
    exit()
