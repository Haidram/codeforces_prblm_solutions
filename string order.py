a = ""
b = ""
a += input()
b += input()
flag = 0
for i in range(len(a)):
    if ord(a[i].lower())-ord(b[i].lower()) > 0:
        flag +=1
    if ord(a[i].lower())-ord(b[i].lower()) < 0:
        flag -= 1
    if flag != 0 and flag > 0:
        print("1")
        break
    if flag != 0 and flag < 0:
        print("-1")
        break
if flag == 0:
    print("0")
