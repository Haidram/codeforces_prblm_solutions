s = ""
outputString = ""
s = input()
a = []
i = 0
while i < len(s):
    a.append(s[i])
    i += 2

for i in range(len(a)):
    for j in range(len(a)-i):
        if j <= len(a)-2:
            b = 0
            if a[j] > a[j+1]:
                b = a[j]
                a[j] = a[j+1]
                a[j+1] = b
x = 0
while x <= len(a)-1:
    if x != len(a)-1:
        outputString += str(a[x]) + "+"
    else:
        outputString += str(a[i])
    x += 1
        
print(outputString)
