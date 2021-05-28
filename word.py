s = ""
s = input()
upper = 0
lower = 0
for i in range(len(s)):
    if ord(s[i])>=65 and ord(s[i]) <=90:
        upper += 1
    else:
        lower += 1
if lower>=upper:
    s = s.lower()
else:
    s = s.upper()
print(s)
