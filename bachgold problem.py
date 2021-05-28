n = int(input())
print(n//2)
if n%2 == 0:
    a = ["2"]*(n//2)
    print(" ".join(a))
else:
    a = ["2"]*((n//2)-1)
    a.append("3")
    print(" ".join(a))
