a = int(input())
inInt = 0
for i in range(a):
    b = ""
    b += input()
    if b == "++X" or b == "X++":
        inInt += 1
    else:
        inInt -= 1
print(inInt)
