a = int(input())
b = 0
if a <= 5:
    b = 1
elif a > 5 and a%5 == 0:
    b = int(a/5)
else:
    b = int(a/5) + 1
print(b)
