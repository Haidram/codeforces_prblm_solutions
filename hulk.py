num = int(input())
s1 = "I hate it"
s2 = "I hate that I love it"
s = num
while num > 2:
    if num%2 == 0:
        s2 = "I hate that I love that " + s2
    else:
        s1 = "I hate that I love that " + s1
    num -= 2
        
if s%2 == 0:
    print(s2)
else:
    print(s1)
